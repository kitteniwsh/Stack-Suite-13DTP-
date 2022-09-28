from flask import render_template, session, redirect
from flask_login import login_required


@login_required
def inventory():
    return render_template("inventory/inventory.html")
