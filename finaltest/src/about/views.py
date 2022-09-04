from flask import render_template, session, redirect

def about():
    return render_template("about/about.html")
