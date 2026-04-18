---
layer: AUDIT
status: audit
canonical_id: MDLYNOR-AUDIT-RESTRUCTURE-001
concept_id: MDLYNOR.AUDIT.CORPUS_RESTRUCTURATION
citation_id: MDLYNOR-AUDIT-RESTRUCTURE-001
document_role: validation
retrieval_weight: 0.14
source_of_truth: MDLYNOR-CANON-015
---

# Diagnostic global

Le corpus est deja solide sur trois points:
- la separation de couche existe;
- le noyau `mu = alpha - beta - kappa` est stable;
- le principe "one concept, one canonical source" est deja presente.

Mais le corpus restait affaibli par:
- des collisions de roles entre doctrine, pack operationnel et artefacts techniques;
- des metadonnees incompltes sur plusieurs fichiers de gouvernance;
- une formalisation parfois plus rhetorique que testable;
- des seuils et des regimes presentes comme quasi-universels alors qu ils doivent rester calibres;
- une distinction encore insuffisante entre preuve, interpretation, convention de calibration et speculation.

# Ce qu il faut absolument conserver

- La separation `CANON` / `RAG_SUPPORT` / `ARCHIVES` / `TECHNIQUE` / `MONITORING` / `AUDIT` / `INBOX_QUARANTAINE`.
- Le principe de source canonique unique par concept.
- Le noyau `alpha`, `beta`, `kappa`, `mu`.
- La projection vers un domaine sur pour les corrections.
- La discipline anti-Goodhart.
- La logique de validation et de tracabilite deja installee.

# Defauts critiques

1. Un pack operationnel etait traite comme doctrine canonique.
2. Plusieurs fichiers de gouvernance manquaient de `citation_id`, `document_role` et `retrieval_weight`.
3. L index canonique omettait un element central de la fin du noyau.
4. Les variables centrales etaient definies, mais pas suffisamment operationalisees.
5. Des seuils de regime etaient exprimes comme des lois stables alors qu ils sont des bandes de calibration.

# Defauts importants mais non critiques

- Redondances entre fiches voisines.
- Style parfois declaratif au lieu de testable.
- Terminologie parfois flottante autour de `support`, `navigation`, `registry`, `answer_card`.
- Formalisme parfois decoratif dans les sections topologiques ou cognitives.
- Validation interne trop souvent confondue avec demonstration generale.

# Architecture documentaire corrigee

## Couche canonique

Contient uniquement les sources autoritaires de premier rang.
Ordre de lecture:
1. portail et registre
2. constitution
3. theorie
4. glossaire et identifiants
5. variables et regimes
6. validation empirique

## Couche support

Contient les resumes chunkables, crosswalks, guides de lecture et aides a la citation.
Elle aide la retrieval, mais n ajoute pas de doctrine.

## Couche archive

Contient versions anciennes, miroirs, releases, logs, exports et preuves historiques.
Elle conserve la trace, pas l autorite.

## Couche technique

Contient code, scripts, configurations, dashboards, packages operationnels et artefacts generes.
Elle execute ou instrumente, mais ne fonde pas la doctrine.

## Couche audit

Contient benchmark, tests, rapports, journaux de correction, controles de derivation et resultats de validation.

## Couche monitoring

Contient la surveillance active, les health reports et les signaux de drift.

## Couche quarantaine

Contient les objets ambigus, temporaires ou non classes.

# Gouvernance documentaire corrigee

Champs a rendre obligatoires pour tout document admissible en production:
- `layer`
- `status`
- `canonical_id`
- `concept_id`
- `citation_id`
- `document_role`
- `retrieval_weight`

Champs recommandes:
- `source_of_truth`
- `source_path`
- `chunking_policy`

Regles:
- un concept correspond a une source canonique unique;
- un `citation_id` doit pointer vers une unite stable et resolvable;
- un document purement operationnel ou technique ne doit pas vivre comme doctrine;
- un document archive ne doit pas concurrencer une source canonique vivante;
- toute reponse de production doit citer un support canonique ou retourner "unsupported".

