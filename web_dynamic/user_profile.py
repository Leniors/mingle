#!/usr/bin/python3
""" logout route for mingle """
from . import app_views
from flask_login import login_required, current_user
from flask import render_template, redirect, url_for, flash
from models import storage
from models.user import User

@app_views.route('/profile/<username>', strict_slashes=False, methods=['GET'])
@login_required
def user_profile(username):
    """ userprofile function """
    user = storage.get_user_by_username(User, username=username)
    storage.reload()
    
    if user:
        if user.username == current_user.username or current_user.super_admin:
            if user.super_admin:
                flash("Super admin profile", "success")
                return render_template("super_admin_profile.html")
            elif user.admin:
                flash("Admin profile", "success")
                return render_template("admin_profile.html")
            else:
                return render_template("user_profile.html")
        else:
            return redirect(url_for("app_views.login"))
    else:
        return redirect(url_for("app_views.login"))