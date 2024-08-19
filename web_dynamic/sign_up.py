#!/usr/bin/python3
""" sign_up route file """

from . import app_views
from .forms import SignUpForm
from flask import render_template, flash, redirect, url_for
from models import storage
from models.user import User
from werkzeug.security import generate_password_hash
import requests

@app_views.route('/sign-up', strict_slashes=False, methods=['GET', 'POST'])
def signup():
    """ sign-up function """
    form = SignUpForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password1 = form.password.data
        
        user = storage.get_user_by_email(User, email=email)
        if user:
            flash("User exists", "error")
            return render_template("sign_up.html", form=form)
        else:
            user_by_username = storage.get_user_by_username(User, username)
            if user_by_username:
                flash("Username already taken", "error")
                return render_template("sign_up.html", form=form)
            else:
                url = "https://www.leeroynyanchwa.tech/api/v1/users"
                data = {
                    "email": email,
                    "username": username,
                    "password": generate_password_hash(password1)
                }
                response = requests.post(url, json=data)
                if response.status_code == 201:
                    flash("Account created", "success")
                    return redirect(url_for("app_views.login"))
    return render_template("sign_up.html", form=form)
