from flask import render_template, send_file, request, session, redirect

def ctf():
    if session["authed"]:
        return render_template("ctf/ctf.html")
    else:
        return redirect("/authenticate/ctf")
