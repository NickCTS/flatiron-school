# Phase 4: Fundamentals
# by Sakib Rasul

# Core Deliverables
# 1. Install Flask.
# 2. Configure a new Flask application.
# 3. Write an index route.
# 4. Test the route.
# 5. Install Flask-SQLAlchemy and Flask-Migrate.
# 6. Create and populate a new database.
# 7. Write a route that interacts with the database.
# 8. Test the route.

from flask import Flask, jsonify
from flask_sqlalchemy import SqlAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify({"message": "Hello!"})