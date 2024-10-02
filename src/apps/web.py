# src/apps/web.py
from flask import Flask, jsonify, render_template, request

from src.btg.progress import ProgressTracker
from src.config import Config

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def web_form():
    if request.method == "POST":
        txid = request.form.get("txid")
        start_time = request.form.get("start_time")
        confirmation_target = request.form.get(
            "confirmation_target", Config.CONFIRMATION_TARGET
        )

        tracker = ProgressTracker()
        return jsonify(
            tracker.track_web_progress(txid, start_time, confirmation_target)
        )

    return render_template("form.html")


@app.route("/tailwind", methods=["GET", "POST"])
def web_form_tailwind():
    if request.method == "POST":
        txid = request.form.get("txid")
        start_time = request.form.get("start_time")
        confirmation_target = request.form.get(
            "confirmation_target", Config.CONFIRMATION_TARGET
        )

        tracker = ProgressTracker()
        return jsonify(
            tracker.track_web_progress(txid, start_time, confirmation_target)
        )

    return render_template("form-tailwind.html")


def run_web():
    app.run(debug=True)
