from flask import render_template, send_file, redirect, request, session, url_for
import os, dotenv

dotenv.load_dotenv("../src/.env")

if "AUTH_TOKEN" not in os.environ:
    raise Exception("AUTH_TOKEN enviroment variable not found.")

auth_token = os.environ["AUTH_TOKEN"]



def authenticate(page):
    if(session["authed"]):
        lg = "Authenticated!"
    else:
        lg = "Unauthorized." 
    if request.method == "GET":
        return render_template("auth/auth.html", logged = lg)
    
    if request.method == "POST":
        creds = request.form
        if "token" not in creds:
            return "Insufficient Credentials"
        if creds["token"] == auth_token:
            session["authed"] = True
            lg = "Authenticated!"
            return redirect(url_for(page))
        else:
            return render_template("auth/auth.html", success="Incorrect token.", logged = lg)

def endsession():
    session["authed"] = False
    return redirect("/authenticate/gg")
