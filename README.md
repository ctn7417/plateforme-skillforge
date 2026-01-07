# Checklist de release - matrice par lot

Ce document définit une matrice de contrôle par lot de release, les critères de pass/fail, l’intégration aux rituels, les preuves attendues et le processus de validation.

## 1) Matrice par lot (fonctionnalités, performance, sécurité, compatibilité, observabilité)

**Définition d’un lot** : un ensemble cohérent de changements livré ensemble (ex. sprint, hotfix, release majeure).

| Lot | Catégorie | Item | Critère Pass | Critère Fail | Preuves attendues |
| --- | --- | --- | --- | --- | --- |
| L-XXX | Fonctionnalités | Couverture des stories et AC | 100% des user stories du lot validées, AC passés | Au moins un AC critique en échec ou non testé | Captures UAT, rapports d’exécution, liens tickets |
| L-XXX | Fonctionnalités | Non-régression clé | Scénarios critiques passés sur env cible | Régression sur un flux critique | Logs de tests, vidéos, captures |
| L-XXX | Performance | Temps de réponse P95 | P95 <= seuil défini pour les endpoints critiques | P95 > seuil ou variance > seuil d’alerte | Rapport APM, exports dashboard |
| L-XXX | Performance | Charge nominale | Stable au volume cible (CPU/RAM/latence) | Dégradation significative ou erreurs > seuil | Rapport de charge, graphiques |
| L-XXX | Sécurité | Vulnérabilités critiques | 0 vulnérabilité critique/haute ouverte | Vulnérabilité critique/haute non mitigée | Rapport SAST/DAST, ticket d’acceptation du risque |
| L-XXX | Sécurité | Secrets et accès | Aucun secret exposé, accès validés | Secrets détectés, accès non revus | Rapport scan secrets, revue IAM |
| L-XXX | Compatibilité | Navigateurs/clients cibles | OK sur la matrice supportée | Échec sur un client supporté | Captures par device, rapports tests |
| L-XXX | Compatibilité | Migration/DB | Migrations appliquées sans erreur | Échec de migration ou rollback impossible | Logs migration, plan rollback |
| L-XXX | Observabilité | Logs et traces | Logs structurés + traces pour parcours clés | Logs absents, incomplets ou non corrélés | Extraits logs, traces APM |
| L-XXX | Observabilité | Alertes et SLO | Alertes actives, SLO inchangé ou respecté | Alertes manquantes, SLO dégradé | Config alertes, dashboard SLO |

## 2) Critères pass/fail (règles générales)

- **Pass** : tous les items du lot sont au vert ou disposent d’une dérogation formelle validée par QA/Tech Lead.
- **Fail** : un item critique en échec ou une absence de preuve sur un item critique.
- **Dérogation** : documentée, datée, avec plan de remédiation et date cible.

## 3) Intégration aux rituels de release

- **Avant UAT** :
  - Pré-remplir la matrice du lot (items + critères + preuves attendues).
  - Valider la disponibilité des environnements et données de test.diff --git a/README.md b/README.md
index 8b137891791fe96927ad78e64b0aad7bded08bdc..810540035d2e024b938a33ed3a8911311ce40b38 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,54 @@
+# Cadre d’évaluation Impact / Effort
 
