from flask import Flask, jsonify, send_from_directory
import json
import os
import glob
from datetime import datetime

# =================================================================================
# MDL YNOR - MU-VIEW DASHBOARD SERVER (V1.0)
# Serveur d'observabilité passive pour Phase 2
# =================================================================================

app = Flask(__name__)

def get_latest_log_file():
    logs = glob.glob("ynor_passive_audit_log_*.jsonl")
    if not logs: return None
    return max(logs, key=os.path.getctime)

@app.route('/api/stats')
def get_stats():
    log_file = get_latest_log_file()
    if not log_file: return jsonify({"error": "No logs found"})
    
    data = []
    with open(log_file, "r") as f:
        for line in f:
            data.append(json.loads(line))
    
    if len(data) == 0: return jsonify({"error": "Empty log"})

    # On prend les 100 derniers points pour le dashboard
    recent = data[-100:]
    
    # Calcul epsilon_q_real (glissant)
    validated = [d for d in data if d.get('validated') and d.get('psi') != 0]
    epsilon_q = 1.0 - (sum([1 for d in validated if d['correct']]) / len(validated)) if validated else 0.0
    
    # Distribution des Régimes
    regimes = {"Accumulation (psi=1)": 0, "Distribution (psi=-1)": 0, "Neutre (psi=0)": 0}
    for d in data[-500:]:
        if d['psi'] == 1: regimes["Accumulation (psi=1)"] += 1
        elif d['psi'] == -1: regimes["Distribution (psi=-1)"] += 1
        else: regimes["Neutre (psi=0)"] += 1
    
    return jsonify({
        "current": recent[-1],
        "history": recent,
        "epsilon_q": round(epsilon_q, 4),
        "regimes": regimes,
        "total_scans": len(data),
        "log_file": log_file
    })

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == "__main__":
    # On lance sur le port 5000 par défaut
    app.run(host='0.0.0.0', port=5000, debug=False)
