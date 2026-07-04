from __future__ import annotations

from datetime import date
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field


class VerificationStatus(str, Enum):
    verified = "verified"
    context = "context"
    unverified = "unverified"
    rejected = "rejected"


class Source(BaseModel):
    title: str
    url: Optional[str] = None
    publisher: Optional[str] = None
    published_at: Optional[str] = None
    accessed_at: Optional[str] = None


class Fact(BaseModel):
    section: str
    title: str
    summary: str
    status: VerificationStatus
    confidence: int = Field(ge=0, le=5)
    sources: List[Source] = Field(default_factory=list)
    note: Optional[str] = None

    def publishable(self) -> bool:
        return self.status in {VerificationStatus.verified, VerificationStatus.context} and self.confidence >= 3 and bool(self.sources)


class DailyKnowledgeObject(BaseModel):
    publication_date: date
    location_label: str = "Maurienne"
    facts: List[Fact] = Field(default_factory=list)

    def facts_for(self, section: str) -> List[Fact]:
        return [f for f in self.facts if f.section == section and f.publishable()]

    def publishable_facts(self) -> List[Fact]:
        return [f for f in self.facts if f.publishable()]
