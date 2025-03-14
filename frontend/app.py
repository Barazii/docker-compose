# frontend/app.py
from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

# Define the backend API URL
API_URL = os.environ["API_URL"]


@app.route("/")
def index():
    response = requests.get(API_URL)
    if response.status_code == 200:
        items = response.json()
        return render_template("index.html", items=items)
    else:
        return "Error fetching items from backend"


if __name__ == "__main__":
    app.run(debug=True, port=8000)
