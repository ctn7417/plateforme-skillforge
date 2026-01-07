import unittest

from skillforge.ai_assistant import AIAssistantModule, AIAssistantPolicy
from skillforge.scaling import (
    CostProfile,
    ScalingPlan,
    estimate_monthly_cost,
    recommend_cost_optimizations,
)
from skillforge.support import SLAPlan, SupportTier
from skillforge.ux import Experiment, UXMetrics, evaluate_micro_optimizations


class UXTests(unittest.TestCase):
    def test_micro_optimization_summary(self):
        experiments = [
            Experiment(
                name="navigation-relabel",
                hypothesis="Clearer labels improve task completion.",
                metrics=UXMetrics(task_success_rate=0.8, time_on_task_seconds=40, satisfaction_score=0.7),
            ),
            Experiment(
                name="inline-help",
                hypothesis="Inline guidance reduces time-on-task.",
                metrics=UXMetrics(task_success_rate=0.9, time_on_task_seconds=30, satisfaction_score=0.9),
            ),
        ]

        baseline = UXMetrics(task_success_rate=0.7, time_on_task_seconds=45, satisfaction_score=0.6)
        summary = evaluate_micro_optimizations(experiments, baseline=baseline)
        self.assertEqual(summary["top_candidate"], "inline-help")
        self.assertTrue(summary["guardrails_met"])
        self.assertIn("improvements_vs_baseline", summary)


class AIAssistantTests(unittest.TestCase):
    def test_policy_allows_module(self):
        policy = AIAssistantPolicy(allowed_regions=["EU"], required_consents=["terms", "ai"])
        module = AIAssistantModule(name="coach", description="AI coach", policy=policy)

        self.assertTrue(module.is_applicable("EU", ["terms", "ai", "analytics"]))
        self.assertFalse(module.is_applicable("US", ["terms", "ai"]))

        decision = module.evaluate("EU", ["terms", "ai"])
        self.assertTrue(decision.allowed)


class ScalingTests(unittest.TestCase):
    def test_cost_estimate(self):
        profiles = {
            "jobs": CostProfile(name="jobs", unit_cost=0.5, fixed_monthly_cost=10),
            "storage": CostProfile(name="storage", unit_cost=0.1, fixed_monthly_cost=5),
        }
        usage = {"jobs": 100, "storage": 50}

        estimate = estimate_monthly_cost(profiles, usage)
        self.assertEqual(estimate["total"], 70.0)

    def test_scaling_plan_recommendation(self):
        plan = ScalingPlan(min_capacity=2, max_capacity=10, scale_up_threshold=0.8, scale_down_threshold=0.3)

        self.assertEqual(plan.recommend_capacity(0.9), 10)
        self.assertEqual(plan.recommend_capacity(0.2), 2)
        self.assertEqual(plan.rightsizing_action(0.9), "scale-up")

    def test_cost_optimization_recommendations(self):
        profiles = {"jobs": CostProfile(name="jobs", unit_cost=0.5, fixed_monthly_cost=10)}
        usage = {"jobs": 0.05}
        recommendations = recommend_cost_optimizations(profiles, usage, idle_threshold=0.1)

        self.assertEqual(recommendations["count"], 1)


class SupportTests(unittest.TestCase):
    def test_sla_targets(self):
        tier = SupportTier(name="gold", coverage_hours="24/7", escalation_path="on-call")
        sla = SLAPlan(
            name="gold-sla",
            response_targets_minutes={"critical": 15},
            resolution_targets_hours={"critical": 4},
            support_tier=tier,
        )

        self.assertEqual(sla.response_time_for("critical"), 15)
        self.assertEqual(sla.resolution_time_for("critical"), 4)

        evaluation = sla.evaluate_incident("critical", response_minutes=10, resolution_hours=3)
        self.assertTrue(evaluation["sla_met"])


if __name__ == "__main__":
    unittest.main()
