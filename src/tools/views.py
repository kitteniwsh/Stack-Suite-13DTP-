from flask import render_template, redirect, session
from flask_login import login_required

@login_required
def tools():

    return render_template("tools/tools.html")
