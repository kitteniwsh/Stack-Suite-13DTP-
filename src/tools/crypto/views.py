from flask import render_template
from flask_login import login_required


@login_required
def crypto():
    """General cryptography page"""
    return render_template("crypto/crypto.html")
