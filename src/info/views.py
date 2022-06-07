from flask import render_template, session, redirect

def info():
    return render_template("info/info.html")
