from flask import Blueprint, render_template
from . import views

blueprint = Blueprint("base", __name__, template_folder="templates")

# Home page
blueprint.add_url_rule('/', 'index', views.index)
blueprint.add_url_rule('/favicon.ico', 'favicon', views.favicon)


@blueprint.app_errorhandler(404)
def error_404(error):
    """Returns a 404 error"""
    return render_template("error_404.html")
