# Backlog V1 — Priorisation et cadrage

## Ordonnancement V1 immédiat (valeur business + dépendances critiques)
1. **Authentification & gestion des comptes** — Pré-requis de sécurité et d’accès pour tous les autres items.
2. **Catalogue des compétences & parcours** — Cœur de la proposition de valeur (contenu disponible).
3. **Évaluation/quiz & certification** — Mesure de valeur perçue et preuve d’acquisition.
4. **Tableau de bord apprenant** — Suivi et rétention, dépend des contenus et évaluations.
5. **Analytics admin/manager** — Pilotage business, dépend des données d’usage.

## Fiches backlog

### 1) Authentification & gestion des comptes
- **Objectif** : Permettre l’accès sécurisé et la gestion des profils utilisateurs.
- **User story** : En tant qu’apprenant, je veux créer un compte et me connecter pour accéder aux parcours.
- **Métriques de succès** :
  - Taux d’inscription terminé > 70 %
  - Temps moyen d’inscription < 2 min
  - < 2 % d’erreurs d’authentification
- **Dépendances** : Aucune (item racine).
- **Critères d’acceptation** :
  - **Given** un visiteur sur la page d’inscription, **When** il soumet un formulaire valide, **Then** son compte est créé et il est connecté.
  - **Given** un utilisateur enregistré, **When** il saisit un mot de passe incorrect, **Then** un message d’erreur explicite s’affiche sans révéler d’information sensible.
  - **Checklist testable** : validation email, réinitialisation mot de passe, déconnexion.
- **Estimation** : M
- **Responsable** : Lead backend

### 2) Catalogue des compétences & parcours
- **Objectif** : Rendre consultables les compétences et parcours disponibles.
- **User story** : En tant qu’apprenant, je veux parcourir un catalogue de parcours pour choisir une formation pertinente.
- **Métriques de succès** :
  - > 50 % des visiteurs consultent un parcours
  - Taux de clic sur un parcours > 20 %
- **Dépendances** : Authentification & gestion des comptes (accès et personnalisation).
- **Critères d’acceptation** :
  - **Given** un utilisateur connecté, **When** il ouvre le catalogue, **Then** il voit la liste des parcours avec titre, niveau, durée.
  - **Given** un parcours, **When** l’utilisateur clique dessus, **Then** il accède à une page détail avec description et compétences associées.
  - **Checklist testable** : recherche par mot-clé, filtres niveau/durée, pagination.
- **Estimation** : L
- **Responsable** : Product designer

### 3) Évaluation/quiz & certification
- **Objectif** : Évaluer les acquis et délivrer une certification.
- **User story** : En tant qu’apprenant, je veux passer un quiz pour valider mes compétences.
- **Métriques de succès** :
  - Taux de complétion des quiz > 60 %
  - > 30 % des apprenants obtiennent une certification
- **Dépendances** : Catalogue des compétences & parcours.
- **Critères d’acceptation** :
  - **Given** un parcours, **When** l’apprenant termine le quiz, **Then** il reçoit un score et un résultat (réussi/échoué).
  - **Given** un score >= seuil, **When** le quiz est soumis, **Then** un badge ou certificat est généré.
  - **Checklist testable** : banque de questions, minuteur optionnel, reprise de session.
- **Estimation** : L
- **Responsable** : Lead product

### 4) Tableau de bord apprenant
- **Objectif** : Permettre le suivi de progression et encourager la rétention.
- **User story** : En tant qu’apprenant, je veux visualiser mon avancement pour rester motivé.
- **Métriques de succès** :
  - Taux de rétention à 7 jours > 25 %
  - Temps moyen passé par session > 5 min
- **Dépendances** : Catalogue des compétences & parcours, Évaluation/quiz & certification.
- **Critères d’acceptation** :
  - **Given** un apprenant connecté, **When** il ouvre le tableau de bord, **Then** il voit son avancement par parcours.
  - **Given** des évaluations passées, **When** le tableau de bord se charge, **Then** il affiche les scores et badges obtenus.
  - **Checklist testable** : progression en %, prochains modules, reprise rapide.
- **Estimation** : M
- **Responsable** : Frontend lead

### 5) Analytics admin/manager
- **Objectif** : Offrir une vue agrégée pour le pilotage.
- **User story** : En tant que manager, je veux suivre l’engagement et la performance des apprenants.
- **Métriques de succès** :
  - > 80 % des managers consultent le dashboard mensuellement
  - Export de données < 10 s
- **Dépendances** : Tableau de bord apprenant, Évaluation/quiz & certification.
- **Critères d’acceptation** :
  - **Given** un manager connecté, **When** il ouvre l’analytics, **Then** il voit les KPIs clés (inscriptions, complétion, scores).
  - **Given** une plage de dates, **When** il filtre, **Then** les graphiques se mettent à jour.
  - **Checklist testable** : export CSV, segmentation par parcours, permissions.
- **Estimation** : L
- **Responsable** : Data/BI lead

## Validation de cohérence globale
- **Capacité** : Items 1-2 en parallèle (auth + catalogue), puis 3-4, puis 5.
- **Chronologie** : Semaines 1-2 (auth), 2-4 (catalogue), 4-6 (quiz), 6-7 (dashboard), 7-8 (analytics).
- **Quick wins** : Authentification et catalogue en tête pour débloquer l’usage rapide.
