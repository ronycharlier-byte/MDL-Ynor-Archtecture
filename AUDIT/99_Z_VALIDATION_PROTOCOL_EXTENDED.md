---
layer: AUDIT
status: audit
canonical_id: MDLYNOR-AUDIT-VALIDATION-PROTOCOL-001
concept_id: MDLYNOR.AUDIT.VALIDATION_PROTOCOL_EXTENDED
citation_id: MDLYNOR-AUDIT-VALIDATION-PROTOCOL-001
document_role: validation
retrieval_weight: 0.16
source_of_truth: MDLYNOR-CANON-017
---

# Protocole de validation externe independante

Cadre:
- ce protocole fige une version du corpus a tester, mais ne pretend pas valider une universalite;
- `mu` et `dot mu` restent des indicateurs locaux derives;
- `D` reste un operateur correctif, pas une variable generative;
- toute hypothese demeure revisable si l evidence externe la contredit.

Base documentaire:
- `AUDIT/98_Z_CORPUS_RESTRUCTURATION_CANONIQUE.md`
- `CANON/17_SCIENTIFIC_VALIDATION.md`
- `CANON/19_EMPIRICAL_MEASUREMENT.md`
- `CANON/11_OPERATEUR_D.md`
- `CANON/08_MU_SURVIE.md`
- `CANON/20_PREDICTIVE_PILOTING.md`

## 1. Version figee a tester

La version de travail est le snapshot `MDLYNOR_EXTVAL_SNAPSHOT_2026-04-18`.
Elle correspond au tree corpus complet verrouille au moment de la creation du manifeste de campagne.

Table de verrouillage:

| Element | Statut |
|---|---|
| Corpus tree | tous les fichiers presentes au lock |
| Manifeste de reference | `AUDIT/00_CORPUS_AUDIT/01_A_AUDIT_CORPUS_AUDIT_SHA256_CANONICAL_MANIFEST.md` |
| Base de restructuration | `AUDIT/98_Z_CORPUS_RESTRUCTURATION_CANONIQUE.md` |
| Contrat de couche | `corpus_layers.json` v1.1 |
| Registre doctrinal | `CANON/00_REGISTRE_AUTORITE.md` et shards associes |

Regles de freeze:
- aucune creation, suppression, renommage ou retag de fichier apres lock;
- aucune retouche de seuil, de split, de poids ou de rubric apres ouverture du test final;
- aucune reutilisation de resultats externes pour reconfigurer le snapshot teste;
- aucun artefact technique ou audit ne peut etre promu a doctrine pendant la campagne.

## 2. Jeux experimentaux

Jeux internes:

| Jeu | Role | Taille minimale | Usage |
|---|---|---:|---|
| `J_cal` | calibration interne | 10 cas | verifier les estimateurs et confirmer les conventions de mesure |
| `J_val` | validation interne | 10 cas | comparer les variantes deja pre-registeres |
| `J_test` | test final untouched | 20 cas | produire la conclusion interne sans retuning ni ablation post hoc |

Jeux externes:

| Jeu | Role | Taille minimale | Usage |
|---|---|---:|---|
| `E1` | corpus externe independant | 40 cas | validation externe blindee sur une source disjointe |
| `E2` | corpus externe independant | 40 cas | replication independante avec equipe et pipeline distincts |

Structure de chaque corpus:
- 10 cas de calibration;
- 10 cas de validation;
- 20 cas de test final untouched.

Familles de cas a stratifier:
- definitional;
- relational;
- procedural;
- negative or unsupported;
- ambiguity or disambiguation.

Criteres d inclusion:
- un seul intent principal par cas;
- provenance stable et resolvable;
- `canonical_id` et `citation_id` disponibles quand un support canonique existe;
- aucune duplication exacte ou quasi duplication avec un autre split;
- texte de la question fixe avant la campagne;
- source set externe disjoint du corpus MDL Ynor et des autres corpus externes;
- packet d annotation complet.

Criteres d exclusion:
- intent multiple ou ambigu;
- citation non resolvable;
- metadata manquante ou incoherente;
- case deja vu dans un autre split;
- mirror ou derive directe du corpus principal;
- prompt, log, wrapper, release ou artefact temporaire utilise comme source primaire;
- materiau de quarantaine, sauf si il est explicitement marque comme contre-exemple controle;
- cas retouches apres ouverture du split.

## 3. Variables et estimateurs preenregistres

Variables operatoires:

