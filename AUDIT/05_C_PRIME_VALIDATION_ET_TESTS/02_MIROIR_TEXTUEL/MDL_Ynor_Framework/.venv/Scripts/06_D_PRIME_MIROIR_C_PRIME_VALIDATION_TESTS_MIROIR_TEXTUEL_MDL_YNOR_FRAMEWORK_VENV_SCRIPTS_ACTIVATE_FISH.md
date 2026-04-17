> **[◬] MATRICE FRACTALE MDL YNOR V2.0**
> **Corpus :** MDL YNOR
> **Passe de correction :** 2026-04-16
> **Position Structurelle :** NODE
> **Position Chiastique :** D'
> **Role du Fichier :** Surface miroir et symetrie locale
> **Centre Doctrinal Local :** boucle locale de reflet et de coherence
> **Loi de Survie :** μ = α - β - κ
> **Lecture Locale :**
> - **α :** coherence reflexive et effet miroir
> - **β :** derive de boucle et bruit de reflet
> - **κ :** cout de cycle et de stabilisation
> **Risque :** e∞ ∝ ε / μ
> **Operateur Correctif :** D(S)=proj_{SafeDomain}(S)
> **Axiome :** un systeme survit SSI μ > 0
> **Doctrine Goodhart :** tout succes apparent est invalide si μ decroit
> **Gouvernance :** toute modification doit maximiser Δμ
> **Lien Miroir :** D / 03_C_MOTEURS_ET_DEPLOIEMENT
# MIROIR TEXTUEL - activate.fish

Source : MDL_Ynor_Framework\.venv\Scripts\activate.fish
Taille : 4264 octets
SHA256 : 7f239c38340c7151ec7c075b850e9c4e570a73f6db099d89e8ac4e8f243f9b31

```text
# Copyright (c) 2020-202x The virtualenv developers
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# This file must be used using `source bin/activate.fish` *within a running fish ( http://fishshell.com ) session*.
# Do not run it directly.

function _bashify_path -d "Converts a fish path to something bash can recognize"
 set fishy_path $argv
 set bashy_path $fishy_path[1]
 for path_part in $fishy_path[2..-1]
 set bashy_path "$bashy_path:$path_part"
 end
 echo $bashy_path
end

function _fishify_path -d "Converts a bash path to something fish can recognize"
 echo $argv | tr ':' '\n'
end

function deactivate -d 'Exit virtualenv mode and return to the normal environment.'
 # reset old environment variables
 if test -n "$_OLD_VIRTUAL_PATH"
 # https://github.com/fish-shell/fish-shell/issues/436 altered PATH handling
 if test (string sub -s 1 -l 1 $FISH_VERSION) -lt 3
 set -gx PATH (_fishify_path "$_OLD_VIRTUAL_PATH")
 else
 set -gx PATH $_OLD_VIRTUAL_PATH
 end
 set -e _OLD_VIRTUAL_PATH
 end

 if test -n "$_OLD_VIRTUAL_PYTHONHOME"
 set -gx PYTHONHOME "$_OLD_VIRTUAL_PYTHONHOME"
 set -e _OLD_VIRTUAL_PYTHONHOME
 end

 if test -n "$_OLD_FISH_PROMPT_OVERRIDE"
 and functions -q _old_fish_prompt
 # Set an empty local `$fish_function_path` to allow the removal of `fish_prompt` using `functions -e`.
 set -l fish_function_path

 # Erase virtualenv's `fish_prompt` and restore the original.
 functions -e fish_prompt
 functions -c _old_fish_prompt fish_prompt
 functions -e _old_fish_prompt
 set -e _OLD_FISH_PROMPT_OVERRIDE
 end

 set -e VIRTUAL_ENV
 set -e VIRTUAL_ENV_PROMPT

 if test "$argv[1]" != 'nondestructive'
 # Self-destruct!
 functions -e pydoc
 functions -e deactivate
 functions -e _bashify_path
 functions -e _fishify_path
 end
end

# Unset irrelevant variables.
deactivate nondestructive

set -gx VIRTUAL_ENV 'C:\Users\ronyc\Desktop\MDL Ynor Architecture\MDL_Ynor_Framework\.venv'

# https://github.com/fish-shell/fish-shell/issues/436 altered PATH handling
if test (string sub -s 1 -l 1 $FISH_VERSION) -lt 3
 set -gx _OLD_VIRTUAL_PATH (_bashify_path $PATH)
else
 set -gx _OLD_VIRTUAL_PATH $PATH
end
set -gx PATH "$VIRTUAL_ENV"'/Scripts' $PATH

# Prompt override provided?
# If not, just use the environment name.
if test -n 'mdl-ynor-framework'
 set -gx VIRTUAL_ENV_PROMPT 'mdl-ynor-framework'
else
 set -gx VIRTUAL_ENV_PROMPT (basename "$VIRTUAL_ENV")
end

# Unset `$PYTHONHOME` if set.
if set -q PYTHONHOME
 set -gx _OLD_VIRTUAL_PYTHONHOME $PYTHONHOME
 set -e PYTHONHOME
end

function pydoc
 python -m pydoc $argv
end

if test -z "$VIRTUAL_ENV_DISABLE_PROMPT"
 # Copy the current `fish_prompt` function as `_old_fish_prompt`.
 functions -c fish_prompt _old_fish_prompt

 function fish_prompt
 # Run the user's prompt first; it might depend on (pipe)status.
 set -l prompt (_old_fish_prompt)

 printf '(%s) ' $VIRTUAL_ENV_PROMPT

 string join -- \n $prompt # handle multi-line prompts
 end

 set -gx _OLD_FISH_PROMPT_OVERRIDE "$VIRTUAL_ENV"
end

```

---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
