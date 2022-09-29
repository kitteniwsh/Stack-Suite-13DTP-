from flask import render_template


def about():
    """About page"""
    return render_template("about/about.html")
