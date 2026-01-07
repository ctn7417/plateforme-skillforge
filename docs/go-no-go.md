# Processus Go/No-Go

## 1. Documents d’entrée

| Document | Contenu attendu | Responsable (R) | Statut (à compléter) |
| --- | --- | --- | --- |
| **KPI** | Résultats clés vs objectifs (performance, stabilité, disponibilité, sécurité). | Product/Tech Lead | ☐ OK ☐ KO |
| **Checklist** | Points bloquants vérifiés (pré-requis, conformité, tests, dépendances). | Release Manager | ☐ OK ☐ KO |
| **Rapport QA** | Couverture et résultats de tests (fonctionnels, régression, automatisés). | QA Lead | ☐ OK ☐ KO |
| **Rapport UAT** | Validation métier, cas d’usage critiques, retours utilisateurs. | Product Owner | ☐ OK ☐ KO |
| **Risques ouverts** | Liste, impacts, mitigation, décision de tolérance au risque. | Risk Owner | ☐ OK ☐ KO |

## 2. Documents de sortie

| Document | Objectif | Livrable | Responsable (R) |
| --- | --- | --- | --- |
| **Décision formalisée** | Acter le Go/No-Go et ses conditions. | Compte rendu signé/validé. | Sponsor/Comité de décision |
| **Plan de déploiement** | Détail du déroulé opérationnel (fenêtre, étapes, responsables). | Plan détaillé + checklists. | Release Manager |
| **Plan rollback** | Procédure de retour arrière (critères, étapes, responsables). | Runbook rollback. | Tech Lead/Ops |

## 3. Format de réunion Go/No-Go

**Objectif :** décider si le déploiement peut être réalisé selon les critères définis.

### Agenda (60–90 min)
1. **Rappel du périmètre et des objectifs** (5 min)
2. **Revue KPI & Checklist** (10 min)
3. **Revue QA** (10 min)
4. **Revue UAT** (10 min)
5. **Risques ouverts & plans de mitigation** (10–15 min)
6. **Prérequis opérationnels (déploiement + rollback)** (10 min)
7. **Décision formelle Go/No-Go** (5 min)
8. **Actions et prochaines étapes** (5 min)

### Décision (à compléter en séance)
- **Décision :** ☐ Go ☐ Go avec conditions ☐ No-Go
- **Conditions (si Go conditionnel) :**
  - …
- **Critères de succès :**
  - …

### Validation
- **Décideur principal :** …
- **Décideurs associés :** …
- **Date/heure de validation :** …
- **Signature/accord :** …

## 4. Rôles et responsabilités (RACI simplifié)

| Rôle | Responsabilités clés |
| --- | --- |
| **Décideurs** | Arbitrage final Go/No-Go, acceptation des risques, validation du plan. |
| **Consultés** | Fournissent les rapports (QA, UAT, KPI, risques), avis techniques et métier. |
| **Informés** | Reçoivent la décision et le plan (Ops, Support, Sécurité, parties prenantes). |

## 5. Modèle de compte rendu standard

**Titre :** Compte rendu Go/No-Go – [Nom du projet] – [Date]

**Participants :**
- …

**Documents d’entrée validés :**
- KPI : ☐ OK ☐ KO (lien : …)
- Checklist : ☐ OK ☐ KO (lien : …)
- Rapport QA : ☐ OK ☐ KO (lien : …)
- Rapport UAT : ☐ OK ☐ KO (lien : …)
- Risques ouverts : ☐ OK ☐ KO (lien : …)

**Synthèse :**
- Points forts : …
- Points de vigilance : …
- Risques acceptés : …

**Décision :** ☐ Go ☐ Go avec conditions ☐ No-Go

**Conditions / Actions :**
| Action | Responsable | Échéance | Statut |
| --- | --- | --- | --- |
| … | … | … | ☐ |

**Plan de déploiement :** (lien vers le plan)

**Plan rollback :** (lien vers le plan)

**Communication :**
- Informer : …
- Canaux : …
- Date/heure : …

**Validation :**
- Décideur : …
- Date/heure : …
- Signature/accord : …
