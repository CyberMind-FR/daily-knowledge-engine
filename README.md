# Daily Knowledge Engine · SpiritualCept

Moteur éditorial quotidien vérifié pour générer des publications comme **Les Cimes de Maurienne**, **Le Café Quantique** et **L'Écho des Cimes**.

Objectif : collecter des faits datés, les vérifier, puis produire des sorties éditoriales illustrables sans inventer d'actualité.

## Commandes rapides

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
python -m dke.cli --publication les-cimes --date 2026-07-04 --out dist
```

## Générer le prompt image seulement

```bash
python -m dke.cli --publication les-cimes --out dist --image-dry-run
```

Sorties :

```text
dist/
  les-cimes.md
  les-cimes.html
  les-cimes-image-prompt.txt
  les-cimes-poster.prompt.txt
```

## Générer l'image finale avec OpenAI

Installer l'option image :

```bash
pip install -e ".[dev,image]"
export OPENAI_API_KEY="sk-..."
python -m dke.cli \
  --publication les-cimes \
  --out dist \
  --image \
  --image-model gpt-image-1 \
  --image-size 1024x1536 \
  --image-quality medium
```

Sortie :

```text
dist/les-cimes-poster.png
```

## GitHub Actions

Deux workflows sont inclus :

- `.github/workflows/ci.yml` : tests + génération des artefacts texte.
- `.github/workflows/daily.yml` : génération quotidienne + option image finale.

Pour activer l'image finale :

1. GitHub → repository → Settings → Secrets and variables → Actions.
2. Ajouter un secret : `OPENAI_API_KEY`.
3. Lancer `Daily Les Cimes` en manuel avec `generate_image=true`.

Le mode planifié quotidien génère par défaut le prompt en dry-run, afin d'éviter des coûts API involontaires.

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
  .github/workflows/   CI et génération quotidienne
```

## Publications disponibles

| Publication | Angle | Sorties |
|---|---|---|
| Les Cimes de Maurienne | revue de presse BD alpine | Markdown, HTML, prompt image, PNG OpenAI optionnel |
| Le Café Quantique | science, IA, cyber, espace | à étendre |
| L'Écho des Cimes | patrimoine, culture, histoire | à étendre |

## Sources

Cette base embarque un mode `sample` pour tester sans réseau. En production, brancher les connecteurs : météo, actualités, sport, astronomie, finance, sources locales.
