#!/usr/bin/python3
from . import app_views
from .forms import MakeAdmin
from models import storage
from models.user import User
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user

@app_views.route('/makeadmin', strict_slashes=False, methods=['GET', 'POST'])
@login_required
def makeadmin():
    """ make admin route """
    print(current_user.super_admin)
    if not current_user.super_admin:
        return redirect(url_for("app_views.login"))
    
    form = MakeAdmin()
    if form.validate_on_submit():
        username = form.username.data
        
        user = storage.get_user_by_username(User, username)
        
        if not user:
            flash("No user with this username")
            return redirect(url_for("app_views.makeadmin"))
        user.admin = True
        user.save()
        return redirect(f"/mingle/profile/{current_user.username}")
        
    return render_template("make_admin.html", form=form)