+## 1) Grille d’impact (1–5)
+Échelle proposée (1 = très faible, 5 = très élevé) :
+
+- **Revenus** : contribution directe aux revenus.
+- **Conversion** : impact sur le taux de conversion.
+- **Rétention** : capacité à faire revenir les utilisateurs.
+- **Différenciation** : avantage compétitif perçu.
+- **Réduction du churn** : diminution des résiliations / désabonnements.
+
+## 2) Grille d’effort (1–5)
+Échelle proposée (1 = faible effort, 5 = effort très élevé) :
+
+- **Complexité technique** : difficulté de conception / implémentation.
+- **Dépendances** : nombre et criticité des dépendances internes/externes.
+- **Charge Front / Back / Data** : volume de travail par domaine.
+- **Risques** : risques techniques, produit, sécurité ou conformité.
+
+## 3) Alignement des grilles (30–45 min)
+Plan d’atelier pour calibrer les scores :
+
+1. Présenter les définitions des critères (impact + effort).
+2. Valider ensemble les exemples de notes 1–5.
+3. Ajuster les grilles si un critère est redondant ou incomplet.
+4. Conclure par une grille finalisée et partagée.
+
+## 4) Scoring des fonctionnalités
+Pour chaque fonctionnalité :
+
+- Attribuer un score **Impact** (1–5) et **Effort** (1–5).
+- **Justification courte (1–2 phrases)** par score, factuelle et actionnable.
+
+Exemple de justification :
+
+- *Impact 4* : « Augmente la conversion sur le tunnel principal selon les tests A/B. »
+- *Effort 2* : « Réutilise les composants existants, peu de dépendances. »
+
+## 5) Synthèse en matrice 2x2
+Positionner chaque fonctionnalité dans la matrice :
+
+- **Quick Wins** (Impact élevé / Effort faible)
+- **Big Bets** (Impact élevé / Effort élevé)
+- **Fill-ins** (Impact faible / Effort faible)
+- **Money Pit** (Impact faible / Effort élevé)
+
+Conserver **le détail des scores** dans un tableau récapitulatif.
+
+### Exemple de tableau de scoring
+
+| Fonctionnalité | Impact (1–5) | Effort (1–5) | Justification | Catégorie |
+|---|---:|---:|---|---|
+| Recherche avancée | 4 | 3 | Améliore la conversion sur le segment power users. | Big Bet |
+| Export CSV | 2 | 1 | Demande récurrente, faible effort. | Fill-in |
diff --git a/README.md b/README.md
index 8b137891791fe96927ad78e64b0aad7bded08bdc..362d70e2943d58ea8fe33e3d746ecbaba083483d 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,53 @@
+# Cadre QA/UAT
 
