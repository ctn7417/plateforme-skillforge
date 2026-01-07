"""Workflow orchestration and automation primitives."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Iterable, Sequence


class StepStatus(str, Enum):
    """Lifecycle status for a workflow step."""

    SUCCESS = "success"
    FAILED = "failed"


@dataclass(frozen=True)
class StepResult:
    """Result of executing a workflow step."""

    name: str
    status: StepStatus
    payload: dict
    message: str = ""


@dataclass(frozen=True)
class WorkflowStep:
    """A single step in an automated workflow."""

    name: str
    action: Callable[[dict], dict]
    description: str = ""

    def run(self, payload: dict) -> StepResult:
        """Run the workflow step and return the step result."""
        try:
            updated = self.action(payload)
        except Exception as exc:  # pragma: no cover - defensive for orchestration safety
            return StepResult(
                name=self.name,
                status=StepStatus.FAILED,
                payload=payload,
                message=str(exc),
            )
        return StepResult(name=self.name, status=StepStatus.SUCCESS, payload=updated)


@dataclass(frozen=True)
class WorkflowReport:
    """Execution report for a workflow run."""

    status: StepStatus
    steps: Sequence[StepResult]
    final_payload: dict


@dataclass
class Workflow:
    """An ordered workflow with optional automation metadata."""

    name: str
    steps: Sequence[WorkflowStep]
    triggers: Iterable[str] = field(default_factory=tuple)
    owners: Sequence[str] = field(default_factory=tuple)

    def execute(self, payload: dict, *, with_report: bool = False) -> dict | WorkflowReport:
        """Execute all steps in order, returning the final payload or report."""
        state = dict(payload)
        results = []
        status = StepStatus.SUCCESS
        for step in self.steps:
            result = step.run(state)
            results.append(result)
            if result.status is StepStatus.FAILED:
                status = StepStatus.FAILED
                state = result.payload
                break
            state = result.payload
        if with_report:
            return WorkflowReport(status=status, steps=tuple(results), final_payload=state)
        return state


@dataclass(frozen=True)
class AutomationRule:
    """Automation rule that decides when to run workflows."""

    name: str
    trigger: str
    workflow: Workflow
    condition: Callable[[dict], bool]

    def should_run(self, event: dict) -> bool:
        """Determine if the workflow should run for the incoming event."""
        return self.trigger == event.get("type") and self.condition(event)

    def run(self, event: dict, *, with_report: bool = False) -> dict:
        """Execute the workflow if the condition is met."""
        if not self.should_run(event):
            return {"status": "skipped", "workflow": self.workflow.name}
        result = self.workflow.execute(event, with_report=with_report)
        return {"status": "completed", "workflow": self.workflow.name, "result": result}
