# Plateforme SkillForge — Spécification fonctionnelle (extrait)

## Rôles et permissions clés

### Apprenant
- Consulter le catalogue et s’inscrire aux parcours disponibles.
- Accéder aux contenus autorisés par son inscription et son état de progression.
- Suivre sa progression, passer des quiz, consulter ses résultats.
- Disposer d’une fiche profil consultable par le manager et le chargé de formation pour identifier les points forts et les points d’amélioration.
- Télécharger les ressources autorisées (ex. PDF/Word) selon les règles d’accès.
- Demander/obtenir une certification lorsque les conditions sont remplies.

### Formateur
- Créer, organiser et mettre à jour les parcours, modules, contenus et évaluations.
- Publier et gérer les sessions (ou cohortes) avec dates et capacités.
- Suivre la progression des apprenants, corriger/valider les évaluations.
- Attribuer des scores et statuer sur la complétion/certification.

### Administrateur
- Gérer les utilisateurs, rôles, permissions et accès globaux.
- Définir les politiques de contenu, de sécurité et de conformité.
- Superviser les parcours, contenus, certifications et rapports globaux.
- Paramétrer les intégrations et gérer les incidents/abus.

## Parcours de formation

### 1) Inscription
- L’apprenant choisit un parcours depuis le catalogue.
- Validation des prérequis (si applicables) et confirmation d’inscription.
- Attribution de l’accès au contenu selon la politique (immédiat ou programmé).

### 2) Progression
- Le parcours est structuré en modules/chapitres.
- Il comprend un tronc commun et des branches de formation spécifiques selon le profil.
- La progression est suivie par étape (statut : non commencé, en cours, terminé).
- Les activités obligatoires doivent être complétées pour avancer.

### 3) Évaluations
- Types : quiz, examens, projets.
- Les évaluations peuvent être auto-corrigées ou corrigées par le formateur.
- Les scores sont enregistrés et pris en compte pour la certification.

### 4) Certification
- Délivrance automatique ou manuelle selon les règles définies.
- Génération d’un certificat téléchargeable si les conditions sont remplies.

## Types de contenus et règles d’accès

### PDF
- Téléchargement autorisé après inscription.
- Accès possible hors ligne selon la politique du parcours.

### Word (DOC/DOCX)
- Téléchargement autorisé pour les supports de travail.
- Peut être limité aux apprenants inscrits et actifs.

### Vidéo
- Accès en streaming.
- Disponibilité conditionnée par la progression (ex. déverrouillage séquentiel).
- Restriction d’accès en cas d’expiration d’inscription ou de non-respect des prérequis.

## Conditions d’obtention de la formation

- Complétion de 100 % des modules obligatoires.
- Score minimal global (ex. ≥ 70 %) et/ou score minimal par évaluation clé.
- Soumission de toutes les évaluations requises.
- Validation finale par le formateur (si applicable).
- Respect des délais de parcours (si définis).
