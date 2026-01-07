"""Configuration et utilitaires pour les rappels de formation."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class ReminderRule:
    name: str
    offset_days: int
    description: str
    send_after_due: bool = False


@dataclass(frozen=True)
class Segment:
    name: str
    description: str
    criteria: str


@dataclass(frozen=True)
class EmailTemplate:
    key: str
    subject: str
    body: str
    cta_text: str
    cta_url: str
    variables: tuple[str, ...]


@dataclass(frozen=True)
class AuditEntry:
    recipient: str
    template_key: str
    segment: str
    sent_at: str


DEFAULT_REMINDER_RULES: tuple[ReminderRule, ...] = (
    ReminderRule(
        name="J-7",
        offset_days=-7,
        description="Rappel 7 jours avant l'échéance",
    ),
    ReminderRule(
        name="J-3",
        offset_days=-3,
        description="Rappel 3 jours avant l'échéance",
    ),
    ReminderRule(
        name="J-1",
        offset_days=-1,
        description="Rappel 1 jour avant l'échéance",
    ),
    ReminderRule(
        name="Relance J+1",
        offset_days=1,
        description="Relance après dépassement de l'échéance",
        send_after_due=True,
    ),
)

DEFAULT_SEGMENTS: tuple[Segment, ...] = (
    Segment(
        name="utilisateur_en_retard",
        description="Utilisateurs ayant dépassé la date limite",
        criteria="date_limite < aujourd'hui",
    ),
    Segment(
        name="utilisateur_a_risque",
        description="Utilisateurs proches de la date limite",
        criteria="date_limite dans les 7 jours",
    ),
    Segment(
        name="nouveau_obligatoire",
        description="Nouveaux inscrits avec formation obligatoire",
        criteria="inscription < 7 jours",
    ),
)

CTA_TEXT = "Accéder au portail formation"
CTA_URL = "https://intranet.example.com/formation"

DEFAULT_TEMPLATES: tuple[EmailTemplate, ...] = (
    EmailTemplate(
        key="rappel_avant_echeance",
        subject="[Action requise] {cours} avant le {date_limite}",
        body=(
            "Bonjour {nom},\n\n"
            "Votre formation {cours} arrive bientôt à échéance (le {date_limite}). "
            "Merci de finaliser vos modules avant cette date."
        ),
        cta_text=CTA_TEXT,
        cta_url=CTA_URL,
        variables=("nom", "cours", "date_limite"),
    ),
    EmailTemplate(
        key="relance_apres_echeance",
        subject="[Relance] {cours} en retard depuis le {date_limite}",
        body=(
            "Bonjour {nom},\n\n"
            "Votre formation {cours} était attendue pour le {date_limite}. "
            "Merci de vous connecter au portail pour la finaliser au plus vite."
        ),
        cta_text=CTA_TEXT,
        cta_url=CTA_URL,
        variables=("nom", "cours", "date_limite"),
    ),
)


class AuditLogger:
    def __init__(self, log_path: Path) -> None:
        self._log_path = log_path

    def record_send(self, *, recipient: str, template_key: str, segment: str) -> AuditEntry:
        entry = AuditEntry(
            recipient=recipient,
            template_key=template_key,
            segment=segment,
            sent_at=datetime.now(timezone.utc).isoformat(),
        )
        self._append_entry(entry)
        return entry

    def _append_entry(self, entry: AuditEntry) -> None:
        self._log_path.parent.mkdir(parents=True, exist_ok=True)
        with self._log_path.open("a", encoding="utf-8") as handle:
            handle.write(
                f"{entry.recipient}|{entry.template_key}|{entry.segment}|{entry.sent_at}\n"
            )


def render_template(template: EmailTemplate, variables: dict[str, str]) -> dict[str, str]:
    _validate_variables(template, variables)
    return {
        "subject": template.subject.format(**variables),
        "body": template.body.format(**variables),
        "cta_text": template.cta_text,
        "cta_url": template.cta_url,
    }


def _validate_variables(template: EmailTemplate, variables: dict[str, str]) -> None:
    missing = [name for name in template.variables if name not in variables]
    if missing:
        raise ValueError(f"Variables manquantes: {', '.join(missing)}")


def list_rules(rules: Iterable[ReminderRule] = DEFAULT_REMINDER_RULES) -> list[dict[str, str]]:
    return [
        {
            "nom": rule.name,
            "decalage_jours": str(rule.offset_days),
            "description": rule.description,
            "apres_echeance": "oui" if rule.send_after_due else "non",
        }
        for rule in rules
    ]


def list_segments(segments: Iterable[Segment] = DEFAULT_SEGMENTS) -> list[dict[str, str]]:
    return [
        {
            "nom": segment.name,
            "description": segment.description,
            "criteres": segment.criteria,
        }
        for segment in segments
    ]


def list_templates(
    templates: Iterable[EmailTemplate] = DEFAULT_TEMPLATES,
) -> list[dict[str, str]]:
    return [
        {
            "cle": template.key,
            "sujet": template.subject,
            "corps": template.body,
            "cta": template.cta_text,
            "cta_url": template.cta_url,
            "variables": ", ".join(template.variables),
        }
        for template in templates
    ]
