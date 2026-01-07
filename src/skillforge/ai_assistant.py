"""AI assistance module definitions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class AIAssistantPolicy:
    """Policy rules to determine when AI assistance is allowed."""

    allowed_regions: Iterable[str]
    required_consents: Iterable[str]

    def allows(self, region: str, consents: Iterable[str]) -> bool:
        """Return True when the region and consents are sufficient."""
        return region in set(self.allowed_regions) and set(self.required_consents).issubset(
            set(consents)
        )


@dataclass(frozen=True)
class AIAssistantDecision:
    """Decision describing eligibility and safeguards for AI assistance."""

    allowed: bool
    reasons: tuple[str, ...]


@dataclass(frozen=True)
class AIAssistantModule:
    """Representation of an AI assistance capability."""

    name: str
    description: str
    policy: AIAssistantPolicy

    def is_applicable(self, region: str, consents: Iterable[str]) -> bool:
        """Check if the module can be enabled for a given context."""
        return self.policy.allows(region, consents)

    def evaluate(self, region: str, consents: Iterable[str]) -> AIAssistantDecision:
        """Return a detailed decision with reasons for enablement."""
        reasons = []
        if region not in set(self.policy.allowed_regions):
            reasons.append(f"Region '{region}' is not eligible.")
        missing = set(self.policy.required_consents) - set(consents)
        if missing:
            reasons.append(f"Missing required consents: {', '.join(sorted(missing))}.")
        allowed = not reasons
        if allowed:
            reasons.append("All eligibility checks passed.")
        return AIAssistantDecision(allowed=allowed, reasons=tuple(reasons))
