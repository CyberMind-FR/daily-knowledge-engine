# Skill · Daily Knowledge Engine SpiritualCept

## Mission

Produire chaque jour une base de connaissances vérifiée, puis la décliner en publications éditoriales : Les Cimes de Maurienne, Le Café Quantique, L'Écho des Cimes.

## Commande utilisateur typique

- "Édition du jour"
- "Version BD quotidienne"
- "Poster Les Cimes"
- "Café Quantique du jour"

## Chaîne obligatoire

1. Collecter les faits du jour.
2. Associer chaque fait à une source.
3. Vérifier date, lieu, chiffre, calendrier, résultat.
4. Rejeter toute information non sourcée.
5. Générer un objet DailyKnowledgeObject.
6. Adapter le ton selon la publication.
7. Générer Markdown, HTML et prompt image.

## Règle cardinale

> Mieux vaut une case vide qu'une fausse manchette.

## Seuil de publication

Un fait est publiable seulement si :

- `status` est `verified` ou `context` ;
- `confidence >= 3` ;
- au moins une source existe.

## Interdictions

- Inventer une étape sportive.
- Inventer une météo ou vigilance.
- Inventer un résultat de match.
- Inventer une découverte scientifique.
- Transformer une hypothèse en actualité.

## Style Les Cimes de Maurienne

Revue de presse BD alpine, bistrot de montagne, humour de comptoir, personnages originaux, ton populaire mais rigoureux.