+## 1. Phases QA (interne) vs UAT (client/utilisateur)
+
+| Aspect | QA (interne) | UAT (client/utilisateur) |
+| --- | --- | --- |
+| Objectif | Vérifier la qualité technique et fonctionnelle avant exposition client. | Valider que le produit répond aux besoins métier et aux scénarios réels. |
+| Responsables | Équipe QA + Tech Lead. | Product Owner + représentants utilisateurs. |
+| Environnement | Intégration/staging contrôlé. | Staging proche production, avec données/flux représentatifs. |
+| Critères d’entrée | Build stable, tests critiques passés, environnement prêt. | Fonctionnalités clés figées, bugs critiques QA résolus. |
+| Critères de sortie | Zéro bug bloquant/critique, risques documentés. | Acceptation formelle, dérogations signées si nécessaire. |
+
+## 2. Couverture minimale
+
+### QA (interne)
+- **Tests critiques** : authentification, parcours principal, paiements/transactions si applicable, gestion des droits.
+- **Smoke tests** : démarrage application, pages clés, API essentielles, intégration systèmes tiers.
+- **Non-régression** : scénarios des bugs majeurs corrigés, modules à fort risque.
+
+### UAT
+- **Parcours métier prioritaires** : scénarios définis par le PO et les utilisateurs clés.
+- **Validation UX/ergonomie** : cohérence des libellés, navigation, clarté des messages.
+- **Conformité** : règles métiers, exigences légales ou contractuelles.
+
+## 3. Outils recommandés
+
+- **Automatisation** : Playwright/Cypress pour UI, Postman/Newman pour API.
+- **Tracking** : Jira/Linear/YouTrack avec workflow dédié QA/UAT.
+- **Reporting** : tableaux de bord (Jira, Allure, ou rapports CI/CD) + synthèse hebdomadaire.
+
+## 4. Responsable validation (RACI)
+
+- **QA Lead** : Responsable (R) de l’exécution QA, qualité des tests, consolidation des résultats.
+- **Tech Lead** : Consulté (C) sur la faisabilité technique, impact correctifs, risques.
+- **Product Owner** : Compte (A) en UAT, donne l’acceptation finale.
+- **Équipe projet** : Informée (I) de l’état et des décisions.
+
+## 5. Délais de correction et critères de sortie
+
+### Délais de correction (SLA)
+- **Bloquant/Critique** : 24–48h.
+- **Majeur** : 3–5 jours ouvrés.
+- **Mineur** : cycle suivant ou planifié.
+
+### Critères de sortie QA
+- 0 bug bloquant/critique ouvert.
+- Taux de réussite des tests critiques ≥ 95%.
+- Rapport QA validé par QA Lead.
+
+### Critères de sortie UAT
+- Acceptation formelle par le Product Owner.
+- Liste de dérogations documentée et signée.
+- Plan de mise en production validé.
diff --git a/README.md b/README.md
index 8b137891791fe96927ad78e64b0aad7bded08bdc..60d4389e57bf886237015487b4803ad8e5cdfaa1 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,62 @@
+# Checklist de release - matrice par lot
+
+Ce document définit une matrice de contrôle par lot de release, les critères de pass/fail, l’intégration aux rituels, les preuves attendues et le processus de validation.
+
+## 1) Matrice par lot (fonctionnalités, performance, sécurité, compatibilité, observabilité)
+
+**Définition d’un lot** : un ensemble cohérent de changements livré ensemble (ex. sprint, hotfix, release majeure).
+
+| Lot | Catégorie | Item | Critère Pass | Critère Fail | Preuves attendues |
+| --- | --- | --- | --- | --- | --- |
+| L-XXX | Fonctionnalités | Couverture des stories et AC | 100% des user stories du lot validées, AC passés | Au moins un AC critique en échec ou non testé | Captures UAT, rapports d’exécution, liens tickets |
+| L-XXX | Fonctionnalités | Non-régression clé | Scénarios critiques passés sur env cible | Régression sur un flux critique | Logs de tests, vidéos, captures |
+| L-XXX | Performance | Temps de réponse P95 | P95 <= seuil défini pour les endpoints critiques | P95 > seuil ou variance > seuil d’alerte | Rapport APM, exports dashboard |
+| L-XXX | Performance | Charge nominale | Stable au volume cible (CPU/RAM/latence) | Dégradation significative ou erreurs > seuil | Rapport de charge, graphiques |
+| L-XXX | Sécurité | Vulnérabilités critiques | 0 vulnérabilité critique/haute ouverte | Vulnérabilité critique/haute non mitigée | Rapport SAST/DAST, ticket d’acceptation du risque |
+| L-XXX | Sécurité | Secrets et accès | Aucun secret exposé, accès validés | Secrets détectés, accès non revus | Rapport scan secrets, revue IAM |
+| L-XXX | Compatibilité | Navigateurs/clients cibles | OK sur la matrice supportée | Échec sur un client supporté | Captures par device, rapports tests |
+| L-XXX | Compatibilité | Migration/DB | Migrations appliquées sans erreur | Échec de migration ou rollback impossible | Logs migration, plan rollback |
+| L-XXX | Observabilité | Logs et traces | Logs structurés + traces pour parcours clés | Logs absents, incomplets ou non corrélés | Extraits logs, traces APM |
+| L-XXX | Observabilité | Alertes et SLO | Alertes actives, SLO inchangé ou respecté | Alertes manquantes, SLO dégradé | Config alertes, dashboard SLO |
+
+## 2) Critères pass/fail (règles générales)
+
+- **Pass** : tous les items du lot sont au vert ou disposent d’une dérogation formelle validée par QA/Tech Lead.
+- **Fail** : un item critique en échec ou une absence de preuve sur un item critique.
+- **Dérogation** : documentée, datée, avec plan de remédiation et date cible.
+
+## 3) Intégration aux rituels de release
+
+- **Avant UAT** :
+  - Pré-remplir la matrice du lot (items + critères + preuves attendues).
+  - Valider la disponibilité des environnements et données de test.
+- **Avant Go/No-Go** :
+  - Revue complète de la matrice par QA + Tech Lead.
+  - Vérification des preuves (captures, logs, rapports).
+  - Décision Go/No-Go consignée avec le statut final du lot.
+
+## 4) Section “preuves” (captures, logs, rapports)
+
+Pour chaque item, joindre au minimum :
+
+- **Captures** (UI, résultats UAT) : images datées.
+- **Logs** (extraits pertinents) : avec time range, corrélation et requêtes associées.
+- **Rapports** (tests, perf, sécurité) : PDF/HTML ou lien vers l’outil source.
+
+## 5) Validation & publication
+
+- **Validation requise** : QA Lead + Tech Lead.
+- **Publication** :
+  - Mettre la matrice à jour dans ce document.
+  - Partager le lien dans le canal release et l’ajouter au référentiel qualité interne.
+
+---
+
+## Modèle de lot (copier-coller)
+
+- Lot : `L-XXX`
+- Période : `YYYY-MM-DD → YYYY-MM-DD`
+- Responsable : `Nom`
+- Statut : `En préparation / En revue / Go / No-Go`
+- Dérogations : `Aucune` / `Liste`
diff --git a/README.md b/README.md
index bfa6edd93f1f0f0707d9f325454a1646778431f1..f9eaee2a6d8c6d1dd1549aab32e04a21e1eb06eb 100644
--- a/README.md
+++ b/README.md
@@ -89,25 +89,64 @@ Pour chaque item, joindre au minimum :
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
+
+---
+
+## Fusionner plusieurs branches en une seule fois
+
+Ce guide décrit comment regrouper plusieurs branches dans une branche cible (ex. `work`) en une seule opération.
+
+### 1) Préparer les branches
+- Mettre à jour les références :
+  - `git fetch --all`
+- Vérifier les branches disponibles :
+  - `git branch -a`
+
+### 2) Se placer sur la branche cible
+- `git switch work`
+- S’assurer que la branche cible est propre :
+  - `git status -sb`
+
+### 3) Fusionner plusieurs branches en une seule commande (merge "octopus")
+Pour fusionner plusieurs branches sans conflits majeurs :
+
+```
+git merge feature/a feature/b feature/c
+```
+
+> Si Git détecte des conflits, il arrête la fusion. Résolvez les conflits, ajoutez les fichiers puis terminez avec `git commit`.
+
+### 4) Fusionner en chaîne (si l’octopus échoue)
+Si l’octopus ne passe pas, fusionnez séquentiellement :
+
+```
+git merge feature/a
+git merge feature/b
+git merge feature/c
+```
+
+### 5) Vérifier et pousser
+- `git log --oneline --decorate -n 5`
+- `git push origin work`


- **Avant Go/No-Go** :
  - Revue complète de la matrice par QA + Tech Lead.
  - Vérification des preuves (captures, logs, rapports).
  - Décision Go/No-Go consignée avec le statut final du lot.

## 4) Section “preuves” (captures, logs, rapports)

Pour chaque item, joindre au minimum :

- **Captures** (UI, résultats UAT) : images datées.
- **Logs** (extraits pertinents) : avec time range, corrélation et requêtes associées.
- **Rapports** (tests, perf, sécurité) : PDF/HTML ou lien vers l’outil source.

## 5) Validation & publication

- **Validation requise** : QA Lead + Tech Lead.
- **Publication** :
  - Mettre la matrice à jour dans ce document.
  - Partager le lien dans le canal release et l’ajouter au référentiel qualité interne.

---

## Modèle de lot (copier-coller)

- Lot : `L-XXX`
- Période : `YYYY-MM-DD → YYYY-MM-DD`
- Responsable : `Nom`
- Statut : `En préparation / En revue / Go / No-Go`
- Dérogations : `Aucune` / `Liste`

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
