# Modèle d'identité et d'accès

## 1. Modèle d'identité

* **Email + mot de passe** : mode principal pour les utilisateurs internes (formateurs, admins).
* **SSO (SAML/OIDC)** : option pour les organisations partenaires.
* **OAuth2/OIDC** : connexion externe (Google/Microsoft) pour les apprenants.

## 2. Rôles et permissions

* **Admin** : gestion des utilisateurs, des rôles, des contenus, et des paramètres sécurité.
* **Formateur** : création/édition de contenus, gestion des cohorts, suivi des apprenants.
* **Apprenant** : consultation des contenus, participation aux évaluations, accès à son profil.
* **Invité** (optionnel) : accès en lecture limitée aux contenus publics.

## 3. Stratégie d'authentification

* **JWT** : access token court (15 min) + refresh token (rotation).
* **Cookies sécurisés** : HttpOnly + SameSite=Lax/Strict pour les sessions web.
* **TLS obligatoire** : chiffrement en transit.

## 4. Gestion des accès aux contenus

* **RBAC** : règles par rôle (admin/formateur/apprenant).
* **ABAC** : conditions contextuelles (cohort, statut d'inscription, progression).

## 5. Principe d'accès interne

* **Moindre privilège** : accès limité au strict nécessaire selon le rôle.
* **Séparation des environnements** : accès production réservé aux besoins opérationnels.
* **Traçabilité** : journalisation des actions sensibles (contenus, rôles, permissions).
* **Revue périodique** : audits réguliers des droits et des comptes inactifs.

## 6. Sécurité avancée

* **MFA** : requis pour admins, optionnel pour formateurs, recommandé pour tous.
* **Politiques de mot de passe** :
  * 12 caractères minimum
  * complexité (majuscule, minuscule, chiffre, symbole)
  * vérification contre listes de mots de passe compromis
  * expiration optionnelle selon politique d'organisation

## 7. Interface de suivi des comptes

* **Tableau de bord** : vue synthétique des comptes et de leurs accès.
* **Compteur d'utilisateurs actifs** : indicateur en temps réel des sessions en cours.
* **Suivi des placements** : états des comptes en cours d'affectation/placement.
* **Comptes révoqués** : liste dédiée avec motifs, date de révocation et actions possibles.
