from flask import render_template, session, redirect, Flask, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
import sys
from models.extensions import db, User, Prime, Composite, t_Primes_Composites
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user






class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])


def authenticate():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                if(user.perms):
                    login_user(user, remember=form.remember.data)
                    return redirect('/')
                else:
                    if(user.checked):
                        return render_template('/auth/auth.html', form=form, lg= "Your account was not verified. Please contact an administrator for futher inquiries.")
                    else:
                        return render_template('/auth/auth.html', form=form, lg= "Your account is still being verified. Please try again later!")


        return render_template('/auth/auth.html', form=form, lg= "Incorrect username or password")
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('/auth/auth.html', form=form)


def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password, perms = 0, checked = False)
        db.session.add(new_user)
        db.session.commit()

        return redirect('/authenticate')
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('/auth/Nauth.html', form=form)


@login_required
def endsession():
    logout_user()
    return redirect('/')
