# Écrans Quiz, Résultats et Feedback

## 1. Écran « Quiz »

### Objectif
Permettre à l’apprenant de répondre aux questions tout en visualisant sa progression et, si activé, un timer.

### Structure
- **Header**
  - Titre du quiz
  - Indicateur de progression (ex. « 3/10 »)
  - Barre de progression (linéaire)
- **Zone question**
  - Intitulé de la question
  - Contexte optionnel (ex. extrait de texte, image)
- **Zone réponses**
  - Choix multiples (radio ou cartes)
  - État sélectionné clairement visible
- **Footer**
  - Bouton « Valider » (désactivé tant qu’aucune réponse)
  - Bouton « Passer » (optionnel, si la règle le permet)

### Timer (optionnel)
- **Affichage** : badge discret en haut à droite (ex. « 00:45 »)
- **Comportement** :
  - Démarre à l’entrée de la question
  - Décompte jusqu’à 0 puis passe automatiquement à la question suivante (ou verrouille la question selon la règle)

### États UX
- **Avant réponse** : question active, réponses cliquables
- **Après validation (feedback instantané)** :
  - Réponse correcte en vert, incorrecte en rouge
  - Icône de feedback + texte court (« Correct » / « Incorrect »)
  - Bouton « Suivant »

---

## 2. Écran « Résultats »

### Objectif
Synthétiser la performance globale et guider l’apprenant vers les points à améliorer.

### Structure
- **Header**
  - Titre « Résultats »
  - Score global (ex. « 8/10 »)
  - Pourcentage de réussite (ex. « 80 % »)
- **Résumé**
  - Indicateur visuel (cercle/anneau de progression)
  - Message d’encouragement selon le score
- **Mauvaises réponses**
  - Liste des questions échouées
  - Pour chaque item :
    - Intitulé court
    - Réponse donnée vs bonne réponse
    - Lien « Voir explication » (redirige vers Feedback)
- **Actions**
  - « Revoir le quiz » / « Retenter »
  - « Accéder aux ressources »

---

## 3. Écran « Feedback »

### Objectif
Fournir une explication détaillée et recommander des ressources pour progresser.

### Structure
- **Header**
  - Titre « Feedback »
  - Indicateur question (ex. « Question 4/10 »)
- **Zone explication**
  - Réponse correcte avec justification
  - Points clés / rappels
- **Ressources recommandées**
  - Liste de ressources (articles, vidéos, modules)
  - Chaque ressource : titre, type, durée estimée
- **Navigation**
  - Bouton « Question suivante »
  - Bouton « Retour aux résultats »

---

## 4. Règles de feedback

### Option A — Feedback instantané
- L’apprenant voit immédiatement si sa réponse est correcte.
- Avantages : apprentissage rapide, correction immédiate des erreurs.
- Recommandé pour : quizz courts, auto-formation.

### Option B — Feedback différé
- L’apprenant reçoit le feedback uniquement à l’écran Résultats.
- Avantages : limite l’influence sur les questions suivantes, favorise la concentration.
- Recommandé pour : évaluations formelles, certification.

### Paramétrage conseillé
- **Mode entraînement** : feedback instantané + explication rapide après chaque question.
- **Mode évaluation** : feedback différé + explications complètes sur écran Feedback.
