from flask import Flask
from base import base
from auth import auth
from ctf import ctf
from tools import tools
from about import about
from info import info
from inventory import inventory
import dotenv, os
from flask_sqlalchemy import SQLAlchemy
from models.extensions import db

dotenv.load_dotenv("../src/.env")

if "SECRET" not in os.environ:
    raise Exception("SECRET enviroment variable not found.")

app = Flask(__name__, static_folder="../static")
from flask_bootstrap import Bootstrap

app.config["SECRET_KEY"] = os.environ["SECRET"]
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
bootstrap = Bootstrap(app)
db.init_app(app)


app.register_blueprint(base.blueprint)
app.register_blueprint(ctf.blueprint)
app.register_blueprint(auth.blueprint)
app.register_blueprint(tools.blueprint)
app.register_blueprint(info.blueprint)
app.register_blueprint(about.blueprint)
app.register_blueprint(inventory.blueprint)

if __name__ == "__main__":
    app.run(debug=True)
    pass
