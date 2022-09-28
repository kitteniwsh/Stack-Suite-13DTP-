from flask import render_template, session, redirect
from flask_login import login_required


@login_required
def ctf():
    return render_template("ctf/ctf.html")
