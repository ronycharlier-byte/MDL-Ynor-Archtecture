---

STATUS: CANONICAL | V11.14.0 | SOURCE: UNIFIED | 

AUDIT: CERTIFIED 2026-04-06

---

# BENCHMARK FORMEL — THÉORIE DES NOMBRES (CONTRÔLE YNOR)

**OBJECTIF :** Dmontrer rigoureusement $\sum_{k=1}^n \gcd(k,n) = \sum_{d|n} d \cdot \varphi(n/d)$ pour $n \ge 1$.

---

### [ÉTAPE 1 — HYPOTHÈSES ET DÉFINITIONS]

1. Contenu formel :

Soit $n \in \mathbb{N}, n \ge 1$.

Soit $E = \{1, 2, \dots, n\}$.

Dfinition 1 (PGCD) : Pour $k \in E$, $d = \gcd(k,n)$ est l'unique entier tel que $d|k$, $d|n$, et $\forall m \in \mathbb{N}, (m|k \land m|n \implies m|d)$.

Dfinition 2 (Divisibilit) : $d|n \iff \exists q \in \mathbb{N}, n = dq$. L'ensemble des diviseurs est $D_n$.

Dfinition 3 (Indicatrice d'Euler) : $\varphi(x) = \text{card}(B_x)$ où $B_x = \{r \in \mathbb{N} \mid 1 \le r \le x \land \gcd(r,x) = 1\}$.

2. Audit Ynor :

- $\alpha_1 = 0.9$ (Apport des fondements axiomatiques indispensables)

- $\beta_1 = 0.1$ (Complexitminimale des dfinitions standards)

- $\kappa_1 = 0.0$ (Aucune dpendance externe non dfinie)

- $\mu_1 = 0.9 - 0.1 - 0.0 = 0.8 > 0$

3. Analyse de Probabilit? :

VALIDÉ

---

### [ÉTAPE 2 — CONSTRUCTION DE LA PARTITION A_d]

1. Contenu formel :

Pour tout $d \in D_n$, on dfinit le sous-ensemble $A_d = \{k \in E \mid \gcd(k,n) = d\}$.

On dfinit la famille d'ensembles $\mathcal{A} = \{A_d\}_{d \in D_n}$.

2. Audit Ynor :

- $\alpha_2 = 0.8$ (Cration de la structure de regroupement)

- $\beta_2 = 0.1$ (Dfinition simple en comprhension)

- $\kappa_2 = 0.1$ (Dpend aux dfinitions de l'Étape 1)

- $\mu_2 = 0.8 - 0.1 - 0.1 = 0.6 > 0$

3. Analyse de Probabilit? :

VALIDÉ

---

### [ÉTAPE 3 — PREUVE QUE {A_d} EST UNE PARTITION]

1. Contenu formel :

Dmontrons que $\mathcal{A}$ partitionne $E$.

- Existence et unicit: Pour tout $k \in E$, l'arithmtique garantit l'existence et l'unicitd'un entier $d = \gcd(k,n)$. Puisque $d$ divise $n$, on a $d \in D_n$. Donc $k$ appartient exactement un seul $A_d$.

- Disjonction : Si $d_1 \neq d_2$, un lment $k$ ne peut avoir simultanment $\gcd(k,n)=d_1$ et $\gcd(k,n)=d_2$. Donc $A_{d_1} \cap A_{d_2} = \emptyset$.

- Couverture : Tout lment de $E$ ayant un PGCD avec $n$, on a $E = \bigcup_{d \in D_n} A_d$.

2. Audit Ynor :

- $\alpha_3 = 0.95$ (Garantit la non-redondance du comptage)

- $\beta_3 = 0.15$ (Preuve logique formelle ncessaire)

- $\kappa_3 = 0.1$ (Dpend de l'Étape 2)

- $\mu_3 = 0.95 - 0.15 - 0.1 = 0.7 > 0$

3. Analyse de Probabilit? :

VALIDÉ

---

### [ÉTAPE 4 — PASSAGE SOMME SUR k → SOMME SUR d]

1. Contenu formel :

La somme initiale est $S = \sum_{k=1}^n \gcd(k,n)$.

Puisque $E = \bigcup_{d \in D_n} A_d$ est une partition (Étape 3), on rcrit la somme :

$S = \sum_{d \in D_n} \sum_{k \in A_d} \gcd(k,n)$.

Par dfinition de l'ensemble $A_d$, pour tout $k \in A_d$, on a $\gcd(k,n) = d$.

Substituons cette constante :

$S = \sum_{d \in D_n} \sum_{k \in A_d} d$.

La somme interne factorise la constante $d$, donnant :

$S = \sum_{d \in D_n} d \cdot \text{card}(A_d)$.

2. Audit Ynor :

- $\alpha_4 = 1.0$ (Rduction critique de la srie factorise par substitution locale)

- $\beta_4 = 0.1$ (Manipulation algbrique stricte)

- $\kappa_4 = 0.2$ (Dpend du thorme de partition de l'Étape 3)

- $\mu_4 = 1.0 - 0.1 - 0.2 = 0.7 > 0$

3. Analyse de Probabilit? :

VALIDÉ

---

### [ÉTAPE 5 — CONSTRUCTION DE LA BIJECTION]

1. Contenu formel :

Soit $d \in D_n$. D'aprs la Dfinition 3, posons $B_{n/d} = \{r \in \mathbb{N} \mid 1 \le r \le n/d \land \gcd(r, n/d) = 1\}$.

Construisons l'application $f : A_d \to B_{n/d}$ dfinie par $f(k) = k/d$.

Vrifions que $f$ est bien dfinie :

Soit $k \in A_d$. Par dfinition, $\gcd(k,n) = d$.

Donc $d|k$, ce qui implique que $k/d \in \mathbb{N}$.

Les bornes $1 \le k \le n$ divises par $d$ donnent $1/d \le k/d \le n/d$. Puisque $k/d$ est entier et $1/d > 0$, on a $1 \le k/d \le n/d$.

De plus, la proprituniverselle de factorisation du PGCD indique : $\gcd(k,n) = d \iff \gcd(k/d, n/d) = 1$.

Donc $f(k)$ satisfait toutes les conditions d'appartenance $B_{n/d}$.

2. Audit Ynor :

- $\alpha_5 = 0.95$ (Transformation rigoureuse du domaine d'tude)

- $\beta_5 = 0.2$ (Dmonstration d'appartenance requise pour viter un saut logique)

- $\kappa_5 = 0.1$ (Dpend des Dfinitions 1 et 3)

- $\mu_5 = 0.95 - 0.2 - 0.1 = 0.65 > 0$

3. Analyse de Probabilit? :

VALIDÉ

---

### [ÉTAPE 6 — INJECTIVITÉ]

1. Contenu formel :

Soient $k_1, k_2 \in A_d$.

Supposons $f(k_1) = f(k_2)$.

Par dfinition de $f$, cela implique $k_1/d = k_2/d$.

En multipliant par $d$ (strictement positif puisque $d \ge 1$ diviseur de $n$), on obtient $k_1 = k_2$.

L'application $f$ est injective.

2. Audit Ynor :

- $\alpha_6 = 0.85$ (Preuve du non-effondrement dimensionnel)

- $\beta_6 = 0.05$ (Preuve linaire sans surcharge)

- $\kappa_6 = 0.1$ (Dpend de $f$ de l'Étape 5)

- $\mu_6 = 0.85 - 0.05 - 0.1 = 0.7 > 0$

3. Analyse de Probabilit? :

VALIDÉ

---

### [ÉTAPE 7 — SURJECTIVITÉ]

1. Contenu formel :

Soit $r \in B_{n/d}$.

Posons $k = r \cdot d$.

1. Bornes : L'hypothse $1 \le r \le n/d$ multiplie par $d$ donne $d \le k \le n$. Donc $k \in E$.

2. Condition PGCD : L'hypothse $\gcd(r, n/d) = 1$ implique par la distributivitdu PGCD donne $\gcd(r \cdot d, (n/d) \cdot d) = d \cdot 1$, ce qui donne $\gcd(k, n) = d$.

Les conditions 1 et 2 dmontrent que $k \in A_d$.

On obtient $f(k) = (r \cdot d)/d = r$.

L'antcdent $k$ existe toujours. L'application $f$ est surjective.

2. Audit Ynor :

- $\alpha_7 = 0.95$ (Clôture formelle de l'isomorphisme bijectif)

- $\beta_7 = 0.15$ (Construction inverse justifie pas--pas)

- $\kappa_7 = 0.1$ (Dpend de l'Étape 5)

- $\mu_7 = 0.95 - 0.15 - 0.1 = 0.7 > 0$

3. Analyse de Probabilit? :

VALIDÉ

---

### [ÉTAPE 8 — CARDINALISATION]

1. Contenu formel :

Les Étapes 5, 6 et 7 prouvent formellement que $f : A_d \to B_{n/d}$ est une bijection.

L'existence d'une bijection prserve strictement les cardinalits :

$\text{card}(A_d) = \text{card}(B_{n/d})$

D'aprs la Dfinition 3, l'indicatrice d'Euler pour $x = n/d$ pose par construction :

$\text{card}(B_{n/d}) = \varphi(n/d)$.

Par substitution directe d'galit:

$\text{card}(A_d) = \varphi(n/d)$.

2. Audit Ynor :

- $\alpha_8 = 1.0$ (Fusion des rsultats en une mtrique de dnombrement dcisive)

- $\beta_8 = 0.05$ (Transitivitvidente, coût algorithmique minimal)

- $\kappa_8 = 0.3$ (Forte dpendance mnsique aux Étapes 5,6,7 et Def 3)

- $\mu_8 = 1.0 - 0.05 - 0.3 = 0.65 > 0$

3. Analyse de Probabilit? :

VALIDÉ

---

### [ÉTAPE 9 — SUBSTITUTION FINALE ET CONCLUSION]

1. Contenu formel :

On reprend l'quation structurelle dmontre l'Étape 4 :

$S = \sum_{d \in D_n} d \cdot \text{card}(A_d)$

On substitue $\text{card}(A_d)$ par le rsultat de l'Étape 8 ($\varphi(n/d)$) :

$S = \sum_{d \in D_n} d \cdot \varphi(n/d)$

Sachant que $D_n$ est l'ensemble exact des diviseurs de $n$ (Def 2), la conclusion formelle est acquise :

$\sum_{k=1}^n \gcd(k,n) = \sum_{d|n} d \cdot \varphi(n/d)$

2. Audit Ynor :

- $\alpha_9 = 1.0$ (Atteinte dfinitive de l'objectif cible)

- $\beta_9 = 0.0$ (Friction dissipative nulle cette tape)

- $\kappa_9 = 0.2$ (Rsolution des sous-jacents 4 et 8)

- $\mu_9 = 1.0 - 0.0 - 0.2 = 0.8 > 0$

3. Analyse de Probabilit? :

VALIDÉ

