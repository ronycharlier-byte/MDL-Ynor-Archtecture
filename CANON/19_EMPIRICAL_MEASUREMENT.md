---
layer: CANON
status: canonical
canonical_id: MDLYNOR-CANON-019
concept_id: MDLYNOR.CONCEPT.EMPIRICAL_MEASUREMENT
citation_id: MDLYNOR-CANON-019
document_role: empirical-measurement
retrieval_weight: 1.08
---

# Empirical Measurement

Operational variables:

| Variable | Definition stricte | Observable associe | Methode d estimation | Echelle / unite | Intervalle de validite | Limites connues | Risque de circularite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `alpha` | capacite de stabilisation effective d un corpus sur un protocole fixe | taux de retour a l etat sur, retention de citation, correction utile apres perturbation | score calibre par tests de recouvrement et de restitution | score normalise `[0, 1]` ou `[0, 100]` | protocole, corpus et fenetre fixes | depend du jeu de test et du seuil de decision | fort si le meme jeu sert a calibrer et a evaluer |
| `beta` | pression de bruit documentaire et de duplication | duplicate rate, archive leakage, mirror recurrence, ambiguity rate | ratio penalise ou score de bruit pondere | score normalise ou proportion | meme protocole de mesure | sensible a la politique d indexation | fort si la politique de retrieval definit le bruit qu elle mesure |
| `kappa` | dette de maintenance et friction interne | erreurs d encodage, nommage instable, liens casss, cout de reconciliation | score d audit technique standardise | score normalise ou cout relatif | protocole d audit defini | capture aussi des couts humains et contextuels | modere si l audit est independant |
| `mu` | marge de survie derivee | combinaison des composantes calibrees | `alpha - beta - kappa` | score derive | seulement si `alpha`, `beta`, `kappa` sont deja valides | n est pas une mesure primaire | fort si on traite `mu` comme une mesure autonome |
| `dot mu` | vitesse de variation de `mu` | pente locale sur fenetre temporelle | difference finie ou regression locale sur fenetre predefinie | score / temps | fenetre suffisante pour filtrer le bruit | tres sensible au choix de la fenetre | fort si la fenetre est choisie apres observation du resultat |
| `epsilon` | amplitude de perturbation imposee ou observee | choc injecte, drift mesure, bruit exogene | amplitude protocolaire ou indice de perturbation | score ou unite native du stress | borne par le protocole | pas une propriete interne du corpus | faible si l amplitude est fixee avant l experience |
| `D` | operateur de projection vers le domaine sur | taux de rejet, correction, distance avant/apres projection, conservation de la validite | application binaire ou carte de projection validee sur des etats tests | operateur, pas un scalaire | defini seulement par rapport a un domaine sur independamment justifie | depend du criterium de surete | fort si le domaine sur est defini par une regle externe au seul operateur |

Interpretation:
- `alpha`, `beta` and `kappa` are operational if their observables are pre-registered and independently audited.
- `mu` is operational as a derived indicator, not as a primary observable.
- `dot mu` is operational only on fixed windows and only with a pre-declared estimator.
- `epsilon` is operational when the perturbation protocol is controlled and documented.
- `D` is operational as a correction operator, but it is not a scalar variable.

Rule:
- measurements are bounds, not absolutes.
- calibration and validation must remain decoupled.
- a variable is not operational if its observable is defined by the same rule it is meant to test.
