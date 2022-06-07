from flask import render_template, send_file, redirect, request, session
import os, dotenv

dotenv.load_dotenv("../src/.env")
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField)
from wtforms.validators import InputRequired, Length
from wtforms_validators import  AlphaNumeric

if "AUTH_TOKEN" not in os.environ:
    raise Exception("AUTH_TOKEN enviroment variable not found.")

auth_token = os.environ["AUTH_TOKEN"]
class tokenForm(FlaskForm):
    token = StringField('auth-token', validators=[InputRequired(), Length(min=3, max=20), AlphaNumeric()])

def authenticate():
    
    try:
        if(session["authed"] == True):
            dd = "Authorized"
        else:
            dd = "Unauthorized"
    except:
        dd = "Unauthorized"
    form = tokenForm()
    if request.method == "POST":
        if form.validate_on_submit():
            
            creds = form.token.data

            if creds == auth_token:
                session["authed"] = True
                dd = "Authorized"
                return render_template("auth/auth.html", success="Success!", lg = dd, form=form)
            else:
                return render_template("auth/auth.html", success="Failed, incorrect token", lg = dd, form=form)
        else:
            return render_template("auth/auth.html", success="Failed, malformed input", lg = dd, form=form)
    if request.method == "GET":
        return render_template("auth/auth.html", lg = dd, form=form)
 
def endsession():
    session["authed"] = False
    return redirect("/authenticate")