Classification minimale des roles:
- `navigation`
- `registry`
- `registry-shard`
- `answer_card`
- `glossary`
- `constitution`
- `theory`
- `validation`
- `measurement`
- `operational-pack`
- `audit-root`
- `technical-root`
- `monitoring-root`
- `quarantine-root`

# Glossaire conceptuel normalise

- `canonical_id`: identifiant stable de la source canonique.
- `citation_id`: cible citeable et stable pour un chunk ou une section.
- `concept_id`: etiquette semantique du concept.
- `document_role`: fonction documentaire precise.
- `source_of_truth`: document ou couche qui fait autorite pour la valeur.
- `retrieval_weight`: score de priorite relatif pour le retrieval.
- `layer`: couche documentaire declarative.
- `status`: etat gouvernance du document.
- `alpha`: capacite de stabilisation effective.
- `beta`: pression de bruit, duplication et propagation parasite.
- `kappa`: dette de maintenance, friction et instabilite d encodage ou de nommage.
- `mu`: marge de survie documentaire, definie par `mu = alpha - beta - kappa`.
- `dot mu`: variation temporelle de `mu`.
- `epsilon`: amplitude de perturbation externe.
- `D`: operateur de projection vers le domaine sur.

# Structure mathematique corrigee

## Defininitions

- `S(t)`: etat du corpus ou du systeme etudie.
- `E(S)`: amplification ou force expansive.
- `D(S)`: dissipation ou projection de securite.
- `M(S_t)`: memoire ou inertie.
- `w(t)`: perturbation admissible.
- `mu`: marge structurale.

## Axiomes utiles

1. La dissipation doit dominer assez pour rendre `mu` positif dans le domaine voulu.
2. L amplification doit rester bornee et interpretable.
3. La memoire doit rester controlee.
4. La perturbation doit etre mesuree, pas supposee infinie.

## Ce qui est conserve

- le schema `dot S = E(S) - D(S) + M(S_t) + w(t)`;
- le calcul `mu = alpha - beta - kappa`;
- la lecture par regimes.

## Ce qui est reduit

- toute pseudo-formalisation qui ne produit ni prediction ni test;
- toute notation qui n est pas reliee a un observable;
- toute extension topologique sans protocole de mesure.

# Structure scientifique corrigee

Le champ principal du corpus est:
- un cadre documentaire et operationnel a marge dissipative;
- interprete comme systeme de gouvernance de retrieval, de stabilite et de validation;
- potentiellement applicable a d autres systemes, mais seulement dans le domaine ou la calibration tient.

Separation stricte:
- description: ce que le corpus fait;
- explication: pourquoi la marge compte;
- prediction: ce que `mu` laisse anticiper;
- norme: ce que le corpus prescrit pour lui-meme;
- speculation: toute extension au-dela des preuves.

Ce qui est testable:
- unicite des sources canoniques;
- absence de leakage archive dans le top retrieval;
- stabilité des citations;
- evolution de `mu` sur des jeux de validation;
- robustesse aux perturbations controllees.

Ce qui ne l est pas encore totalement:
- universalite du cadre;
- interpretation ontologique forte de `mu`;
- transposition sans recalibration a des domaines tres differents.

# Variables a operationaliser

