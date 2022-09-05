from flask import Flask
from base import base
from auth import auth
from ctf import ctf
import dotenv, os

dotenv.load_dotenv("../src/.env")

if "SECRET" not in os.environ:
    raise Exception("SECRET enviroment variable not found.")

app = Flask(__name__, static_folder="../static")

app.config["SECRET_KEY"] = os.environ["SECRET"]

app.register_blueprint(base.blueprint)
app.register_blueprint(ctf.blueprint)
app.register_blueprint(auth.blueprint)

if __name__ == "__main__":
    app.run()
