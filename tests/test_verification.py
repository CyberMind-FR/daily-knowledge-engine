from datetime import date

from dke.models import DailyKnowledgeObject, Fact, VerificationStatus
from dke.verify import enforce_publication_rules


def test_verified_fact_without_source_is_rejected():
    dko = DailyKnowledgeObject(publication_date=date(2026, 7, 4), facts=[
        Fact(section="sport", title="Fake match", summary="Unsourced", status=VerificationStatus.verified, confidence=5, sources=[])
    ])
    cleaned = enforce_publication_rules(dko)
    assert cleaned.facts[0].status == VerificationStatus.rejected


def test_low_confidence_is_rejected():
    dko = DailyKnowledgeObject(publication_date=date(2026, 7, 4), facts=[
        Fact(section="local", title="Rumor", summary="Low confidence", status=VerificationStatus.context, confidence=2, sources=[])
    ])
    cleaned = enforce_publication_rules(dko)
    assert cleaned.facts[0].status == VerificationStatus.rejected
