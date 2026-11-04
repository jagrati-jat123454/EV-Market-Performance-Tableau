import os
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/health")
def health():
    return jsonify(status="ok", service="EV Market Performance")

@app.get("/api/project")
def project_info():
    return jsonify({
        "name": "EV Market Performance",
        "visualizations": [
            {
                "type": "dashboard",
                "title": "EV Market Performance Dashboard",
                "url": "https://public.tableau.com/views/Dashboard1_17937007105250/Dashboard1"
            },
            {
                "type": "story",
                "title": "EV Market Story",
                "url": "https://public.tableau.com/views/EVMARKET-STORY_17937005218180/Story1"
            }
        ]
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
