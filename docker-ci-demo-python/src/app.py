import os
from datetime import datetime, timezone
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok"), 200


@app.get("/")
def index():
    return jsonify(
        message="Hello from Python Docker CI Demo!",
        timestamp=datetime.now(timezone.utc).isoformat(),
        version=os.getenv("APP_VERSION", "1.0.0"),
    ), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", 3000))
    app.run(host="0.0.0.0", port=port)