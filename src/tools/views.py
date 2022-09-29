from flask import render_template
from flask_login import login_required


@login_required
def tools():
    """Tools page"""
    return render_template("tools/tools.html")
