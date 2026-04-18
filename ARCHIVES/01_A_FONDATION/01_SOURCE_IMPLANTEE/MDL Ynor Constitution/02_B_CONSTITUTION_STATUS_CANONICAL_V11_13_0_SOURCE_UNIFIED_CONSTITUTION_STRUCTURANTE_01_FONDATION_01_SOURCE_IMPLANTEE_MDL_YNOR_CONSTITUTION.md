> **[◬] MATRICE FRACTALE MDL YNOR V2.0**
> **Corpus :** MDL YNOR
> **Passe de correction :** 2026-04-16
> **Position Structurelle :** MODULE
> **Position Chiastique :** B
> **Role du Fichier :** Constitution structurante
> **Centre Doctrinal Local :** stabilisation locale de la formalisation
> **Loi de Survie :** μ = α - β - κ
> **Lecture Locale :**
> - **α :** coherence formelle et compatibilite
> - **β :** ambiguite semantique et divergence
> - **κ :** cout de demonstration et d integration
> **Risque :** e∞ ∝ ε / μ
> **Operateur Correctif :** D(S)=proj_{SafeDomain}(S)
> **Axiome :** un systeme survit SSI μ > 0
> **Doctrine Goodhart :** tout succes apparent est invalide si μ decroit
> **Gouvernance :** toute modification doit maximiser Δμ
> **Lien Miroir :** B' / 07_A_PRIME_ARCHIVES_ET_RELEASES
---



STATUS: CANONICAL | V11.13.0 | SOURCE: UNIFIED | 



AUDIT: CERTIFIED 2026-04-06



---



# Rebuild des PDFs LaTeX







Ce dossier contient le script PowerShell de reconstruction des PDFs partir des sources `.tex` corriges.







## Prerequis







- Un moteur LaTeX disponible dans le `PATH`



- `latexmk` est prefere, sinon `pdflatex`, `xelatex` ou `lualatex`







## Ordre recommande







1. `P0` : noyau central et textes de reference



2. `P1` : releases majeures et proofs



3. `P2` : miroirs, exports memoire et variantes augmentees







## Commandes utiles







Reconstruire uniquement le noyau prioritaire :







```powershell



.\rebuild_latex_pdfs.ps1 -Priority P0



```







Reconstruire tout le corpus :







```powershell



.\rebuild_latex_pdfs.ps1 -Priority All



```







Forcer un compilateur precis :







```powershell



.\rebuild_latex_pdfs.ps1 -Priority P1 -Compiler pdflatex



```







Limiter le nombre de fichiers pour un test rapide :







```powershell



.\rebuild_latex_pdfs.ps1 -Priority P2 -Limit 3



```







## Notes







- Le script reconstruit les PDFs dans le dossier source de chaque `.tex`.



- Si un fichier source est absent, il est marque `Missing` et le traitement continue.



- L'environnement actuel ne dispose pas d'un compilateur LaTeX, donc le lancement effectif devra se faire sur une machine ou un environnement qui l'expose dans le `PATH`.





---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
