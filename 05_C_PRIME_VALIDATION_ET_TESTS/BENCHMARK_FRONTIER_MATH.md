---



STATUS: CANONICAL | V11.13.0 | SOURCE: UNIFIED | 



AUDIT: CERTIFIED 2026-04-06



---



# BENCHMARK EXISTANT — FRONTIERMATH







## Prsentation



**Nom du benchmark :** FrontierMath



**Nature :** Benchmark existant de raisonnement mathmatique avanc. Il a tconçu autour de problmes originaux, non publis, afin de limiter au maximum la contamination par mmorisation et de tester un raisonnement rellement soutenu.







## Fondement



FrontierMath est structuren plusieurs niveaux de difficult(“tiers”), allant de l'olympiade de haut niveau la recherche pure :



- **Tiers 1–3 (Base Set) :** 300 problmes couvrant la thorie des nombres, la gomtrie algbrique, l'analyse relle et la combinatoire.



    - **Tier 1 :** Équivalent aux problmes d'olympiades nationales/internationales.



    - **Tiers 2 & 3 :** Expertise de niveau master/doctorat (rsolution par un expert en plusieurs heures/jours).



- **Tier 4 (Expansion Set) :** 50 problmes de niveau recherche (rsolution par un expert en plusieurs semaines).







## Mtriques d'Évaluation (Epoch AI)



Le benchmark value la difficultselon trois axes :



- **Background (1-5) :** Niveau de connaissances (1: Lyce, 3: Licence, 5: Recherche).



- **Creativity :** Temps estimpour identifier l'ide clde la solution.



- **Execution :** Temps estimpour finaliser la preuve/calcul aprs l'ide cl.







## Pourquoi c’est l’un des plus durs



- **Problmes originaux :** Conçus pour être "Guess-Proof" et viter la contamination (Zero-shot contamination).



- **Tool-Assisted :** Les modles ont accs des environnements de calcul (Python) pour vrifier leurs tapes, testant ainsi la capacitutiliser des outils de manire rigoureuse.



- **Difficultextrême :** Atteint le niveau de la recherche mathmatique contemporaine.







## Objectif au sein de l'Architecure MDL Ynor



Tester si un systme est capable de :



- Raisonner sous forte complexit.



- Maintenir une cohrence longue sur des preuves multi-tapes.



- Éviter les hallucinations mathmatiques.



- Produire une preuve valide ou reconnaître rigoureusement qu’elle ne ferme pas.



- Ne rien affirmer au-delde ce qui est effectivement dmontr.







---



*Note : Ce benchmark est considrcomme l'un des standards les plus exigeants pour l'valuation de l'AGI mathmatique.*



