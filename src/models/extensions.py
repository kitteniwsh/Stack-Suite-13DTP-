from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db = SQLAlchemy()
db.metadata.clear()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(90))
    perms = db.Column(db.Integer)
    checked = db.Column(db.Boolean)
