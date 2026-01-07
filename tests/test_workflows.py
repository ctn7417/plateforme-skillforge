import unittest

from skillforge.workflows import AutomationRule, StepStatus, Workflow, WorkflowStep


class WorkflowTests(unittest.TestCase):
    def test_workflow_executes_steps(self):
        def add_one(payload):
            payload["value"] += 1
            return payload

        def add_two(payload):
            payload["value"] += 2
            return payload

        workflow = Workflow(
            name="onboarding",
            steps=[
                WorkflowStep(name="add-one", action=add_one),
                WorkflowStep(name="add-two", action=add_two),
            ],
        )

        report = workflow.execute({"value": 0}, with_report=True)
        self.assertEqual(report.status, StepStatus.SUCCESS)
        self.assertEqual(report.final_payload["value"], 3)

    def test_automation_rule_runs_when_triggered(self):
        workflow = Workflow(name="triage", steps=[WorkflowStep(name="noop", action=lambda p: p)])
        rule = AutomationRule(
            name="incident-triage",
            trigger="incident",
            workflow=workflow,
            condition=lambda event: event.get("severity") == "high",
        )

        event = {"type": "incident", "severity": "high"}
        result = rule.run(event, with_report=True)
        self.assertEqual(result["status"], "completed")


if __name__ == "__main__":
    unittest.main()