| Variable | Definition operative | Estimateur preenregistre | Fenetre | Seuil ou usage |
|---|---|---|---|---|
| `alpha` | capacite de stabilisation effective | moyenne ponderee de la recuperation, de la retention de citation et du succes de correction | batch de 10 cas, agregation sur bloc de 40 cas | local, non universel |
| `beta` | pression de bruit documentaire | moyenne ponderee de la duplication, de la fuite et de l ambiguite | batch de 10 cas, agregation sur bloc de 40 cas | plus bas est mieux |
| `kappa` | dette de maintenance et friction interne | moyenne ponderee des metadonnees invalides, liens casses et couts de reconciliation | batch de 10 cas, agregation sur bloc de 40 cas | plus bas est mieux |
| `mu` | marge derivee | `alpha - beta - kappa` | meme fenetre que les composantes | bandes locales seulement |
| `dot mu` | pente de la marge | Theil-Sen sur 4 blocs consecutifs | minimum 4 blocs | alerte si negatif sur 2 fenetres |
| `epsilon` | amplitude de perturbation | proportion imposee par famille de perturbation | famille-specifique | 0.05, 0.10, 0.20 |
| `D` | projection vers le domaine sur | comparaison avant / apres projection | par cas | operateur correctif uniquement |

Metriques de resultat:

| Metrique | Type | Estimateur | Seuil de decision | Statut |
|---|---|---|---|---|
| `top5_pertinent_rate` | primaire | proportion de cas ou le top-5 contient le niveau de pertinence pre-registre | `>= 0.70` | seuil local, provisoire |
| `top1_useful_rate` | primaire | proportion de cas ou le top-1 est utile et source-correct | `>= 0.90` | seuil local, provisoire |
| `citation_canonical_rate` | primaire | proportion de citations resolues vers la source canonique correcte | `= 1.00` | seuil dur |
| `citation_stable_rate` | primaire | proportion de citations identiques a repetition / reseed | `= 1.00` | seuil dur |
| `archive_leak_rate` | primaire | proportion de fuites archive dans le retrieval interdit | `= 0.00` | seuil dur |
| `tech_leak_rate` | primaire | proportion de fuites technique dans le retrieval interdit | `= 0.00` | seuil dur |
| `duplicate_rate` | primaire | proportion de doublons top-k | `= 0.00` | seuil dur |
| `no_valid_source_rate` | primaire | proportion de reponses sans source valide | `= 0.00` | seuil dur |
| `monopoly_violation_rate` | primaire | proportion de cas ou une source domine au-dela du cap pre-registre | `= 0.00` | seuil dur |
| `average_score` | secondaire | moyenne, mediane, ecart-type et bootstrap BCa du score 0-10 | rapport seulement | support de lecture |
| `support_rate` | secondaire | part des objets `RAG_SUPPORT` dans les top-k | rapport seulement | descriptif |
| `canonical_rate` | secondaire | part des objets `CANON` dans les top-k | rapport seulement | descriptif |
| `quarantine_count` | secondaire | nombre de cas envoyes en quarantaine | `= 0` pour toute conclusion positive | garde-fou |
| `drift_global` | secondaire | variation agregee entre blocs consecutifs | alerte si `> 1.5` | garde-fou corpus-local |
| `inter_annotator_alpha` | garde-fou | Krippendorff alpha sur les labels principaux | `>= 0.67` minimum, `>= 0.80` prefere | independance de jugement |

Conventions d estimation:
- les taux binaires utilisent un intervalle de Wilson a 95 pour cent;
- les scores continus utilisent moyenne, mediane, variance, MAD et intervalle bootstrap BCa a 95 pour cent;
- `dot mu` utilise une pente robuste, jamais une simple lecture de deux points;
- les seuils ci-dessus sont des bandes de decision corpus-locales, pas des lois universelles;
- `mu` et `dot mu` sont reportes comme diagnostics, pas comme preuves autonomes de validite externe.

## 4. Criteres d echec

Echec protocolaire:
- le manifeste ne correspond plus au tree teste;
- un split est reutilise apres ouverture;
- un seuil est retouche apres observation du test final;
- une equipe voit a la fois les labels et la condition de run;
- le test final n est plus untouched;
- une source externe est en fait un miroir ou un derive du corpus principal.

Echec du modele:
- `archive_leak_rate > 0`;
- `tech_leak_rate > 0`;
- `citation_canonical_rate < 1.00` sur un split touche a la conclusion;
- `citation_stable_rate < 1.00` sur un split touche a la conclusion;
- `duplicate_rate > 0`;
- `no_valid_source_rate > 0`;
- `top5_pertinent_rate < 0.70` sur le test final untouched ou sur une replication externe;
- `top1_useful_rate < 0.90` sur le test final untouched ou sur une replication externe;
- `mu <= 0` sur le bloc de calibration ou de validation lorsque le corpus est cense rester en domaine de survie;
- `dot mu < 0` sur deux blocs consecutifs sans mitigation possible.

