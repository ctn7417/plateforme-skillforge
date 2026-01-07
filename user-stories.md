# Personas cibles

- **Apprenant** : utilise la plateforme pour découvrir des formations, s’inscrire, suivre des contenus et mesurer sa progression.
- **Formateur** : conçoit et publie des formations, suit l’engagement des apprenants et ajuste ses contenus.
- **Admin** : administre la plateforme, gère les utilisateurs, et assure la disponibilité des formations.

# Fonctionnalités MVP & user stories

## 1) Authentification et gestion de compte

- **Story** (Must) : *En tant qu’apprenant, je veux créer un compte avec email et mot de passe afin d’accéder aux formations et suivre ma progression.*
  - **Critères d’acceptation (Given/When/Then)**
    - **Given** je suis sur la page d’inscription, **When** je saisis un email valide, un mot de passe conforme et je confirme, **Then** un compte est créé et je suis connecté.
    - **Given** je saisis un email déjà utilisé, **When** je soumets le formulaire, **Then** un message d’erreur explicite est affiché et le compte n’est pas créé.
- **Story** (Must) : *En tant qu’apprenant, je veux me connecter avec mes identifiants afin d’accéder à mon tableau de bord.*
  - **Critères d’acceptation (Given/When/Then)**
    - **Given** j’ai un compte existant, **When** je saisis mes identifiants valides, **Then** je suis authentifié et redirigé vers mon tableau de bord.
    - **Given** je saisis un mot de passe invalide, **When** je tente de me connecter, **Then** un message d’erreur apparaît et je reste sur la page de connexion.

## 2) Catalogue de formations

- **Story** (Must) : *En tant qu’apprenant, je veux consulter un catalogue listant les formations disponibles afin de trouver une formation pertinente.*
  - **Critères d’acceptation (Given/When/Then)**
    - **Given** je suis sur la page catalogue, **When** la page se charge, **Then** je vois une liste paginée avec le titre, le niveau et la durée de chaque formation.
    - **Given** le catalogue contient plus de 20 formations, **When** je change de page, **Then** je vois la page suivante avec 20 éléments maximum.
- **Story** (Should) : *En tant qu’apprenant, je veux filtrer les formations par niveau afin d’identifier les formations adaptées à mon expertise.*
  - **Critères d’acceptation (Given/When/Then)**
    - **Given** je suis sur le catalogue, **When** je sélectionne le filtre “Débutant”, **Then** seules les formations de niveau débutant sont affichées.
    - **Given** aucun résultat ne correspond au filtre, **When** le filtrage est appliqué, **Then** un message “Aucune formation trouvée” est affiché.

## 3) Détail de formation

- **Story** (Must) : *En tant qu’apprenant, je veux voir la page de détail d’une formation afin de comprendre son contenu et ses prérequis.*
  - **Critères d’acceptation (Given/When/Then)**
    - **Given** je sélectionne une formation dans le catalogue, **When** j’ouvre sa fiche, **Then** je vois le titre, la description, les modules, la durée totale et les prérequis.
    - **Given** une formation ne comporte pas de prérequis, **When** j’ouvre la fiche, **Then** la section prérequis indique “Aucun”.

## 4) Inscription à une formation

- **Story** (Must) : *En tant qu’apprenant, je veux m’inscrire à une formation afin de commencer à suivre les modules.*
  - **Critères d’acceptation (Given/When/Then)**
    - **Given** je suis connecté et sur une fiche formation, **When** je clique sur “S’inscrire”, **Then** je suis inscrit et la formation apparaît dans mon tableau de bord.
    - **Given** je suis déjà inscrit, **When** je clique sur “S’inscrire”, **Then** le bouton est désactivé et un message “Déjà inscrit” s’affiche.

## 5) Suivi des modules et progression

- **Story** (Must) : *En tant qu’apprenant, je veux marquer un module comme terminé afin de suivre ma progression globale.*
  - **Critères d’acceptation (Given/When/Then)**
    - **Given** je suis inscrit à une formation, **When** je clique sur “Marquer comme terminé” pour un module, **Then** le module est marqué terminé et le pourcentage de progression est mis à jour.
    - **Given** je rafraîchis la page, **When** j’accède à la formation, **Then** l’état “Terminé” persiste pour le module.
- **Story** (Should) : *En tant qu’apprenant, je veux voir ma progression globale sur le tableau de bord afin d’identifier les formations en cours.*
  - **Critères d’acceptation (Given/When/Then)**
    - **Given** je suis connecté, **When** j’ouvre mon tableau de bord, **Then** chaque formation affiche un pourcentage de progression calculé.
    - **Given** je n’ai aucune formation, **When** j’ouvre le tableau de bord, **Then** un message “Aucune formation en cours” est affiché.

## 6) Création et publication de formations (formateur)

- **Story** (Must) : *En tant que formateur, je veux créer une formation avec titre, description et modules afin de la publier aux apprenants.*
  - **Critères d’acceptation (Given/When/Then)**
    - **Given** je suis connecté en tant que formateur, **When** je crée une formation avec les champs requis, **Then** la formation est enregistrée en brouillon.
    - **Given** je publie une formation en brouillon, **When** je clique sur “Publier”, **Then** la formation devient visible dans le catalogue public.

## 7) Gestion des utilisateurs et formations (admin)

- **Story** (Must) : *En tant qu’admin, je veux activer ou désactiver un compte utilisateur afin de sécuriser l’accès à la plateforme.*
  - **Critères d’acceptation (Given/When/Then)**
    - **Given** je suis sur la page d’administration des utilisateurs, **When** je désactive un compte, **Then** l’utilisateur ne peut plus se connecter.
    - **Given** un compte est désactivé, **When** je le réactive, **Then** l’utilisateur peut se reconnecter.
- **Story** (Could) : *En tant qu’admin, je veux retirer une formation du catalogue afin de ne plus la proposer aux apprenants.*
  - **Critères d’acceptation (Given/When/Then)**
    - **Given** je suis sur la liste des formations, **When** je clique sur “Retirer”, **Then** la formation n’apparaît plus dans le catalogue public.
    - **Given** une formation est retirée, **When** un apprenant tente d’y accéder via l’URL, **Then** il voit un message “Formation indisponible”.

# Vérification de testabilité

Chaque story ci-dessus est :
- **Mesurable** : critères quantifiables (ex. progression en %, présence/absence d’éléments, état activé/désactivé).
- **Sans ambiguïté** : actions et résultats attendus explicités via Given/When/Then.
- **Testable** : chaque critère peut être validé par un test UI/funcionnel ou API.
