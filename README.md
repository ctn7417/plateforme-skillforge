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
  - Valider la disponibilité des environnements et données de test.
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

