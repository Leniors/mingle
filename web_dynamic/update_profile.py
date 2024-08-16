#!/usr/bin/python3
""" logout route for mingle """
from . import app_views
from flask_login import login_required, current_user
from flask import render_template, redirect, flash
from models import storage
from models.user import User
from .forms import EditProfileForm
import requests

@app_views.route('/profile/<username>/editprofile', strict_slashes=False, methods=['GET', 'PUT', 'POST'])
@login_required
def edit_profile(username):
    """ Edit profile function """
    user = storage.get_user_by_username(User, username=username)
    if not user:
        flash("Can't load user")
        return redirect(f"/mingle/profile/{current_user.username}")

    # Pre-populate form with current user data
    form = EditProfileForm(obj=user)

    if form.validate_on_submit():
        fullname = form.fullname.data
        about = form.about.data
        
        url = f"http://localhost:5001/api/v1/users/{username}"
        data = {
            "fullname": fullname,
            "about": about
        }
        response = requests.put(url, json=data)
        if response.status_code == 200:
            flash("Update Successful", "success")
            return redirect(f"/mingle/profile/{current_user.username}")
        else:
            flash("Did not update", "error")
            return redirect(f"/mingle/profile/{current_user.username}")
    else:
        return render_template("edit_profile.html", form=form)