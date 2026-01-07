"""Scalability and cost modeling utilities."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class CostProfile:
    """Cost profile for a workload, in arbitrary units."""

    name: str
    unit_cost: float
    fixed_monthly_cost: float = 0.0

    def estimate(self, usage_units: float) -> float:
        """Estimate monthly cost for a given usage volume."""
        return self.fixed_monthly_cost + (self.unit_cost * usage_units)


@dataclass(frozen=True)
class ScalingPlan:
    """Scaling plan that describes thresholds and target capacity."""

    min_capacity: int
    max_capacity: int
    scale_up_threshold: float
    scale_down_threshold: float

    def recommend_capacity(self, utilization: float) -> int:
        """Recommend a capacity based on utilization."""
        if utilization >= self.scale_up_threshold:
            return self.max_capacity
        if utilization <= self.scale_down_threshold:
            return self.min_capacity
        return int(round((self.min_capacity + self.max_capacity) / 2))

    def rightsizing_action(self, utilization: float) -> str:
        """Provide a human-readable rightsizing action."""
        if utilization >= self.scale_up_threshold:
            return "scale-up"
        if utilization <= self.scale_down_threshold:
            return "scale-down"
        return "hold"


def estimate_monthly_cost(profiles: Mapping[str, CostProfile], usage: Mapping[str, float]) -> dict:
    """Estimate monthly costs across multiple profiles."""
    breakdown = {}
    total = 0.0
    for name, profile in profiles.items():
        cost = profile.estimate(usage.get(name, 0.0))
        breakdown[name] = round(cost, 2)
        total += cost
    return {"total": round(total, 2), "breakdown": breakdown}


def recommend_cost_optimizations(
    profiles: Mapping[str, CostProfile],
    usage: Mapping[str, float],
    *,
    idle_threshold: float = 0.1,
) -> dict:
    """Recommend optimizations for low-usage cost centers."""
    opportunities = []
    for name, profile in profiles.items():
        units = usage.get(name, 0.0)
        if units <= idle_threshold and profile.fixed_monthly_cost > 0:
            opportunities.append(
                {
                    "profile": name,
                    "suggestion": "Consider pausing or consolidating fixed costs for low usage.",
                }
            )
    return {"opportunities": opportunities, "count": len(opportunities)}
