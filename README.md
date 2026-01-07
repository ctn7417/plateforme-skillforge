# Cadre d’évaluation Impact / Effort

## 1) Grille d’impact (1–5)
Échelle proposée (1 = très faible, 5 = très élevé) :

- **Revenus** : contribution directe aux revenus.
- **Conversion** : impact sur le taux de conversion.
- **Rétention** : capacité à faire revenir les utilisateurs.
- **Différenciation** : avantage compétitif perçu.
- **Réduction du churn** : diminution des résiliations / désabonnements.

## 2) Grille d’effort (1–5)
Échelle proposée (1 = faible effort, 5 = effort très élevé) :

- **Complexité technique** : difficulté de conception / implémentation.
- **Dépendances** : nombre et criticité des dépendances internes/externes.
- **Charge Front / Back / Data** : volume de travail par domaine.
- **Risques** : risques techniques, produit, sécurité ou conformité.

## 3) Alignement des grilles (30–45 min)
Plan d’atelier pour calibrer les scores :

1. Présenter les définitions des critères (impact + effort).
2. Valider ensemble les exemples de notes 1–5.
3. Ajuster les grilles si un critère est redondant ou incomplet.
4. Conclure par une grille finalisée et partagée.

## 4) Scoring des fonctionnalités
Pour chaque fonctionnalité :

- Attribuer un score **Impact** (1–5) et **Effort** (1–5).
- **Justification courte (1–2 phrases)** par score, factuelle et actionnable.

Exemple de justification :

- *Impact 4* : « Augmente la conversion sur le tunnel principal selon les tests A/B. »
- *Effort 2* : « Réutilise les composants existants, peu de dépendances. »

## 5) Synthèse en matrice 2x2
Positionner chaque fonctionnalité dans la matrice :

- **Quick Wins** (Impact élevé / Effort faible)
- **Big Bets** (Impact élevé / Effort élevé)
- **Fill-ins** (Impact faible / Effort faible)
- **Money Pit** (Impact faible / Effort élevé)

Conserver **le détail des scores** dans un tableau récapitulatif.

### Exemple de tableau de scoring

| Fonctionnalité | Impact (1–5) | Effort (1–5) | Justification | Catégorie |
|---|---:|---:|---|---|
| Recherche avancée | 4 | 3 | Améliore la conversion sur le segment power users. | Big Bet |
| Export CSV | 2 | 1 | Demande récurrente, faible effort. | Fill-in |
