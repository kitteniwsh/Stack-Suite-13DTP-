from flask import render_template
from flask_login import login_required


@login_required
def inventory():
    """Inventory page"""
    return render_template("inventory/inventory.html")
