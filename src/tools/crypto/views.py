from flask import render_template, session, redirect
from flask_login import login_required

@login_required
def crypto():

    return render_template("crypto/crypto.html")
