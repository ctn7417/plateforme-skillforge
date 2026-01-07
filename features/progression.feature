# language: fr
Fonctionnalité: Progression et certification
  Afin de garantir l'accès au quiz et la délivrance de certification
  En tant qu'utilisateur inscrit et connecté
  Je veux finaliser les modules puis lancer le quiz selon ma progression

  Contexte:
    Étant donné un catalogue "Parcours Data" avec les modules "M1", "M2" et "M3"

  @parcours_critique
  Scénario: Parcours complet avec certification délivrée
    Étant donné un utilisateur inscrit et connecté "alice"
      Et sa progression est complète sur "Parcours Data"
    Quand il termine tous les modules du parcours
      Et il lance le quiz final
      Et il obtient un score de 85
    Alors le quiz est accessible
      Et la certification est délivrée
      Et le statut de certification est "délivrée"

    Données de test minimales:
      | utilisateur | parcours      | modules complétés | score | score requis | certification |
      | alice       | Parcours Data | M1,M2,M3          | 85    | 70           | délivrée      |

  Scénario: Progression partielle - quiz verrouillé
    Étant donné un utilisateur inscrit et connecté "bruno"
      Et sa progression est partielle sur "Parcours Data"
      Et il a complété les modules "M1" et "M2"
    Quand il tente de lancer le quiz final
    Alors le quiz est verrouillé
      Et un message indique "Complétez tous les modules pour débloquer le quiz"

    Données de test minimales:
      | utilisateur | parcours      | modules complétés | modules restants | quiz accessible |
      | bruno       | Parcours Data | M1,M2             | M3               | non             |

  Scénario: Reprise - progression conservée
    Étant donné un utilisateur inscrit et connecté "carla"
      Et sa progression est partielle sur "Parcours Data"
      Et il a complété le module "M1"
    Quand il se déconnecte puis se reconnecte
    Alors sa progression conserve le module "M1" comme terminé
      Et il peut reprendre au module "M2"

    Données de test minimales:
      | utilisateur | parcours      | modules complétés | module suivant |
      | carla       | Parcours Data | M1                | M2            |

  Scénario: Score insuffisant - certification non délivrée, tentative autorisée
    Étant donné un utilisateur inscrit et connecté "diego"
      Et sa progression est complète sur "Parcours Data"
    Quand il lance le quiz final
      Et il obtient un score de 60
    Alors la certification n'est pas délivrée
      Et une nouvelle tentative est autorisée

    Données de test minimales:
      | utilisateur | parcours      | score | score requis | tentative autorisée |
      | diego       | Parcours Data | 60    | 70           | oui                 |

  Scénario: Score insuffisant - certification non délivrée, tentative refusée
    Étant donné un utilisateur inscrit et connecté "elena"
      Et sa progression est complète sur "Parcours Data"
      Et elle a déjà utilisé 3 tentatives
    Quand elle lance le quiz final
      Et elle obtient un score de 65
    Alors la certification n'est pas délivrée
      Et une nouvelle tentative est refusée
      Et un message indique "Nombre maximal de tentatives atteint"

    Données de test minimales:
      | utilisateur | parcours      | score | score requis | tentatives utilisées | tentatives max | tentative autorisée |
      | elena       | Parcours Data | 65    | 70           | 3                    | 3             | non                 |
