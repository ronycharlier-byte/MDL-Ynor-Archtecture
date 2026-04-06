﻿# =============================================================================
# COPYRIGHT (c) 2026 CHARLIER RONY - TOUS DROITS RESERVES
# MDL YNOR - AUDIT ACCESS MANAGEMENT (CLI)
# Facilitates NDA submission and Activation Code requests.
# =============================================================================
import os
import sys

def manage_audit_access():
    print("=" * 60)
    print(" ⚛️ MDL YNOR - PROTOCOLE D'ACCÈS AUDITEUR (v2.2.0-PROD)")
    print("=" * 60)
    print("\n[ÉCHELLE DE SÉCURITÉ : DEFCON 5]")
    print("Le subset OPEN (mathmatiques de base) est djaccessible.")
    print("L'accs au cœur AGI (Inno-Active) ncessite une validation.")
    
    print("\n--- PROCÉDURE DE DEMANDE D'ACCÈS ---")
    print("1. [NDA] Tlchargez et signez le Non-Disclosure Agreement (mdl_nda.pdf)")
    print("2. [DOSSIER] Envoyez votre CV/Profil institutionnel (ENS, Poly, MIT...)")
    print("3. [CONTACT] ronycharlier@mdlstrategy.com - Objet: [YNOR-AUDIT-REQ]")
    
    confirm = input("\nConfirmer l'envoi du dossier complet (O/N) : ")
    
    if confirm.lower() == 'o':
        print("\n⏳ [SYSTÈME] Dpôt de dossier enregistr.")
        print("🚩 [INFO] Un Activation Code temporaire vous sera envoyaprs revue.")
        print("-" * 60)
        print("CETTE PROCÉDURE GARANTIT L'IP SHIELD DE L'Coordonnateur Principal de Recherche SUPRÊME.")
        print("-" * 60)
    else:
        print("\n❌ Demande annule. Seul le subset OPEN est autoris.")

if __name__ == "__main__":
    manage_audit_access()
