from __future__ import annotations

from dke.models import DailyKnowledgeObject, VerificationStatus


class VerificationError(Exception):
    pass


def enforce_publication_rules(dko: DailyKnowledgeObject) -> DailyKnowledgeObject:
    """Reject facts that cannot be safely published.

    Hard rule: no source, no publication. The function does not invent replacements.
    """
    cleaned = dko.model_copy(deep=True)
    for fact in cleaned.facts:
        if fact.status == VerificationStatus.verified and not fact.sources:
            fact.status = VerificationStatus.rejected
            fact.confidence = 0
            fact.note = "Rejected: verified fact without source."
        if fact.confidence < 3:
            fact.status = VerificationStatus.rejected
            fact.note = "Rejected: confidence below publication threshold."
    return cleaned
