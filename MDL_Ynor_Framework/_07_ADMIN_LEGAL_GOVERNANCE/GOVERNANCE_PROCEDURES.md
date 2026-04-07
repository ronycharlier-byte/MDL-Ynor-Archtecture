---

STATUS: CANONICAL | V11.14.0 | AUDIT: CERTIFIED | FINAL CONSOLIDATED REVIEW / V11.14.0

---

# 🏛️ PROCÉDURES DE GOUVERNANCE & AUDIT (MDL YNOR)

**Version :** 2.3.0-PROD | **Auteurs :** Charlier Rony

---

## 🔒 1. GOUVERNANCE DES SECRETS (VAULT-READY)

MDL Ynor a migrd'une authentification hardcode vers une gestion par variables d'environnement (`.env`).

### 1.1 Rotation des Cls

*   **Rotation des API Keys (LLM) :** Tous les 90 jours ou en cas d'anomalie dissipative ($\mu < 0.2$ persistante).

*   **Rotation du MASTER_AUTH :** À chaque mise jour majeure du manifeste (`mdl_global_knowledge.json`).

## ⚖️ 2. PROTOCOLE D'AUDIT EXTERNE

L'audit est grvia le script `request_audit_access.py`.

### 2.1 Critres Reviewer

*   **Audit Scientifique :** Doit fournir une preuve d'affiliation acadmique (CNRS, INRIA, ENS etc.).

*   **Audit Scurit:** Doit possder une certification (OSCP, CISSP) ou être un partenaire auditeur tier-1.

### 2.2 Accs Reviewer

L'accs est accordvia un **Activation Code** temporaire lil'IP du reviewer.

## 🚩 3. CONFINEMENT DU SYSTÈME (CONFINEMENT-IRL)

Les agents autonomes (`AutonomousIRLYnorAgent`) sont bridés par défaut :

*   `READ_ONLY_MODE = TRUE`

*   Toute tentative d'criture hors sandbox est bloque et consigne dans `mdl_audit_trail.log`.

*   Un humain doit explicitement basculer `MDL_ALLOW_WRITE=TRUE` pour autoriser une mutation structurelle.

---

*Ce document forme la base de la confiance oprationnelle du systme Ynor.*

