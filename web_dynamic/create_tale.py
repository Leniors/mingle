#!/usr/bin/python3
""" createtale route file """

from . import app_views
from .forms import TaleForm
from flask import render_template, flash, redirect, url_for
from models import storage
from models.tale import Tale
from flask_login import login_required, current_user
import requests

@app_views.route('/createtale', strict_slashes=False, methods=['GET', 'POST'])
@login_required
def create_tale():
    """ create_tale function """
    form = TaleForm()
    if form.validate_on_submit():
        url = "http://localhost:5001/api/v1/tales"
        data = {
            "title": form.title.data,
            "content": form.content.data,
            "user_username": current_user.username
        }
        response = requests.post(url, json=data)
        return redirect(f"/mingle/profile/{current_user.username}")
    return render_template("create_tale.html", form=form)
