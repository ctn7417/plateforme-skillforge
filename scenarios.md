# Scénarios et cas limites – Parcours de formation

## 1. Scénario nominal par parcours
**Inscription → 100% progression → quiz → certification**
1. L’utilisateur s’inscrit au parcours.
2. Le parcours devient actif et le premier module est débloqué.
3. L’utilisateur suit tous les modules jusqu’à **100%** de progression.
4. Le quiz de fin de parcours devient disponible.
5. L’utilisateur passe le quiz et obtient un score **≥ seuil de réussite**.
6. Le système attribue la certification et affiche la date d’obtention.

## 2. Cas limites exigés
### 2.1 Progression partielle (40% ou 70%)
1. L’utilisateur s’inscrit et progresse jusqu’à **40%**.
2. Vérifier que le quiz final reste indisponible tant que la progression < 100%.
3. L’utilisateur progresse ensuite à **70%**.
4. Vérifier que seuls les modules correspondant au niveau atteint sont débloqués.

### 2.2 Reprise (retour après interruption)
1. L’utilisateur interrompt le parcours après avoir terminé le module 3.
2. Il revient plus tard.
3. Le système le repositionne sur le **dernier module complété**.
4. La progression et l’état des modules sont restaurés fidèlement.

### 2.3 Score insuffisant (échec du quiz, ré-essai)
1. L’utilisateur atteint 100% et passe le quiz.
2. Il obtient un score **< seuil de réussite**.
3. Le système affiche l’échec et propose un **nouvel essai**.
4. Après ré-essai avec score **≥ seuil**, la certification est attribuée.

## 3. Cas limites usuels
### 3.1 Quiz non disponible / module verrouillé
1. L’utilisateur tente d’accéder au quiz avant 100% de progression.
2. Le système refuse l’accès et indique que le quiz est verrouillé.
3. L’utilisateur tente d’ouvrir un module non débloqué.
4. Le module est indiqué comme **verrouillé** et l’accès est bloqué.

### 3.2 Abandon en milieu de quiz
1. L’utilisateur démarre le quiz.
2. Il quitte le quiz avant de le terminer.
3. À la reprise, le système :
   - soit reprend la tentative en cours (si autorisé),
   - soit considère l’essai comme abandonné et propose un nouvel essai.

### 3.3 Certification déjà obtenue
1. L’utilisateur a déjà obtenu la certification.
2. Il tente de repasser le quiz.
3. Vérifier le comportement attendu :
   - **Ré-attribution bloquée** : le quiz est désactivé et la certification reste inchangée.
   - **Ré-attribution autorisée** : le quiz est disponible mais n’altère pas la date de certification (sauf règle explicite).

## 4. Règles métier à valider
- **Seuil de réussite** : définir une valeur (ex. **70%** ou **80%**) et vérifier l’application stricte.
- **Nombre de tentatives** : illimité vs limité (ex. **3 tentatives**), vérifier les blocages.
- **Accès au quiz** : uniquement à **100%** de progression.
- **Déverrouillage des modules** : séquentiel (module N+1 après module N).
- **Reprise** : redémarrage au **dernier module complété** avec progression conservée.
- **Certification** : attribuée uniquement si progression = 100% **et** score ≥ seuil.
- **Repassage du quiz** : comportement explicite si certification déjà obtenue.
