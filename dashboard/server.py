import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# --- ROUTES ---

@app.route("/")
def index():
    return "<h1>MDL Ynor V1.6.1 - Sovereign Dashboard</h1><p>Status: ACTIVE (SAFE_MODE)</p>"

@app.route("/api/status")
def status():
    return jsonify({
        "status": "STABLE",
        "mode": "SAFE_MODE",
        "version": "1.6.1"
    })

def run_server():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
