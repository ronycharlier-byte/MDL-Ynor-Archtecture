---
**Système MDL Ynor - Validation Continue**
**Date de révision** : 2026-04-09
**Status: Science-Ready [10/10]**
---

# MIROIR TEXTUEL - activate.bat

Source : MDL_Ynor_Framework\.venv\Scripts\activate.bat
Taille : 2724 octets
SHA256 : 831df39df1c765b819ff49153be5ed37841fb562d0d3cced23b9c359980ec2c2

```text
@REM Copyright (c) 2020-202x The virtualenv developers
@REM
@REM Permission is hereby granted, free of charge, to any person obtaining
@REM a copy of this software and associated documentation files (the
@REM "Software"), to deal in the Software without restriction, including
@REM without limitation the rights to use, copy, modify, merge, publish,
@REM distribute, sublicense, and/or sell copies of the Software, and to
@REM permit persons to whom the Software is furnished to do so, subject to
@REM the following conditions:
@REM
@REM The above copyright notice and this permission notice shall be
@REM included in all copies or substantial portions of the Software.
@REM
@REM THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
@REM EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
@REM MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
@REM NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
@REM LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
@REM OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
@REM WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

@REM This file is UTF-8 encoded, so we need to update the current code page while executing it
@for /f "tokens=2 delims=:." %%a in ('"%SystemRoot%\System32\chcp.com"') do @set _OLD_CODEPAGE=%%a

@if defined _OLD_CODEPAGE (
 "%SystemRoot%\System32\chcp.com" 65001 > nul
)

@for %%i in ("C:\Users\ronyc\Desktop\MDL Ynor Architecture\MDL_Ynor_Framework\.venv") do @set "VIRTUAL_ENV=%%~fi"

@set "VIRTUAL_ENV_PROMPT=mdl-ynor-framework"
@if NOT DEFINED VIRTUAL_ENV_PROMPT (
 @for %%d in ("%VIRTUAL_ENV%") do @set "VIRTUAL_ENV_PROMPT=%%~nxd"
)

@if defined _OLD_VIRTUAL_PROMPT (
 @set "PROMPT=%_OLD_VIRTUAL_PROMPT%"
) else (
 @if not defined PROMPT (
 @set "PROMPT=$P$G"
 )
 @if not defined VIRTUAL_ENV_DISABLE_PROMPT (
 @set "_OLD_VIRTUAL_PROMPT=%PROMPT%"
 )
)
@if not defined VIRTUAL_ENV_DISABLE_PROMPT (
 @set "PROMPT=(%VIRTUAL_ENV_PROMPT%) %PROMPT%"
)

@REM Don't use () to avoid problems with them in %PATH%
@if defined _OLD_VIRTUAL_PYTHONHOME @goto ENDIFVHOME
 @set "_OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%"
:ENDIFVHOME

@set PYTHONHOME=

@REM if defined _OLD_VIRTUAL_PATH (
@if not defined _OLD_VIRTUAL_PATH @goto ENDIFVPATH1
 @set "PATH=%_OLD_VIRTUAL_PATH%"
:ENDIFVPATH1
@REM ) else (
@if defined _OLD_VIRTUAL_PATH @goto ENDIFVPATH2
 @set "_OLD_VIRTUAL_PATH=%PATH%"
:ENDIFVPATH2

@set "PATH=%VIRTUAL_ENV%\Scripts;%PATH%"

@if defined _OLD_CODEPAGE (
 "%SystemRoot%\System32\chcp.com" %_OLD_CODEPAGE% > nul
 @set _OLD_CODEPAGE=
)

```

---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
