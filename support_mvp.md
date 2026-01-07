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
- **S0** : cadrage final + gel MVP strict.
- **S1–S2** : design + specs + POC intégrations critiques.
- **S3–S6** : build MVP strict + tests E2E minimaux.
- **S7** : pilote interne + collecte feedback.
- **S8** : release MVP strict.
- **S9+** : incréments MVP étendu (par lots)

---

# Validation finale (compte‑rendu + décisions)
- **Compte‑rendu** : décisions, risques acceptés, owners, échéances.
- **Décisions formalisées** : périmètre MVP, critères de succès, budget/ressources.
- **Signature** : Sponsor + Product + Tech + Compliance.
