import os
import re

ROOT_DIR = r"c:\Users\ronyc\Desktop\MDL Ynor"

REPLACEMENTS = [
 # Emojis marketing frequents dans les titres
 (r'|||||||||||', ''), 
 
 # Vocabulaire non-scientifique ou sur-prometteur -> Vocabulaire academique
 (r'(?i)\b(rigoureux|rigoureux)\b', 'rigoureux'),
 (r'(?i)\b(significatif|significatif)\b', 'significatif'),
 (r'(?i)\b(formel|formel)\b', 'formel'),
 (r'(?i)\b(déterministe|déterministe)\b', 'déterministe'),
 (r'(?i)\b(innovant|innovant)\b', 'innovant'),
 (r'(?i)\b(cash[- ]?machine)\b', 'générateur de liquidité'),
 (r'(?i)\b(majeur|majeur|majeur|majeur)\b', 'majeur'),
 (r'(?i)\b(notable|notable)\b', 'notable'),
 (r'(?i)\b(remarquable|remarquable|remarquable|remarquable|remarquable|remarquable)\b', 'remarquable'),
 (r'(?i)\b(pertinent|pertinent|pertinent)\b', 'pertinent'),
 (r'(?i)\b(garanti à 100%|statistiquement robuste)\b', 'statistiquement robuste'),
 (r'(?i)\b(les fondements de|les fondements de)\b', 'les fondements de'),
 (r'(?i)\b(optimisation|optimisation)\b', 'optimisation'),
 (r'(?i)\b(rendement optimisé)\b', 'rendement optimisé'),
 (r'(?i)\b(l\'le modèle canonique|le modèle canonique)\b', 'le modèle canonique'),
 (r'(?i)\b(la convergence)\b', 'la convergence'),
 
 # Exclamations multiples (ex: ! -> !)
 (r'!{2,}', '!'),
 
 # Nettoyage cosmetique
 (r' +', ' ') # espaces multiples crees par la suppression des emojis
]

def sanitize_file(filepath):
 try:
 with open(filepath, 'r', encoding='utf-8') as f:
 content = f.read()
 except Exception as e:
 # Ignore les fichiers non-utf8 (ex: pdf, binaires)
 return False
 
 original = content
 for pattern, repl in REPLACEMENTS:
 content = re.sub(pattern, repl, content)
 
 if original != content:
 with open(filepath, 'w', encoding='utf-8') as f:
 f.write(content)
 return True
 return False

def main():
 updated_files = 0
 for root, dirs, files in os.walk(ROOT_DIR):
 # Exclure .git
 if '.git' in root or '.obsidian' in root:
 continue
 
 for file in files:
 if file.endswith(('.md', '.txt', '.tex', '.json', '.py')):
 filepath = os.path.join(root, file)
 if sanitize_file(filepath):
 updated_files += 1

 print(f"Termine. {updated_files} fichiers ont ete nettoyes et standardises au format academique.")

if __name__ == '__main__':
 main()
