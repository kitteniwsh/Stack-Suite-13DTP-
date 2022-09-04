from flask import Blueprint
from . import views

blueprint = Blueprint("inventory", __name__, template_folder="templates")

blueprint.add_url_rule('/inventory', 'inventory', views.inventory)
