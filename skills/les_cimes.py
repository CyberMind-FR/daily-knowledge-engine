from __future__ import annotations

from jinja2 import Template

from dke.models import DailyKnowledgeObject


class LesCimesSkill:
    name = "Les Cimes de Maurienne"

    def render_markdown(self, dko: DailyKnowledgeObject) -> str:
        sections = ["monde", "europe", "france", "maurienne", "vie_locale", "meteo", "lune", "histoire", "science", "technologie", "sante", "sport", "economie", "comptoir"]
        template = Template("""# 🏔️ LES CIMES DE MAURIENNE
## Revue de presse quotidienne vérifiée · {{ dko.publication_date }}
### Au comptoir des sommets

> Principe : aucune information non sourcée n'est publiée.

{% for section in sections %}{% set facts = dko.facts_for(section) %}{% if facts %}
## {{ section|replace('_', ' ')|upper }}
{% for fact in facts %}
### {{ fact.title }}
{{ fact.summary }}

Sources : {% for s in fact.sources %}{{ s.publisher or s.title }}{% if s.url %} · {{ s.url }}{% endif %}{% if not loop.last %}, {% endif %}{% endfor %}

{% endfor %}{% endif %}{% endfor %}
---

☕ **Mot du patron** : Mieux vaut une case vide qu'une fausse manchette.
""")
        return template.render(dko=dko, sections=sections)

    def render_html(self, dko: DailyKnowledgeObject) -> str:
        body = self.render_markdown(dko).replace("\n", "<br>\n")
        return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Les Cimes de Maurienne</title>
<style>
body {{ max-width: 980px; margin: 2rem auto; padding: 1rem; font-family: system-ui, sans-serif; background:#f4ead6; color:#241f18; }}
main {{ background:#fff8e8; border:3px solid #241f18; padding:2rem; box-shadow: 8px 8px 0 #241f18; }}
h1,h2,h3 {{ font-family: Georgia, serif; }}
</style>
</head>
<body><main>{body}</main></body></html>"""

    def render_image_prompt(self, dko: DailyKnowledgeObject) -> str:
        facts = "\n".join([f"- {f.section}: {f.title} — {f.summary}" for f in dko.publishable_facts()])
        return f"""Créer un poster BD quotidien en français intitulé LES CIMES DE MAURIENNE, daté {dko.publication_date}.
Style : revue de presse illustrée de bistrot alpin, personnages originaux, croquis simplifié, papier ivoire, encre noire, couleurs limitées, humour de comptoir.
Ne pas inventer d'information. Utiliser uniquement ces faits vérifiés ou contextuels :
{facts}
Inclure des cartouches : actualité, météo, lune, histoire du jour, sport, science/technologie/santé si disponibles, dessin du comptoir, mot du patron.
"""
