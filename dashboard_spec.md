# Dashboard UI — Spécification fonctionnelle

## 1. Structure UI (3 sections principales)

Le dashboard est organisé en 3 sections disposées en grille (ou en colonnes empilées sur mobile) :

1. **News**
2. **Dates importantes**
3. **Formations obligatoires**

### Layout recommandé

- **Desktop** : 3 colonnes ou 2 colonnes + 1 pleine largeur selon contraintes UI.
- **Mobile** : sections empilées, même ordre.

Chaque section contient :
- Un **titre**.
- Une **liste d’éléments**.
- Un **CTA principal**.

---

## 2. Sources de données

| Section | Source | Exemple d’accès |
| --- | --- | --- |
| News | Flux éditorial commun / API (ex: `/api/news`) | Dernières publications |
| Dates importantes | Calendrier global (ex: `/api/calendar`) | Événements entreprise |
| Formations obligatoires | Assignations par utilisateur (ex: `/api/user/{id}/trainings`) | Suivi individuel |

---

## 3. Règles d’affichage

### News
- Afficher les **N dernières news** (ex: N=5).
- Pour chaque item : **titre**, **date**, **lien**.

### Dates importantes
- Afficher les **X prochaines dates** (ex: X=3).
- Ajouter un badge **“urgent”** si la date est dans les **7 prochains jours**.

### Formations obligatoires
Pour chaque formation assignée :
- **Statut** :
  - **À faire** (non démarrée)
  - **En cours** (progression en cours)
  - **En retard** (date limite dépassée)

---

## 4. CTAs principaux

| Section | CTA |
| --- | --- |
| News | **“Voir toutes les news”** |
| Dates importantes | **“Voir calendrier complet”** |
| Formations obligatoires | **“Accéder à la formation”** |

---

## 5. États UI (par section)

Chaque section doit gérer ses propres états :

### ✅ Loading
- Afficher un **skeleton** ou loader localisé à la section.

### ⚠️ Vide
- Afficher un message neutre :
  - News : “Aucune news disponible”
  - Dates : “Aucune date à venir”
  - Formations : “Aucune formation assignée”

### ❌ Erreur
- Afficher un message avec option de retry :
  - “Impossible de charger les données. Réessayer.”

