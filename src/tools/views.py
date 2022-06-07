from flask import render_template, redirect, session

def tools():
    if not session["authed"]:
        return redirect("/authenticate")
    return render_template("tools/tools.html")
