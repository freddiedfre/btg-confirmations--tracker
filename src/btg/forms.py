# src/btg/forms.py
import logging

import requests

from src.config import Config


@app.route("/", methods=["GET", "POST"])
def form(html_type="default"):
    if request.method == "POST":
        txid = request.form["txid"]
        start_time = request.form.get("start_time", "")
        confirmation_target = request.form.get("confirmation_target", 300)
        ProgressTracker.track_progress(txid, start_time, confirmation_target)
    if html_type == "tailwind":
        return render_template("form-tailwind.html")
    return render_template("form.html")
