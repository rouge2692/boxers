from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_cors import CORS
import json
import pandas as pd

from pymongo import MongoClient

# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import text

app = Flask(__name__)

# required authentication
app.secret_key = "super secret string"
# loads config.py to app.config dictionary
app.config.from_object("config")

db = MongoClient(app.config["MONGODB_SETTINGS"]).get_database("SweepNoDB")

# login_manager = LoginManager()
# login_manager.init_app(app)

CORS(app)


@app.route("/", methods=["GET"])
def homePage():
    return render_template("index.html")


from app import models
