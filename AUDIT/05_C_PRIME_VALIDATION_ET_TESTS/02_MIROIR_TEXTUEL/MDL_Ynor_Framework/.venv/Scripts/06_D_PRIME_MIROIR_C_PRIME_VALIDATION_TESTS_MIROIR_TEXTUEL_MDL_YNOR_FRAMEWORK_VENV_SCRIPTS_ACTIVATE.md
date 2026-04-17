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
# MIROIR TEXTUEL - activate

Source : MDL_Ynor_Framework\.venv\Scripts\activate
Taille : 4162 octets
SHA256 : 13271b5f80d7ba679e949c1ea6ff0c2104991e9a04d6d8ec95f107ca22e5593d

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

# This file must be used with "source bin/activate" *from bash*
# you cannot run it directly

if ! [ -z "${SCRIPT_PATH+_}" ] ; then
 _OLD_SCRIPT_PATH="$SCRIPT_PATH"
fi

# Get script path (only used if environment is relocatable).
if [ -n "${BASH_VERSION:+x}" ] ; then
 SCRIPT_PATH="${BASH_SOURCE[0]}"
 if [ "$SCRIPT_PATH" = "$0" ]; then
 # Only bash has a reasonably robust check for source'dness.
 echo "You must source this script: \$ source $0" >&2
 exit 33
 fi
elif [ -n "${ZSH_VERSION:+x}" ] ; then
 SCRIPT_PATH="${(%):-%x}"
elif [ -n "${KSH_VERSION:+x}" ] ; then
 SCRIPT_PATH="${.sh.file}"
fi

deactivate () {
 unset -f pydoc >/dev/null 2>&1 || true

 # reset old environment variables
 # ! [ -z ${VAR+_} ] returns true if VAR is declared at all
 if ! [ -z "${_OLD_VIRTUAL_PATH:+_}" ] ; then
 PATH="$_OLD_VIRTUAL_PATH"
 export PATH
 unset _OLD_VIRTUAL_PATH
 fi
 if ! [ -z "${_OLD_VIRTUAL_PYTHONHOME+_}" ] ; then
 PYTHONHOME="$_OLD_VIRTUAL_PYTHONHOME"
 export PYTHONHOME
 unset _OLD_VIRTUAL_PYTHONHOME
 fi

 # The hash command must be called to get it to forget past
 # commands. Without forgetting past commands the $PATH changes
 # we made may not be respected
 hash -r 2>/dev/null

 if ! [ -z "${_OLD_VIRTUAL_PS1+_}" ] ; then
 PS1="$_OLD_VIRTUAL_PS1"
 export PS1
 unset _OLD_VIRTUAL_PS1
 fi

 unset VIRTUAL_ENV
 unset VIRTUAL_ENV_PROMPT
 if [ ! "${1-}" = "nondestructive" ] ; then
 # Self destruct!
 unset -f deactivate
 fi
}

# unset irrelevant variables
deactivate nondestructive

VIRTUAL_ENV='C:\Users\ronyc\Desktop\MDL Ynor Architecture\MDL_Ynor_Framework\.venv'
if ([ "$OSTYPE" = "cygwin" ] || [ "$OSTYPE" = "msys" ]) && $(command -v cygpath &> /dev/null) ; then
 VIRTUAL_ENV=$(cygpath -u "$VIRTUAL_ENV")
fi
export VIRTUAL_ENV

# Unset the `SCRIPT_PATH` variable, now that the `VIRTUAL_ENV` variable
# has been set. This is important for relocatable environments.
if ! [ -z "${_OLD_SCRIPT_PATH+_}" ] ; then
 SCRIPT_PATH="$_OLD_SCRIPT_PATH"
 export SCRIPT_PATH
 unset _OLD_SCRIPT_PATH
else
 unset SCRIPT_PATH
fi

_OLD_VIRTUAL_PATH="$PATH"
PATH="$VIRTUAL_ENV/Scripts:$PATH"
export PATH

if [ "xmdl-ynor-framework" != x ] ; then
 VIRTUAL_ENV_PROMPT="mdl-ynor-framework"
else
 VIRTUAL_ENV_PROMPT=$(basename "$VIRTUAL_ENV")
fi
export VIRTUAL_ENV_PROMPT

# unset PYTHONHOME if set
if ! [ -z "${PYTHONHOME+_}" ] ; then
 _OLD_VIRTUAL_PYTHONHOME="$PYTHONHOME"
 unset PYTHONHOME
fi

if [ -z "${VIRTUAL_ENV_DISABLE_PROMPT-}" ] ; then
 _OLD_VIRTUAL_PS1="${PS1-}"
 PS1="(${VIRTUAL_ENV_PROMPT}) ${PS1-}"
 export PS1
fi

# Make sure to unalias pydoc if it's already there
alias pydoc 2>/dev/null >/dev/null && unalias pydoc || true

pydoc () {
 python -m pydoc "$@"
}

# The hash command must be called to get it to forget past
# commands. Without forgetting past commands the $PATH changes
# we made may not be respected
hash -r 2>/dev/null || true

```

---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
