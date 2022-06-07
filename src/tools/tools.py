from flask import Blueprint
from .crypto import crypto
from . import views
from .rsa import rsa
blueprint = Blueprint("tools", __name__, template_folder="templates")


blueprint.register_blueprint(rsa.blueprint)

blueprint.register_blueprint(crypto.blueprint)
blueprint.add_url_rule('/tools', 'tools', views.tools)
