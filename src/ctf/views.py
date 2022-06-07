from flask import render_template, session, redirect

def ctf():
    try:
        if not session["authed"]:
            return redirect("/authenticate")
    except:
        return redirect("/authenticate")
    return render_template("ctf/ctf.html")
