import hashlib
import json
from datetime import datetime

JOURNAL_PATH = "05_C_PRIME_VALIDATION_ET_TESTS/JOURNAL_DE_REPRODUCTIBILITE.md"
SIGNATURE_PATH = "05_C_PRIME_VALIDATION_ET_TESTS/JOURNAL_SIGNATURE.json"

def sign_journal():
    if not os.path.exists(JOURNAL_PATH):
        print(f"Erreur : {JOURNAL_PATH} introuvable.")
        return

    with open(JOURNAL_PATH, "rb") as f:
        file_data = f.read()
        file_hash = hashlib.sha256(file_data).hexdigest()

    signature = {
        "timestamp": str(datetime.now()),
        "file": JOURNAL_PATH,
        "sha256": file_hash,
        "status": "IMMUTABLE_CLAIM_SIGNED",
        "signer": "MDL YNOR ENGINE V11.13"
    }

    with open(SIGNATURE_PATH, "w") as f:
        json.dump(signature, f, indent=4)

    print(f"Journal signé avec succès : {file_hash}")

import os
if __name__ == "__main__":
    sign_journal()
