# Plateforme Skillforge

Documentation essentielle :

- [Installation](INSTALLATION.md)
- [Architecture & flux réseau](docs/architecture.md)
- [Dossier d'exploitation](docs/exploitation.md)

## Points de cadrage à valider

1. Définir le budget maximal (capex/opex) et le délai cible de livraison.
2. Fixer le niveau de qualité attendu (ex. performance minimale, stabilité).
3. Délimiter le périmètre technique (ex. intégrations externes minimales).
4. Valider les contraintes avec les sponsors.

## Plan de priorisation des objectifs produit

### Étapes proposées

1. Organiser un atelier rapide (60–90 min) avec les décideurs pour classer acquisition/activation/rétention par impact.
2. Définir pour chaque objectif un KPI principal (ex. taux d’inscription, taux d’activation J+7, rétention M+1).
3. Fixer des cibles réalistes (baseline + objectif) et l’horizon temporel.
4. Formaliser la priorisation dans un tableau (Objectif ➜ KPI ➜ Cible ➜ Horizon).

### Tableau de priorisation (à compléter)

| Objectif | KPI principal | Cible (baseline ➜ objectif) | Horizon |
| --- | --- | --- | --- |
| Acquisition | Taux d’inscription |  |  |
| Activation | Taux d’activation J+7 |  |  |
| Rétention | Rétention M+1 |  |  |

## MVP — Plateforme SkillForge

### Objectifs business prioritaires
1. **Acquisition** : augmenter le nombre d’inscriptions qualifiées.
2. **Activation** : amener les apprenants à démarrer un premier module dans les 7 jours.
3. **Rétention** : améliorer le taux de complétion des parcours.

### Parcours utilisateurs critiques
- **Inscription** : création de compte et validation email.
- **Accès à un parcours** : découverte du catalogue puis inscription à un parcours.
- **Progression** : démarrage, suivi, reprise et complétion des modules.
- **Certification** : génération d’un certificat unique après complétion.
- **Vue manager** : consultation d’un coût budgétaire en fonction du délai de formation.

### Parcours de formation par poste
- **Ingénieurs** : parcours orientés technique (fondamentaux, spécialisation, validation).
- **Concepteurs** : parcours orientés design/méthode (recherche, prototypage, validation).

### Fonctionnalités minimales nécessaires (MVP)
- Authentification (inscription/connexion, récupération de mot de passe).
- Catalogue de parcours + recherche simple.
- Module de formation (lecture de contenus, progression par étape).
- Suivi de progression (pour l’apprenant et pour les managers).
- Délivrance d’un **certificat unique** après complétion.
- **Vue manager** : coût budgétaire estimé en fonction du délai de formation.

### Contraintes MVP
- **Budget** : cadré pour livrer un MVP en 8–12 semaines.
- **Délais** : première version utilisable par un groupe pilote.
- **Qualité** : stabilité fonctionnelle et suivi de progression fiable.
- **Périmètre technique** : intégrations minimales (ex. SSO et reporting avancé reportés).

### Validation et document MVP (1–2 pages)
- Synthèse des objectifs, parcours, fonctionnalités et contraintes.
- Validation formelle avec les parties prenantes.

## Matrice de priorisation

### Matrice (1–5)

| Domaine | Dépendances | Valeur | Risque | Justification courte |
| --- | --- | --- | --- | --- |
| Auth | 5 | 5 | 4 | Prérequis technique et sécurité pour tous les autres domaines. |
| Parcours | 4 | 4 | 3 | S’appuie sur l’auth; structure l’expérience utilisateur. |
| Questionnaires | 3 | 4 | 3 | Dépend des parcours pour l’enchaînement pédagogique. |
| Certificats | 2 | 3 | 2 | Dépend des questionnaires pour les résultats. |

### Validation de l’ordre

L’ordre **auth → parcours → questionnaires → certificats** est respecté, car chaque domaine dépend logiquement du précédent :

1. **Auth** : base d’accès, sécurité, et identification des utilisateurs.
2. **Parcours** : nécessite l’authentification pour attribuer et suivre un parcours.
3. **Questionnaires** : rattachés aux parcours et à la progression des utilisateurs.
4. **Certificats** : reposent sur les résultats des questionnaires.

### Décision et hypothèses

**Décision**
- Prioriser le travail selon l’ordre validé pour réduire les blocages et maximiser la valeur livrée tôt.

**Hypothèses**
- L’authentification est indispensable avant toute fonctionnalité métier.
- Les parcours définissent la structure qui conditionne les questionnaires.
- Les certificats ne peuvent être délivrés qu’après l’évaluation via questionnaires.
- Les risques sont principalement liés à la sécurité (auth) et à l’intégration des flux (parcours ↔ questionnaires).

## Cadre d’évaluation Impact / Effort

### 1) Grille d’impact (1–5)
Échelle proposée (1 = très faible, 5 = très élevé) :

- **Revenus** : contribution directe aux revenus.
- **Conversion** : impact sur le taux de conversion.
- **Rétention** : capacité à faire revenir les utilisateurs.
- **Différenciation** : avantage compétitif perçu.
- **Réduction du churn** : diminution des résiliations / désabonnements.

### 2) Grille d’effort (1–5)
Échelle proposée (1 = faible effort, 5 = effort très élevé) :

- **Complexité technique** : difficulté de conception / implémentation.
- **Dépendances** : nombre et criticité des dépendances internes/externes.
- **Charge Front / Back / Data** : volume de travail par domaine.
- **Risques** : risques techniques, produit, sécurité ou conformité.

### 3) Alignement des grilles (30–45 min)
Plan d’atelier pour calibrer les scores :

1. Présenter les définitions des critères (impact + effort).
2. Valider ensemble les exemples de notes 1–5.
3. Ajuster les grilles si un critère est redondant ou incomplet.
4. Conclure par une grille finalisée et partagée.

### 4) Scoring des fonctionnalités
Pour chaque fonctionnalité :

- Attribuer un score **Impact** (1–5) et **Effort** (1–5).
- **Justification courte (1–2 phrases)** par score, factuelle et actionnable.

Exemple de justification :

- *Impact 4* : « Augmente la conversion sur le tunnel principal selon les tests A/B. »
- *Effort 2* : « Réutilise les composants existants, peu de dépendances. »

### 5) Synthèse en matrice 2x2
Positionner chaque fonctionnalité dans la matrice :

- **Quick Wins** (Impact élevé / Effort faible)
- **Big Bets** (Impact élevé / Effort élevé)
- **Fill-ins** (Impact faible / Effort faible)
- **Money Pit** (Impact faible / Effort élevé)

Conserver **le détail des scores** dans un tableau récapitulatif.

#### Exemple de tableau de scoring

| Fonctionnalité | Impact (1–5) | Effort (1–5) | Justification | Catégorie |
|---|---:|---:|---|---|
| Recherche avancée | 4 | 3 | Améliore la conversion sur le segment power users. | Big Bet |
| Export CSV | 2 | 1 | Demande récurrente, faible effort. | Fill-in |

## Cadre QA/UAT

### 1. Phases QA (interne) vs UAT (client/utilisateur)

| Aspect | QA (interne) | UAT (client/utilisateur) |
| --- | --- | --- |
| Objectif | Vérifier la qualité technique et fonctionnelle avant exposition client. | Valider que le produit répond aux besoins métier et aux scénarios réels. |
| Responsables | Équipe QA + Tech Lead. | Product Owner + représentants utilisateurs. |
| Environnement | Intégration/staging contrôlé. | Staging proche production, avec données/flux représentatifs. |
| Critères d’entrée | Build stable, tests critiques passés, environnement prêt. | Fonctionnalités clés figées, bugs critiques QA résolus. |
| Livrables | Rapport QA, statut de couverture, risques et dérogations. | Rapport UAT, retours métiers, décision Go/No-Go. |
| Critères de sortie | Zéro bug bloquant/critique, risques documentés. | Acceptation formelle, dérogations signées si nécessaire. |

### 2. Couverture minimale

#### QA (interne)
- **Tests critiques** : authentification, parcours principal, paiements/transactions si applicable, gestion des droits.
- **Smoke tests** : démarrage application, pages clés, API essentielles, intégration systèmes tiers.
- **Non-régression** : scénarios des bugs majeurs corrigés, modules à fort risque.
- **Qualité technique** : erreurs console/serveur, logs, stabilité des intégrations.

#### UAT
- **Parcours métier prioritaires** : scénarios définis par le PO et les utilisateurs clés.
- **Validation UX/ergonomie** : cohérence des libellés, navigation, clarté des messages.
- **Conformité** : règles métiers, exigences légales ou contractuelles.
- **Acceptance métier** : critères d’acceptation des user stories et résultats attendus.

### 3. Outils recommandés

- **Automatisation** : Playwright/Cypress pour UI, Postman/Newman pour API, tests CI/CD.
- **Tracking** : Jira/Linear/YouTrack avec workflow dédié QA/UAT (statuts, priorités, SLA).
- **Reporting** : tableaux de bord (Jira, Allure, ou rapports CI/CD) + synthèse hebdomadaire.
- **Feedback UAT** : formulaires structurés, captures d’écran/vidéos, compte-rendu de session.

### 4. Responsable validation (RACI)

- **QA Lead** : Responsable (R) de l’exécution QA, qualité des tests, consolidation des résultats.
- **Tech Lead** : Consulté (C) sur la faisabilité technique, impact correctifs, risques.
- **Product Owner** : Compte (A) en UAT, donne l’acceptation finale.
- **Équipe projet** : Informée (I) de l’état et des décisions.
- **Responsable validation** : QA Lead en QA, Product Owner en UAT.

### 5. Délais de correction et critères de sortie

#### Délais de correction (SLA)
- **Bloquant/Critique** : 24–48h.
- **Majeur** : 3–5 jours ouvrés.
- **Mineur** : cycle suivant ou planifié.

#### Critères de sortie QA
- 0 bug bloquant/critique ouvert.
- Taux de réussite des tests critiques ≥ 95%.
- Rapport QA validé par QA Lead.

#### Critères de sortie UAT
- Acceptation formelle par le Product Owner.
- Liste de dérogations documentée et signée.
- Plan de mise en production validé.

## Checklist de release - matrice par lot

Ce document définit une matrice de contrôle par lot de release, les critères de pass/fail, l’intégration aux rituels, les preuves attendues et le processus de validation.

### 1) Matrice par lot (fonctionnalités, performance, sécurité, compatibilité, observabilité)

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

### 2) Critères pass/fail (règles générales)

- **Pass** : tous les items du lot sont au vert ou disposent d’une dérogation formelle validée par QA/Tech Lead.
- **Fail** : un item critique en échec ou une absence de preuve sur un item critique.
- **Dérogation** : documentée, datée, avec plan de remédiation et date cible.

### 3) Intégration aux rituels de release

- **Avant UAT** :
  - Pré-remplir la matrice du lot (items + critères + preuves attendues).
  - Valider la disponibilité des environnements et données de test.
- **Avant Go/No-Go** :
  - Revue complète de la matrice par QA + Tech Lead.
  - Vérification des preuves (captures, logs, rapports).
  - Validation formelle consignée (QA/Tech Lead).
  - Décision Go/No-Go consignée avec le statut final du lot.

### 4) Section “preuves” (captures, logs, rapports)

Pour chaque item, joindre au minimum :

- **Captures** (UI, résultats UAT) : images datées.
- **Logs** (extraits pertinents) : avec time range, corrélation et requêtes associées.
- **Rapports** (tests, perf, sécurité) : PDF/HTML ou lien vers l’outil source.

### 5) Validation & publication

- **Validation requise** : QA Lead + Tech Lead.
- **Publication** :
  - Mettre la matrice à jour dans ce document.
  - Partager le lien dans le canal release, consigner l’approbation QA/Tech Lead, et l’ajouter au référentiel qualité interne.

---

### Modèle de lot (copier-coller)

- Lot : `L-XXX`
- Période : `YYYY-MM-DD → YYYY-MM-DD`
- Responsable : `Nom`
- Statut : `En préparation / En revue / Go / No-Go`
- Dérogations : `Aucune` / `Liste`

## Modèle d'identité et d'accès

### 1. Modèle d'identité

- **Email + mot de passe** : mode principal pour les utilisateurs internes (formateurs, admins).
- **SSO (SAML/OIDC)** : option pour les organisations partenaires.
- **OAuth2/OIDC** : connexion externe (Google/Microsoft) pour les apprenants.

### 2. Rôles et permissions

- **Admin** : gestion des utilisateurs, des rôles, des contenus, et des paramètres sécurité.
- **Formateur** : création/édition de contenus, gestion des cohorts, suivi des apprenants.
- **Apprenant** : consultation des contenus, participation aux évaluations, accès à son profil.
- **Invité** (optionnel) : accès en lecture limitée aux contenus publics.

### 3. Stratégie d'authentification

- **JWT** : access token court (15 min) + refresh token (rotation).
- **Cookies sécurisés** : HttpOnly + SameSite=Lax/Strict pour les sessions web.
- **TLS obligatoire** : chiffrement en transit.

### 4. Gestion des accès aux contenus

- **RBAC** : règles par rôle (admin/formateur/apprenant).
- **ABAC** : conditions contextuelles (cohort, statut d'inscription, progression).

### 5. Principe d'accès interne

- **Moindre privilège** : accès limité au strict nécessaire selon le rôle.
- **Séparation des environnements** : accès production réservé aux besoins opérationnels.
- **Traçabilité** : journalisation des actions sensibles (contenus, rôles, permissions).
- **Revue périodique** : audits réguliers des droits et des comptes inactifs.

### 6. Sécurité avancée

- **MFA** : requis pour admins, optionnel pour formateurs, recommandé pour tous.
- **Politiques de mot de passe** :
  - 12 caractères minimum
  - complexité (majuscule, minuscule, chiffre, symbole)
  - vérification contre listes de mots de passe compromis
  - expiration optionnelle selon politique d'organisation

### 7. Interface de suivi des comptes

- **Tableau de bord** : vue synthétique des comptes et de leurs accès.
- **Compteur d'utilisateurs actifs** : indicateur en temps réel des sessions en cours.
- **Suivi des placements** : états des comptes en cours d'affectation/placement.
- **Comptes révoqués** : liste dédiée avec motifs, date de révocation et actions possibles.

## Plateforme SkillForge — Spécification fonctionnelle (extrait)

### Rôles et permissions clés

#### Apprenant
- Consulter le catalogue et s’inscrire aux parcours disponibles.
- Accéder aux contenus autorisés par son inscription et son état de progression.
- Suivre sa progression, passer des quiz, consulter ses résultats.
- Disposer d’une fiche profil consultable par le manager et le chargé de formation pour identifier les points forts et les points d’amélioration.
- Télécharger les ressources autorisées (ex. PDF/Word) selon les règles d’accès.
- Demander/obtenir une certification lorsque les conditions sont remplies.

#### Formateur
- Créer, organiser et mettre à jour les parcours, modules, contenus et évaluations.
- Publier et gérer les sessions (ou cohortes) avec dates et capacités.
- Suivre la progression des apprenants, corriger/valider les évaluations.
- Attribuer des scores et statuer sur la complétion/certification.

#### Administrateur
- Gérer les utilisateurs, rôles, permissions et accès globaux.
- Définir les politiques de contenu, de sécurité et de conformité.
- Superviser les parcours, contenus, certifications et rapports globaux.
- Paramétrer les intégrations et gérer les incidents/abus.

### Parcours de formation

#### 1) Inscription
- L’apprenant choisit un parcours depuis le catalogue.
- Validation des prérequis (si applicables) et confirmation d’inscription.
- Attribution de l’accès au contenu selon la politique (immédiat ou programmé).

#### 2) Progression
- Le parcours est structuré en modules/chapitres.
- Il comprend un tronc commun et des branches de formation spécifiques selon le profil.
- La progression est suivie par étape (statut : non commencé, en cours, terminé).
- Les activités obligatoires doivent être complétées pour avancer.

#### 3) Évaluations
- Types : quiz, examens, projets.
- Les évaluations peuvent être auto-corrigées ou corrigées par le formateur.
- Les scores sont enregistrés et pris en compte pour la certification.

#### 4) Certification
- Délivrance automatique ou manuelle selon les règles définies.
- Génération d’un certificat téléchargeable si les conditions sont remplies.

### Types de contenus et règles d’accès

#### PDF
- Téléchargement autorisé après inscription.
- Accès possible hors ligne selon la politique du parcours.

#### Word (DOC/DOCX)
- Téléchargement autorisé pour les supports de travail.
- Peut être limité aux apprenants inscrits et actifs.

#### Vidéo
- Accès en streaming.
- Disponibilité conditionnée par la progression (ex. déverrouillage séquentiel).
- Restriction d’accès en cas d’expiration d’inscription ou de non-respect des prérequis.

### Conditions d’obtention de la formation

- Complétion de 100 % des modules obligatoires.
- Score minimal global (ex. ≥ 70 %) et/ou score minimal par évaluation clé.
- Soumission de toutes les évaluations requises.
- Validation finale par le formateur (si applicable).
- Respect des délais de parcours (si définis).

## Fusionner plusieurs branches en une seule fois

Ce guide décrit comment regrouper plusieurs branches dans une branche cible (ex. `work`) en une seule opération.

### 1) Préparer les branches
- Mettre à jour les références :
  - `git fetch --all`
- Vérifier les branches disponibles :
  - `git branch -a`

### 2) Se placer sur la branche cible
- `git switch work`
- S’assurer que la branche cible est propre :
  - `git status -sb`

### 3) Fusionner plusieurs branches en une seule commande (merge "octopus")
Pour fusionner plusieurs branches sans conflits majeurs :

```
git merge feature/a feature/b feature/c
```

> Si Git détecte des conflits, il arrête la fusion. Résolvez les conflits, ajoutez les fichiers puis terminez avec `git commit`.

### 4) Fusionner en chaîne (si l’octopus échoue)
Si l’octopus ne passe pas, fusionnez séquentiellement :

```
git merge feature/a
git merge feature/b
git merge feature/c
```

### 5) Vérifier et pousser
- `git log --oneline --decorate -n 5`
- `git push origin work`
