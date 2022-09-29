from flask import render_template
from flask_login import login_required


@login_required
def ctf():
    """Main crypto page"""
    return render_template("ctf/ctf.html")
