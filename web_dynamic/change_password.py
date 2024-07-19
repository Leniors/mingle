#!/usr/bin/python3
""" change password route for mingle """
from . import app_views
from .forms import ChangePasswordForm
from flask import render_template, redirect, url_for, flash
from models import storage
from models.user import User
from werkzeug.security import check_password_hash, generate_password_hash

@app_views.route('/changepassword/<username>', strict_slashes=False, methods=['GET', 'POST'])
def changepassword(username):
    """ changepassword function """
    form = ChangePasswordForm()
    if form.validate_on_submit():
        current_password = form.current_password.data
        new_password = form.new_password.data
        
        
        user = storage.get_user_by_username(User, username)
        if user:
            if check_password_hash(user.password, current_password):
                user.password = generate_password_hash(new_password)
                user.save()
                flash("Pasword changed.", "success")
                return redirect(f"/mingle/profile/{user.username}")
            else:
                flash("Wrong current password", "error")
                return render_template("change_password.html", form=form)
        else:
            flash("No user with this username", "error")
            redirect(url_for("app_views.login"))
    return render_template("change_password.html", form=form)
