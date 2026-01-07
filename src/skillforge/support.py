"""Support tiers and SLA definitions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class SupportTier:
    """Support tier with coverage and escalation commitments."""

    name: str
    coverage_hours: str
    escalation_path: str


@dataclass(frozen=True)
class SLAPlan:
    """Service-level agreement plan."""

    name: str
    response_targets_minutes: Mapping[str, int]
    resolution_targets_hours: Mapping[str, int]
    support_tier: SupportTier

    def response_time_for(self, severity: str) -> int:
        """Return the response target for a given severity level."""
        return self.response_targets_minutes.get(severity, 0)

    def resolution_time_for(self, severity: str) -> int:
        """Return the resolution target for a given severity level."""
        return self.resolution_targets_hours.get(severity, 0)

    def evaluate_incident(self, severity: str, *, response_minutes: int, resolution_hours: int) -> dict:
        """Evaluate an incident against SLA targets."""
        response_target = self.response_time_for(severity)
        resolution_target = self.resolution_time_for(severity)
        response_met = response_target == 0 or response_minutes <= response_target
        resolution_met = resolution_target == 0 or resolution_hours <= resolution_target
        return {
            "severity": severity,
            "response_target_minutes": response_target,
            "resolution_target_hours": resolution_target,
            "response_met": response_met,
            "resolution_met": resolution_met,
            "sla_met": response_met and resolution_met,
        }