Echec d independance:
- meme equipe pour la selection du corpus, l annotation et la decision finale;
- annotateurs non blindes sur la condition ou le label attendu;
- adjudication faite avant le premier passage blind;
- corpus externe partage avec le corpus principal les memes sources ou le meme pipeline de construction.

## 5. Plan d annotation externe

Roles:

| Role | Fonction | Acces autorise | Interdits |
|---|---|---|---|
| Curator externe | assemble et nettoie le corpus externe | sources brutes, hashes, IDs de cas | labels, seuils, sorties du modele |
| Annotator A | premier passage blind | packets de cas anonymises, texte, citations candidates | condition de run, score attendu, split cible |
| Annotator B | second passage blind | memes elements que A | memes interdits que A |
| Adjudicator | resout les desaccords | disagreements, evidence pack, rubric figee | historique des choix internes, parametres caches du modele |
| Statistician | agrege les resultats | labels figees, seeds, logs | reannotation, reindexation, tuning |
| Operator | execute le modele | configuration figee, corpus verrouille | labels, consensus, adjudication |

Regles minimales:
- au moins 2 equipes externes distinctes pour `E1` et `E2`;
- aucune personne ne peut etre a la fois curator, annotator, adjudicator et operator;
- les annotateurs sont blindes au systeme, au split, a la condition et au seuil de decision;
- les annotateurs voient les textes et les citations candidates, mais pas la reponse attendue;
- l adjudication ne commence qu apres le premier passage blind;
- tout desaccord majeur va au trio blind -> adjudication -> enregistrement;
- si `inter_annotator_alpha < 0.67`, le bloc est descriptif seulement et ne peut pas porter de claim fort.

## 6. Plan d ablation

Principe:
- les ablations se font sur `J_cal` et `J_val`, jamais sur `J_test`;
- les variantes sont comparees a un baseline run sous meme seed et meme ordre de cas;
- le plan est one-factor-at-a-time, avec 2x2 pour les couplages critiques;
- une ablation a delta nul est un signal a investiguer, pas un succes automatique.

Facteurs a ablater:

| Facteur | Ablation | Signal attendu |
|---|---|---|
| Couche `CANON` | retirer l acces canonique | baisse des citations canoniques et hausse des unsupported |
| Couche `RAG_SUPPORT` | retirer l aide a la lecture | baisse du top5 pertinent et hausse de la variance |
| Couche `ARCHIVES` | autoriser ou retirer la couche archive | hausse de fuite ou baisse de couverture historique |
| Couche `TECHNIQUE` | exposer ou masquer les artefacts techniques | fuite technique si la barriere saute |
| Resolved citation | desactiver la resolution de citation | baisse de `citation_canonical_rate` et `citation_stable_rate` |
| Contract metadata | relacher `canonical_id`, `citation_id`, `document_role`, `retrieval_weight` | hausse du no-valid-source et des collisions |
| Anti-monopoly | retirer le cap de dominance top-k | hausse de concentration et de violation |
| Operator `D` | desactiver la projection safe-domain | hausse des etats hors domaine |
| `mu` / `dot mu` | supprimer le monitoring de marge | perte d alerte precoce, pas de garantie de correction |
| Blind annotation | remplacer par annotation visible | hausse du biais de confirmation |
| Adjudication | supprimer le second passage | hausse des desaccords non resolus |
| Quarantine | supprimer la quarantaine | augmentation du bruit et des cas ambigus dans la sortie |

Couplages critiques a tester en 2x2:
- `CANON` x `RAG_SUPPORT`;
- `D` x `citation resolution`;
- `blind annotation` x `adjudication`;
- `quarantine` x `leak gates`.

Critere de valeur d une ablation:
- elle doit modifier au moins une metrique primaire dans la direction attendue;
- elle doit le faire sans toucher au test final untouched;
- elle doit produire un delta avec intervalle d incertitude, pas seulement une intuition.

## 7. Plan de perturbation

Families de perturbation:

| Famille | Construction | `epsilon` | Metriques surveillees |
|---|---|---:|---|
| Textuelle | orthographe, ponctuation, casse, segmentation | 0.05 / 0.10 / 0.20 | top5, top1, citation stable |
| Provenance | renommage de section, normalisation de chemin, alias de citation | 0.05 / 0.10 / 0.20 | citation canonical, citation stable |
| Retrieval | insertion de distracteurs, doublons, miroirs controles | 0.05 / 0.10 / 0.20 | leakage, duplicate, monopoly |
| Metadata | suppression ou corruption de champs non critiques | 0.05 / 0.10 / 0.20 | no-valid-source, quarantine, drift |
| Temporelle | permutation des cas, reseed, reorder des lots | 0.05 / 0.10 / 0.20 | dot mu, variance, stabilite inter-run |

