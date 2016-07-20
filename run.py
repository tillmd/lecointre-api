# encoding: UTF-8

from flask import Flask, jsonify
import os
from utils import get_menu

app = Flask(__name__)


@app.route("/")
def menu():
    menu = get_menu()
    return jsonify(menu)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
