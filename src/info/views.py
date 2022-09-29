from flask import render_template


def info():
    """Info page"""
    return render_template("info/info.html")