Regles:
- la perturbation est definie avant execution;
- le jeu perturbe garde sa clef de verite, sauf dans le sous-ensemble explicitement destine a la corruption;
- le code de perturbation est fige et logge;
- si une perturbation ameliore artificiellement les scores, elle est traitee comme suspicion de leakage ou de Goodhart, pas comme succes.

## 8. Sorties statistiques requises

Chaque run doit produire:
- un score par cas;
- une moyenne, une mediane, une variance, un ecart-type et une MAD par split;
- un intervalle a 95 pour cent pour chaque metrique primaire;
- une mesure d accord inter-annotateurs;
- une mesure de heterogeneite entre corpus externes;
- un delta baseline vs ablation;
- un delta baseline vs perturbation;
- des drapeaux de non-conclusion.

Estimation imposee:
- proportions binaires: Wilson a 95 pour cent;
- scores continus: BCa bootstrap a 95 pour cent;
- slopes: Theil-Sen ou pente robuste equivalente;
- accord: Krippendorff alpha;
- variance inter-run: variance empirique par seed et par bloc;
- heterogeneite inter-corpus: range et, si le nombre de corpus le permet, variance entre corpus.

Artifacts requis:
- `results.json`;
- `results.md`;
- `split_manifest.json`;
- `annotation_log.jsonl`;
- `adjudication_log.jsonl`;
- `seed_log.json`;
- `lock_manifest.json`.

Conditions de non-conclusion:
- l intervalle de confiance d une metrique primaire chevauche le seuil de decision;
- la variance entre annotateurs ou entre corpus est trop large pour un jugement stable;
- le nombre de cas valides est inferieur au minimum pre-registre;
- l independance externe est incomplete;
- le test final a ete touche avant la fin du protocole.

## 9. Conditions d interpretation

| Statut | Ce que cela veut dire | Ce que cela ne veut pas dire |
|---|---|---|
| Confirmation partielle | le corpus survit a au moins une validation externe blindee avec independance reelle | preuve universelle |
| Invalidation partielle | au moins un corpus externe ou une famille de perturbation casse les seuils primaires | invalidation totale de tout le cadre |
| Echec du modele | echec sur test final untouched, ou fuite / citation / source fail hard | simple bruit experimental |
| Besoin de recalibration | les resultats ne tiennent que si les seuils, les fenetres ou `D` sont reajustes sur la calibration | rejet definitif de toute valeur du corpus |
| Non-conclusion | evidence incomplete, intervalle trop large ou independance insuffisante | confirmation implicite |

Regles de lecture:
- `mu` et `dot mu` classent l etat local du corpus, mais ne generalisent pas a eux seuls;
- une bonne performance interne ne suffit jamais pour conclure a une validite externe;
- une baisse sur externe peut signifier une vraie limite de domaine, pas forcement une panne globale;
- si les bandes de seuils doivent etre retouchees apres coup, la bonne conclusion est recalibration, pas victoire.

## 10. Protocole final de validation externe

Ordre d execution:

1. geler le snapshot, le manifeste et le lock file;
2. verifier les hashes et la conformite au contrat de couche;
3. constituer `J_cal`, `J_val` et `J_test` sur le corpus interne fige;
4. constituer `E1` et `E2` sur des sources externes disjointes;
5. produire les packets d annotation anonymises;
6. faire passer `J_cal` par la calibration et valider les estimateurs;
7. figer les seuils, les fenetres et le plan d ablation;
8. executer `J_val` et les ablations pre-registrees;
9. ouvrir `J_test` une seule fois et ne plus le retoucher;
10. faire annoter `E1` et `E2` en blind, puis adjudication separee;
11. executer la suite de perturbations controlees;
12. calculer scores, variances, intervalles et heterogeneite;
13. classer le resultat en confirmation partielle, invalidation partielle, echec, besoin de recalibration ou non-conclusion;
14. archiver tous les manifests, logs, seeds et resultats.

Arret immediat si:
- une fuite archive ou technique apparait sur un split touche a la conclusion;
- la citation canonique ou la stabilite de citation chute sur le test final;
- l independance externe ou le blind est rompu;
- une retouche post-hoc du seuil ou du split est necessaire.

Conclusion operatoire:
- ce protocole est executable, sobre et publiable;
- il n'agrandit pas artificiellement le corpus;
- il accepte explicitement la possibilite d un echec reel;
- il ne transforme pas une validation locale en preuve universelle.
