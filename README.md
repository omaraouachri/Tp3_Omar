

```markdown
# Quick Start

## Installation des Dépendances

```
pip install -r requirements.txt
```
## Expansion de Requête et Classement

Ce code vise à répondre à une requête envoyée par l'utilisateur. Pour cela, le code effectue d'abord le traitement nécessaire pour la requête, puis filtre les documents qui contiennent un ou plusieurs des tokens de la requête.

Ensuite, les documents filtrés sont utilisés pour attribuer un score à chaque document. Deux fonctions ont été implémentées à cet effet :

- **calculate_score_occurances**: qui prend en compte l'importance du nombre d'occurrences des tokens dans les documents.
  
- **calculate_score_positions**: qui prend en compte la position des mots-clés et donne un score plus élevé aux documents qui correspondent à la position. Elle applique également un poids plus important aux tokens qui ont un sens par rapport aux stop words.

À la fin, le code génère un fichier `resultat.json` qui contient :

- l'ID des documents, leurs titres et leurs URLs,
- leurs scores qui sont calculés par la fonction `calculate_score_positions`,
- le nombre de documents dans l'index,
- le nombre de documents ayant survécu au filtre.

## Exécution du Code

Pour exécuter le code, spécifiez la requête et le mode :

Le mode :

- **ET** si vous souhaitez que les documents contiennent tous les tokens de la requête.
  
- **OU** si vous souhaitez que les documents contiennent au moins un token de la requête.

```bash
python3 main.py --query "Ce sont les fautes fatales" --mode OU
```

