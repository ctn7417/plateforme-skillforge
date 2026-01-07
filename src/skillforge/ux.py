"""UX experimentation and micro-optimization utilities."""

from __future__ import annotations

from dataclasses import dataclass
from statistics import mean
from typing import Iterable


@dataclass(frozen=True)
class UXMetrics:
    """Key UX metrics captured during experiments."""

    task_success_rate: float
    time_on_task_seconds: float
    satisfaction_score: float

    def score(self) -> float:
        """Aggregate score used to rank micro-optimizations."""
        return (self.task_success_rate * 0.5) + (self.satisfaction_score * 0.5)

    def meets_guardrails(self, *, min_success_rate: float, min_satisfaction: float) -> bool:
        """Return True when the metrics meet guardrail thresholds."""
        return self.task_success_rate >= min_success_rate and self.satisfaction_score >= min_satisfaction


@dataclass(frozen=True)
class Experiment:
    """Definition for a UX experiment."""

    name: str
    hypothesis: str
    metrics: UXMetrics


def evaluate_micro_optimizations(
    experiments: Iterable[Experiment],
    *,
    baseline: UXMetrics | None = None,
    min_success_rate: float = 0.7,
    min_satisfaction: float = 0.6,
) -> dict:
    """Summarize experiments and highlight opportunities."""
    experiments = list(experiments)
    if not experiments:
        return {
            "status": "no-data",
            "recommendation": "Collect baseline UX metrics before optimizations.",
        }

    guarded = [
        exp for exp in experiments if exp.metrics.meets_guardrails(
            min_success_rate=min_success_rate,
            min_satisfaction=min_satisfaction,
        )
    ]
    candidate_pool = guarded or experiments
    top_experiment = max(candidate_pool, key=lambda exp: exp.metrics.score())
    average_time = mean(exp.metrics.time_on_task_seconds for exp in experiments)

    improvements = None
    if baseline:
        improvements = {
            "task_success_rate_delta": round(top_experiment.metrics.task_success_rate - baseline.task_success_rate, 3),
            "satisfaction_delta": round(top_experiment.metrics.satisfaction_score - baseline.satisfaction_score, 3),
            "time_on_task_delta_seconds": round(top_experiment.metrics.time_on_task_seconds - baseline.time_on_task_seconds, 2),
        }

    return {
        "status": "ready",
        "top_candidate": top_experiment.name,
        "average_time_on_task_seconds": round(average_time, 2),
        "guardrails_met": top_experiment.metrics.meets_guardrails(
            min_success_rate=min_success_rate,
            min_satisfaction=min_satisfaction,
        ),
        "improvements_vs_baseline": improvements,
        "recommendation": (
            f"Prioritize '{top_experiment.name}' and target a {average_time:.1f}s task time."
        ),
    }
