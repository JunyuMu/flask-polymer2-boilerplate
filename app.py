# -*- coding: utf-8 -*-
import os

from flask import Flask, current_app

static_folder_path = "static/build/es5-bundled" if os.getenv("FLASK_ENV") == "production" else "static"

app = Flask(__name__, static_folder=static_folder_path)

@app.route("/static/<path:path>")
def static_c(path):
    return current_app.send_static_file(path)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return current_app.send_static_file("index.html")

if __name__ == "__main__":
    app.run()
