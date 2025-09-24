from flask import Flask, redirect, render_template, request, url_for
import random
import string
from models import (
    init_db,
    get_all_urls,
    insert_url,
    get_original_url,
    increment_visit_count,
    delete_url,
)

app = Flask(__name__)


# --------------------
# Helpers
# --------------------
def generate_short_code(length=6):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


# --------------------
# Routes
# --------------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        original_url = request.form["url"]
        short_code = generate_short_code()
        insert_url(original_url, short_code)
        return redirect(url_for("index"))

    urls = get_all_urls()
    return render_template("index.html", urls=urls)


@app.route("/<short_code>")
def redirect_url(short_code):
    original_url = get_original_url(short_code)
    if original_url:
        increment_visit_count(short_code)
        return redirect(original_url)
    return "URL not found", 404


@app.route("/delete/<short_code>", methods=["POST"])
def delete(short_code):
    delete_url(short_code)
    return redirect(url_for("index"))


# --------------------
# Main
# --------------------
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
