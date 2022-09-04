from flask_sqlalchemy import SQLAlchemy 
from flask_login import UserMixin
from sqlalchemy.ext.automap import automap_base

db = SQLAlchemy()
db.metadata.clear()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(90))
    perms = db.Column(db.Integer)
    checked = db.Column(db.Boolean)


class Composite(db.Model):
    __tablename__ = 'Composite'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.BigInteger)

    Primes = db.relationship('Prime', secondary='Primes_Composites', backref='composites')



class Prime(db.Model):
    __tablename__ = 'Primes'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.BigInteger)



t_Primes_Composites = db.Table(
    'Primes_Composites',
    db.Column('cid', db.ForeignKey('Composite.id')),
    db.Column('pid', db.ForeignKey('Primes.id'))
)