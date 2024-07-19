#!/usr/bin/python3
""" logout route for mingle """
from flask_login import login_required, logout_user
from flask import redirect, url_for, flash
from . import app_views

@app_views.route('/logout', strict_slashes=False, methods=['GET', 'POST'])
@login_required
def logout():
    """ logout function """
    logout_user()
    flash("Logout successful", "success")
    return redirect(url_for("mingle"))