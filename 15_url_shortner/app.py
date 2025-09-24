from flask import Flask
from models import (
    init_db,
    get_all_urls,
    insert_url,
    get_original_url,
    increment_visit_count,
    delete_url,
)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
