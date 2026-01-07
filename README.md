# Plateforme Skillforge — Spécifications de diffusion de contenus

## 1. Types de contenu supportés
- **PDF** : documents de cours et supports téléchargeables ou consultables en ligne.
- **Vidéo** : modules vidéo pédagogiques (chapitres, sessions live enregistrées).
- **Audio** : podcasts, capsules audio et versions audio des cours.
- **SCORM** : paquets SCORM 1.2/2004 pour le suivi e‑learning.

## 2. Modes d’accès
- **Streaming adaptatif** :
  - **HLS** (HTTP Live Streaming) pour la compatibilité large (web et mobile).
  - **DASH** (Dynamic Adaptive Streaming over HTTP) pour les lecteurs compatibles.
- **Téléchargement sécurisé** :
  - Téléchargement chiffré ou signé, limité dans le temps.
  - Accès restreint aux utilisateurs autorisés et appareils connus.

## 3. Liens signés et durée de validité
- **Génération de liens signés** côté backend (API) pour tous les assets protégés.
- **Durée de validité configurable** (ex. 5 à 60 minutes pour streaming, 24 h pour téléchargement), selon le niveau de sensibilité.
- **Paramètres inclus** : identifiant de l’utilisateur, horodatage d’expiration, signature HMAC.
- **Rotation de clé** possible sans interrompre le service (grâce à une fenêtre de chevauchement).

## 4. Contrôle des droits d’accès (API + lecteur)
- **Côté API** :
  - Vérification d’authentification (JWT/OAuth) et des droits d’accès (rôle, abonnement, statut du cours).
  - Autorisation fine par contenu (chapitre/module).
  - Audit/logging des accès (utilisateur, contenu, IP, device).
- **Côté lecteur** :
  - Validation du jeton d’accès avant lecture.
  - Revalidation périodique pour sessions longues.
  - Blocage si expiration ou révocation (token invalidé).

## 5. Cache/CDN et gestion des quotas
- **CDN** en frontal pour les assets lourds (vidéo, audio, PDF).
- **Cache HTTP** configuré par type de contenu :
  - Streaming : segments courts avec TTL réduit.
  - Téléchargements : TTL plus long mais liés à la validité du lien signé.
- **Quota par utilisateur** :
  - Limitation du nombre de téléchargements.
  - Restriction du nombre de devices actifs simultanés.
- **Monitoring** :
  - Alertes sur consommation de bande passante.
  - Analyse des pics pour ajuster les limites.

