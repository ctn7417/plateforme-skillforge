# Support 1 page — Objectifs & MVP (strict / étendu)

## Objectifs
- Valider l’opportunité et l’alignement métier autour d’un MVP livrable en ≤ 8–10 semaines.
- Réduire le risque produit en priorisant un flux utilisateur bout‑en‑bout mesurable.
- Disposer d’un périmètre clair pour lancer l’exécution (tech, contenu, conformité).

## MVP strict (indispensable)
- **Parcours utilisateur clé** : inscription → sélection d’un parcours → premier contenu → validation de progression.
- **Gestion des contenus** : catalogue minimal (≤ 10 items), tagging simple, visibilité par rôle.
- **Suivi** : complétion des modules, statut utilisateur, export CSV basique.
- **Accès & sécurité** : SSO ou login email, rôles (admin / contributeur / apprenant).
- **Mesure** : 3 KPIs (activation, complétion, satisfaction rapide NPS‑like).

## MVP étendu (si capacité)
- **Personnalisation** : recommandations simples basées sur tags/profil.
- **Automatisation** : notifications email (rappel, fin de module).
- **Analytics avancés** : tableaux par cohortes, filtres, export enrichi.
- **Conformité** : gestion fine des consentements, politique de rétention.
- **Qualité** : tests E2E sur parcours clés + monitoring d’usage.

---

# Session de validation (45–60 min)
**Participants** : Sponsor, Product, Tech lead, Compliance, Ops/Support.

**Agenda**
1. **Rappel objectifs & contexte** (5 min)
2. **Présentation MVP strict vs étendu** (15 min)
3. **Risques majeurs & arbitrages** (15 min)
4. **Consensus & décisions** (10–15 min)
5. **Prochaines étapes** (5 min)

**Livrables attendus**
- MVP strict validé (oui/non, conditions)
- Liste des ajouts MVP étendu (priorisés)
- Go/No‑Go + owners des risques

---

# Risques majeurs (tech, métier, conformité)
## Tech
- **Intégrations** : SSO/IdP non stabilisé → risque de retard.
- **Scalabilité** : pics d’usage non anticipés → performance.
- **Qualité des contenus** : formats hétérogènes → effort d’ingestion.

## Métier
- **Adoption** : valeur perçue insuffisante sans accompagnement.
- **Périmètre** : dérives fonctionnelles (features “nice‑to‑have”).
- **ROI** : KPIs mal définis → décision difficile.

## Conformité
- **Données perso** : base légale / consentement à préciser.
- **Traçabilité** : exigences d’audit non couvertes.
- **Rétention** : politique de purge non définie.

---

# Ajustement de la roadmap (selon consensus)
## Planning de release (jalons + buffers)
**Objectif** : jalonner clairement la progression, prévoir des buffers de correction et sécuriser la décision Go/No‑Go.

| Semaine | Jalons | Objectifs | Livrables / preuves |
| --- | --- | --- | --- |
| **S0** | **Cadrage final + gel MVP strict** | Scope figé, alignement sur objectifs et risques. | Checklist cadrage signée, KPIs validés, compte‑rendu de décision. |
| **S1–S2** | **Design + specs + POC intégrations critiques** | Spécifications prêtes pour build. | Dossier specs, maquettes validées, rapport POC. |
| **S3–S6** | **Build MVP strict** | Delivery fonctionnel + tests E2E minimaux. | Backlog livré, rapport d’avancement, KPI dev (vélocité, qualité). |
| **S6 (fin dev)** | **Jalon fin dev** | Code complet + stable pour QA. | Checklist fin dev, rapport de stabilité (build, tests). |
| **S6–S7** | **QA interne** | Campagne QA + corrections critiques. | Rapport QA, matrice de release mise à jour. |
| **S7 (fin QA)** | **Jalon fin QA** | QA validée, passage UAT. | Checklist QA, anomalies résolues/acceptées. |
| **S7 (buffer)** | **Buffer corrections post‑QA** | Corrections bloquantes + re‑tests. | Rapport correctifs + re‑tests. |
| **S7–S8** | **UAT** | Validation métier et cas d’usage critiques. | Rapport UAT, retours consolidés, KPI d’acceptation. |
| **S8 (début UAT)** | **Jalon début UAT** | UAT démarrée avec périmètre figé. | Checklist début UAT, plan de test UAT. |
| **S8 (buffer)** | **Buffer corrections post‑UAT** | Corrections UAT + validation finale. | Rapport correctifs UAT + validation. |
| **S8 (Go/No‑Go)** | **Jalon Go/No‑Go** | Décision formalisée de release. | Compte‑rendu Go/No‑Go, checklist release, KPIs finaux. |
| **S8** | **Release MVP strict** | Mise en production + communication. | Rapport de release, notes de version, plan de suivi. |
| **S9+** | **Incréments MVP étendu (par lots)** | Ajouts itératifs. | Checklists de lot, rapports QA/UAT par lot. |

## Alignement & communication
- **Parties prenantes clés** : Sponsor, Product, Tech Lead, QA Lead, Ops/Support.
- **Rituels d’alignement** : points hebdo + revue de jalons (fin dev, fin QA, début UAT, Go/No‑Go).
- **Communication planning** : planning de release partagé (canal dédié + calendrier), mises à jour à chaque jalon avec liens vers livrables (checklists, KPI, rapports).

---

# Validation finale (compte‑rendu + décisions)
- **Compte‑rendu** : décisions, risques acceptés, owners, échéances.
- **Décisions formalisées** : périmètre MVP, critères de succès, budget/ressources.
- **Signature** : Sponsor + Product + Tech + Compliance.
