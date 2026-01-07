# Cadrage MVP — Plateforme SkillForge

## 1) Objectifs business immédiats
- **Onboarding rapide** : réduire la friction d’entrée (inscription/connexion simple, profil minimal).
- **Validation de compétences** : attester l’acquisition via questionnaires + certification.
- **Activation utilisateur** : conduire l’utilisateur à terminer un parcours en moins de 7 jours.
- **Crédibilité / monétisation** : certificats partageables et traçables.
- **Engagement** : progression claire et jalonnée.

## 2) Classement des domaines (dépendances, valeur, risque)

| Domaine | Dépendances | Valeur utilisateur | Risque technique | Priorité |
| --- | --- | --- | --- | --- |
| Auth | Base pour personnalisation et suivi | Accès & compte | Modéré | 1 |
| Parcours | S’appuie sur auth | Structure l’apprentissage | Modéré | 2 |
| Questionnaires | Rattachés à un parcours | Validation des acquis | Moyen | 3 |
| Certificats | Dépend des résultats | Forte valeur post-complétion | Moyen | 4 |

## 3) MVP strict (parcours complet de bout en bout)

**Objectif : permettre un parcours complet de bout en bout, sans extras.**

- **Auth** : inscription/connexion basique (email + mot de passe).
- **Parcours** : un parcours simple composé d’étapes.
- **Questionnaires** : un quiz par étape, scoring basique et résultat.
- **Certificat** : génération d’un certificat si score ≥ seuil.
- **Suivi** : progression utilisateur minimale (statuts “en cours” / “complété”).

## 4) MVP étendu (nice-to-have proches du cœur)

- **Auth** : reset de mot de passe, SSO basique.
- **Parcours** : tags, filtres, prérequis, parcours multiples.
- **Questionnaires** : banque de questions, feedback détaillé.
- **Certificats** : QR code, partage LinkedIn, personnalisation visuelle.
- **Reporting léger** : tableau de progression global.

## 5) Extension demandée : labs interactifs intégrés

**Objectif :** permettre à l’utilisateur de lancer des labs depuis l’application (ex. création de container), avec un environnement de lab connecté aux outils internes.

- **Cas d’usage principal** : depuis une étape de parcours, l’utilisateur déclenche un lab (ex. lancer un conteneur de TP), interagit avec un environnement isolé, et récupère un score ou un statut de réussite.
- **Contraintes clés** :
  - Isolation par utilisateur / session.
  - Temps de provisioning rapide (objectif < 2 min).
  - Traçabilité (qui a lancé quoi, durée, résultats).
  - Sécurité (ressources limitées, sandboxing, quotas).

## 6) Validation des priorités

- **Produit** : conforte la priorisation sur la valeur utilisateur et l’activation.
- **Tech** : valide la faisabilité et réduit les risques.
- **Métiers** : confirme l’adéquation aux objectifs formation/compétences.

**Livrables de validation** :
- 1 page de synthèse MVP (objectifs + MVP strict + MVP étendu).
- Décisions de priorité (auth → parcours → questionnaires → certificats).
- Roadmap indicative (2–3 lots).
