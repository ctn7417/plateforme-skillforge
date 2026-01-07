# Cadre QA/UAT

## 1. Phases QA (interne) vs UAT (client/utilisateur)

| Aspect | QA (interne) | UAT (client/utilisateur) |
| --- | --- | --- |
| Objectif | Vérifier la qualité technique et fonctionnelle avant exposition client. | Valider que le produit répond aux besoins métier et aux scénarios réels. |
| Responsables | Équipe QA + Tech Lead. | Product Owner + représentants utilisateurs. |
| Environnement | Intégration/staging contrôlé. | Staging proche production, avec données/flux représentatifs. |
| Critères d’entrée | Build stable, tests critiques passés, environnement prêt. | Fonctionnalités clés figées, bugs critiques QA résolus. |
| Critères de sortie | Zéro bug bloquant/critique, risques documentés. | Acceptation formelle, dérogations signées si nécessaire. |

## 2. Couverture minimale

### QA (interne)
- **Tests critiques** : authentification, parcours principal, paiements/transactions si applicable, gestion des droits.
- **Smoke tests** : démarrage application, pages clés, API essentielles, intégration systèmes tiers.
- **Non-régression** : scénarios des bugs majeurs corrigés, modules à fort risque.

### UAT
- **Parcours métier prioritaires** : scénarios définis par le PO et les utilisateurs clés.
- **Validation UX/ergonomie** : cohérence des libellés, navigation, clarté des messages.
- **Conformité** : règles métiers, exigences légales ou contractuelles.

## 3. Outils recommandés

- **Automatisation** : Playwright/Cypress pour UI, Postman/Newman pour API.
- **Tracking** : Jira/Linear/YouTrack avec workflow dédié QA/UAT.
- **Reporting** : tableaux de bord (Jira, Allure, ou rapports CI/CD) + synthèse hebdomadaire.

## 4. Responsable validation (RACI)

- **QA Lead** : Responsable (R) de l’exécution QA, qualité des tests, consolidation des résultats.
- **Tech Lead** : Consulté (C) sur la faisabilité technique, impact correctifs, risques.
- **Product Owner** : Compte (A) en UAT, donne l’acceptation finale.
- **Équipe projet** : Informée (I) de l’état et des décisions.

## 5. Délais de correction et critères de sortie

### Délais de correction (SLA)
- **Bloquant/Critique** : 24–48h.
- **Majeur** : 3–5 jours ouvrés.
- **Mineur** : cycle suivant ou planifié.

### Critères de sortie QA
- 0 bug bloquant/critique ouvert.
- Taux de réussite des tests critiques ≥ 95%.
- Rapport QA validé par QA Lead.

### Critères de sortie UAT
- Acceptation formelle par le Product Owner.
- Liste de dérogations documentée et signée.
- Plan de mise en production validé.
