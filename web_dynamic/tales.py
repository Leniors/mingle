#!/usr/bin/python3
"""
tales Page
"""

from . import app_views
from flask import render_template, flash, redirect
from flask_login import login_required, current_user
from models import storage
from models.tale import Tale
from .forms import EditTaleForm
import requests

@app_views.route('/tales/<id>', strict_slashes=False, methods=['GET'])
def tales(id):
    """ Tales function """
    tale = storage.get_tale_by_id(Tale, id)
    return render_template("tale.html", tale=tale)

@app_views.route('/tales/<id>/update', strict_slashes=False, methods=['GET', 'POST'])
@login_required
def update_tale(id):
    """ Update Tale function """
    tale = storage.get_tale_by_id(Tale, id)
    if not tale:
        flash("Can't load Tale")
        return redirect(f"/mingle/profile/{current_user.username}")

    # Pre-populate form with current user data
    form = EditTaleForm(obj=tale)

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        
        url = f"http://www.leeroynyanchwa.tech:5001/api/v1/tales/{id}"
        data = {
            "title": title,
            "content": content
        }
        response = requests.put(url, json=data)
        if response.status_code == 200:
            flash("Update Successful", "success")
            return redirect(f"/mingle/profile/{current_user.username}")
        else:
            flash("Did not update", "error")
            return redirect(f"/mingle/profile/{current_user.username}")
    else:
        return render_template("edit_tale.html", form=form)