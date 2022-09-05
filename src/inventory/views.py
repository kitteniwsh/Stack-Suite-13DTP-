from flask import render_template, session, redirect

def inventory():
    return render_template("inventory/inventory.html")
