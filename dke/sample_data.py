from __future__ import annotations

from datetime import date

from dke.models import DailyKnowledgeObject, Fact, Source, VerificationStatus


def build_sample_dko(publication_date: date) -> DailyKnowledgeObject:
    """Offline sample used for tests and rendering.

    Replace with live connectors in production. Values are deliberately conservative.
    """
    src_tour = Source(title="Tour de France 2026 Grand Départ", publisher="letour.fr", url="https://www.letour.fr/", accessed_at=str(publication_date))
    src_meteo = Source(title="Prévisions Savoie", publisher="Météo-France", url="https://meteofrance.com/", accessed_at=str(publication_date))
    src_history = Source(title="4 July historical events", publisher="Encyclopaedia / historical reference", accessed_at=str(publication_date))
    src_moon = Source(title="Moon phase calendar", publisher="Astronomy reference", accessed_at=str(publication_date))

    return DailyKnowledgeObject(
        publication_date=publication_date,
        facts=[
            Fact(section="france", title="Fortes chaleurs", summary="La rubrique météo doit être confirmée par une source météo du jour avant publication.", status=VerificationStatus.context, confidence=3, sources=[src_meteo]),
            Fact(section="sport", title="Tour de France 2026", summary="Le Grand Départ 2026 est prévu à Barcelone. Ne publier l'étape du jour qu'après vérification officielle du parcours daté.", status=VerificationStatus.context, confidence=4, sources=[src_tour]),
            Fact(section="lune", title="Phase lunaire", summary="La phase de la Lune doit provenir d'un calendrier astronomique daté.", status=VerificationStatus.context, confidence=3, sources=[src_moon]),
            Fact(section="histoire", title="4 juillet", summary="Date associée notamment à la Déclaration d'indépendance des États-Unis en 1776.", status=VerificationStatus.context, confidence=4, sources=[src_history]),
            Fact(section="comptoir", title="Dessin du comptoir", summary="Tu crois qu'on vit une époque historique ? Oui... mais elle manque encore de recul.", status=VerificationStatus.context, confidence=4, sources=[src_history]),
        ],
    )
