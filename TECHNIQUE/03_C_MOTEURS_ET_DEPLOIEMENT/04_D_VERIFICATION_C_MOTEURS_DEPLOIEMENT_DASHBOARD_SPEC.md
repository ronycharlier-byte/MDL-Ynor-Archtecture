> **[◬] MATRICE FRACTALE MDL YNOR V2.0**
> **Corpus :** MDL YNOR
> **Passe de correction :** 2026-04-16
> **Position Structurelle :** LAYER
> **Position Chiastique :** D
> **Role du Fichier :** Specification du tableau de bord de supervision
> **Centre Doctrinal Local :** lecture des signaux, metriques et alertes
> **Loi de Survie :** μ = α - β - κ
> **Lecture Locale :**
> - **α :** lecture des signaux, metriques et alertes
> - **β :** surcharge visuelle
> - **κ :** cout d attention
> **Risque :** e∞ ∝ ε / μ
> **Operateur Correctif :** D(S)=proj_{SafeDomain}(S)
> **Axiome :** un systeme survit SSI μ > 0
> **Doctrine Goodhart :** tout succes apparent est invalide si μ decroit
> **Gouvernance :** toute modification doit maximiser Δμ
> **Lien Miroir :** D' / 05_C_PRIME_VALIDATION_ET_TESTS
---



STATUS: CANONICAL | V11.13.0 | SOURCE: UNIFIED | 



AUDIT: CERTIFIED 2026-04-06



---



# DASHBOARD SPEC







## But



Documenter les surfaces d affichage de `C` afin que le pilotage soit coherent entre l API, le terminal utilisateur et le monitor de viabilite.







## Surfaces Existantes



### Dashboard API natif



- route: `/dashboard`



- rendu HTML genere par `ynor_api_server.py`



- usage: supervision legere et acces humain rapide







### Terminal utilisateur



- fichier: `streamlit_dashboard.py`



- usage: envoi d une requete a `/run`



- affichage: outil utilise, reponse retour environnement, mu et systeme







### Audit mu interactif



- fichier: `app.py`



- usage: comparaison d une baseline LLM et d une execution protegee



- affichage: cout, gain, courbe mu, auto-learning bridge







### Monitor HTML FastAPI



- fichier: `ynor_dashboard_v2.py`



- usage: visualisation de session, courbe mu, logs, rafraichissement periodique



- port observe: `8493`







## Experience Utilisateur Visee



- voir si le moteur est vivant



- voir si la viabilite est bonne



- voir si la requete est coupee a temps



- voir si les logs et l auto-apprentissage sont alimentes







## Blocs Informationnels Attendus



- statut du moteur



- indice mu



- activite des systemes 1 et 2



- historique des appels



- traces de logs recents



- couts ou economies si le dashboard les calcule







## Regles De Presentation



- fond sombre ou contraste



- typographie lisible



- indicateurs numeriques visibles en premier



- couleur positive pour la stabilite



- couleur d alerte pour la divergence







## Regles De Comportement



- le dashboard ne doit pas presenter les émergence



- les donnees sensibles doivent etre masquees



- l auto-refresh ne doit pas saturer le moteur



- le dashboard doit rester utile meme si le backend est partiellement degrade







## Priorite De Construction



1. rendre l etat du moteur lisible



2. rendre la viabilite mu lisible



3. rendre les appels et logs lisibles



4. rendre les ecritures et partages optionnels





---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
