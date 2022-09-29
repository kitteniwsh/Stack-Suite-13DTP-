from flask import render_template, send_file


def index():
    """Home page"""
    return render_template("base/index.html")


def favicon():
    return send_file("../static/favicon.ico", mimetype='image/gif')
