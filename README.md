# Daily Knowledge Engine · SpiritualCept

Moteur éditorial quotidien vérifié pour générer des publications comme **Les Cimes de Maurienne**, **Le Café Quantique** et **L'Écho des Cimes**.

Objectif : collecter des faits datés, les vérifier, puis produire des sorties éditoriales illustrables sans inventer d'actualité.

## Commandes rapides

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
python -m dke.cli --publication les-cimes --date 2026-07-04 --out dist
```

## Principe éditorial

> Mieux vaut une case vide qu'une fausse manchette.

Chaque information publiée doit porter :

- une source ;
- une date de consultation ou de publication ;
- un niveau de confiance ;
- un statut : `verified`, `context`, `unverified`, `rejected`.

Les sorties bloquent automatiquement les informations `unverified` et `rejected`.

## Architecture

```text
daily-knowledge-engine/
  dke/                 moteur commun
  skills/              publications spécialisées
  render/              rendus Markdown / HTML
  templates/           styles éditoriaux
  tests/               tests de non-régression
  examples/            objets de connaissance exemples
  .github/workflows/   CI GitHub Actions
```

## Publications disponibles

| Publication | Angle | Sorties |
|---|---|---|
| Les Cimes de Maurienne | revue de presse BD alpine | Markdown, HTML, prompt image |
| Le Café Quantique | science, IA, cyber, espace | à étendre |
| L'Écho des Cimes | patrimoine, culture, histoire | à étendre |

## Sources

Cette base embarque un mode `sample` pour tester sans réseau. En production, brancher les connecteurs : météo, actualités, sport, astronomie, finance, sources locales.

