"""Models and database functions for gechur project."""

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()

app = Flask(__name__)

class User(db.Model):
    """User of the gechur website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Items(db.Model):
    """Items the user has put into the website"""

    __tablename__ = "items"

    item_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    item_name = db.Column(db.String(64), nullable=False)
    cost_of_item = db.Column(db.Integer, nullable=False)
    hours_to_use = db.Column(db.Integer, nullable=False)
    hours_used = db.Column(db.Integer, nullable=False)
    completed = db.Column(db.Boolean)
    given_away = db.Column(db.Boolean)
    description = db.Column(db.Text, nullable=True)


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nathanwood:asdf@localhost:5432/gechur'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    connect_to_db(app)
    print("Connected to DB.")