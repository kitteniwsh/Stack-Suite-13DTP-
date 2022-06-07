from flask import render_template, session, redirect

def crypto():
    if not session["authed"]:
        return redirect("/authenticate")
    return render_template("crypto/crypto.html")
