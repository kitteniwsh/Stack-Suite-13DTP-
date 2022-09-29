from flask import Blueprint
from . import views

blueprint = Blueprint("crypto", __name__,
                      template_folder="templates", url_prefix="/tools")
# General cryptography page
blueprint.add_url_rule('/crypto', 'crypto', views.crypto)