| Variable | Definition | Observable associe | Estimation | Unite / echelle | Plage valide | Limites |
| --- | --- | --- | --- | --- | --- | --- |
| `alpha` | capacite de stabilisation effective | taux de retour a l etat sur, retention de citation, correction utile | score de recalibration a partir de tests de recouvrement | score normalise | domaine calibre | n est pas une constante universelle |
| `beta` | bruit documentaire et pression de duplication | duplicate rate, archive leakage, mirror recurrence, ambiguity rate | ratio de bruit ou score penalise | score normalise | domaine calibre | depend du corpus et de sa taille |
| `kappa` | dette de maintenance et friction interne | erreurs d encodage, nommage instable, liens casss, cout de reconciliation | score d audit technique | score normalise | domaine calibre | capture aussi des couts humains |
| `mu` | marge de survie | combinaison des trois precedentes | `alpha - beta - kappa` | score derive | domaine calibre | utile seulement si `alpha`, `beta`, `kappa` sont calibrables |
| `dot mu` | vitesse de variation de la marge | pente sur fenetre temporelle | difference finie ou regression locale | score / temps | domaine calibre | sensible au bruit court terme |
| `epsilon` | amplitude de perturbation | choc, injection, bruit, drift | mesure de perturbation imposee | score ou unite native | scenario defini | n est pas la sortie du systeme |
| `D` | projection de securite | elimination des etats hors domaine | operateur binaire ou projection | operateur | toujours defini sur le domaine sur | doit etre monotone et explicite |

Regle pratique:
- si une variable ne peut pas etre reliee a un observable, elle doit etre reframee comme convention ou supprimee.

# Plan de validation renforce

1. Validation interne:
- tests de front matter;
- unicite des `canonical_id`;
- resolvabilite des `citation_id`;
- detection de doublons et de fuites archive.

2. Validation externe:
- relecture independente;
- comparaison avec corpus temoins;
- controle de plausibilite hors du corpus.

3. Ablation:
- retirer une couche, un shard ou une regle et mesurer la degradation.

4. Perturbations controlees:
- injecter des doublons, des variantes orthographiques, des miroirs ou des faux positifs et mesurer la robustesse.

5. Separation calibration / validation:
- calibrer les seuils sur un sous-ensemble;
- evaluer sur un autre sous-ensemble non vu.

6. Mesures longitudinales:
- suivre `mu`, `dot mu`, leakage, et temps de recuperation dans le temps.

7. Incertitude:
- fournir intervalles, pas seulement des points.

# Corrections prioritaires par ordre d urgence

1. Maintenir hors CANON tout pack operationnel ou wrapper.
2. Completer les metadonnees de tous les fichiers de gouvernance.
3. Normaliser les roles documentaires et les seuils de retrieval.
4. Traiter les regimes de `mu` comme bandes de calibration, pas comme lois absolues.
5. Rendre les variables centrales observables et auditables.
6. Renforcer les protocoles d ablation, de replique et d incertitude.
7. Nettoyer les doublons conceptuels entre archives et support.

# Version canonique amelioree du corpus

Version courte:
- Le corpus MDL Ynor est un systeme documentaire a couches explicites.
- `CANON` porte les sources autoritaires.
- `RAG_SUPPORT` porte l aide a la lecture.
- `ARCHIVES` porte la trace historique.
- `TECHNIQUE` porte l execution.
- `MONITORING` porte l observation.
- `AUDIT` porte la preuve et la validation.
- `INBOX_QUARANTAINE` porte l ambigu.
- Le noyau formel est `S(t)`, `E`, `D`, `M`, `w`, `alpha`, `beta`, `kappa`, `mu`, `dot mu`.
- La discipline scientifique consiste a separer description, explication, prediction, norme et speculation.
- La discipline documentaire consiste a separer source, support, archive, outil, audit et quarantaine.

Version canonique plus forte:
- Une source canonique ne concurrence pas une autre source canonique.
- Une variable non observable n est pas encore une variable operative.
- Une performance apparente qui degrade `mu` est une regression, pas un succes.
- Une preuve non citable n est pas une preuve de production.

# Verdict final sur le gain obtenu

Le corpus passe d un proto-systeme tres avance mais encore partiellement brouille a un cadre plus robuste, plus citable et plus audit-able.

Gain principal:
- separation documentaire nette;
- gouvernance plus stricte;
- noyau mathematique plus propre;
- statut epistemique plus explicite;
- validation plus testable.

Risque residuel principal:
- la validation empirique reste la partie la plus faible du systeme.

Conclusion:
- le corpus gagne en coherence, en credibilite internationale et en resistance au drift;
- il reste a durcir encore les benchmarks et la replication independante pour atteindre un niveau pleinement mature.
