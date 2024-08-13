#!/usr/bin/python3
""" login route for mingle """
from . import app_views
from .forms import LoginForm
from flask import render_template, redirect, url_for, flash
from models import storage
from models.user import User
from werkzeug.security import check_password_hash
from flask_login import login_user

@app_views.route('/login', strict_slashes=False, methods=['GET', 'POST'])
def login():
    """ login function """
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        user = storage.get_user_by_email(User, email=email)
        if user:
            if check_password_hash(user.password, password):
                flash("Login successful.", "success")
                login_user(user, remember=True)
                return redirect(url_for("mingle"))
            else:
                flash("Wrong password", "error")
                return redirect(url_for("app_views.login"))
        else:
            flash("No user with this email", "error")
            return redirect(url_for("app_views.login"))
    return render_template("login.html", form=form)
