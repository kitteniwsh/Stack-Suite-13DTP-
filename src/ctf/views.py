from flask import render_template, session, redirect

def ctf():
    if not session["authed"]:
        return redirect("/authenticate")
    return render_template("ctf/ctf.html")
