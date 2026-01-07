# Matrice de priorisation

## Matrice (1–5)

| Domaine | Dépendances | Valeur | Risque | Justification courte |
| --- | --- | --- | --- | --- |
| Auth | 5 | 5 | 4 | Prérequis technique et sécurité pour tous les autres domaines. |
| Parcours | 4 | 4 | 3 | S’appuie sur l’auth; structure l’expérience utilisateur. |
| Questionnaires | 3 | 4 | 3 | Dépend des parcours pour l’enchaînement pédagogique. |
| Certificats | 2 | 3 | 2 | Dépend des questionnaires pour les résultats. |

## Validation de l’ordre

L’ordre **auth → parcours → questionnaires → certificats** est respecté, car chaque domaine dépend logiquement du précédent :

1. **Auth** : base d’accès, sécurité, et identification des utilisateurs.
2. **Parcours** : nécessite l’authentification pour attribuer et suivre un parcours.
3. **Questionnaires** : rattachés aux parcours et à la progression des utilisateurs.
4. **Certificats** : reposent sur les résultats des questionnaires.

## Décision et hypothèses

**Décision**
- Prioriser le travail selon l’ordre validé pour réduire les blocages et maximiser la valeur livrée tôt.

**Hypothèses**
- L’authentification est indispensable avant toute fonctionnalité métier.
- Les parcours définissent la structure qui conditionne les questionnaires.
- Les certificats ne peuvent être délivrés qu’après l’évaluation via questionnaires.
- Les risques sont principalement liés à la sécurité (auth) et à l’intégration des flux (parcours ↔ questionnaires).
