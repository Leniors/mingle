#!/usr/bin/python3
""" createtale route file """

from . import app_views
from .forms import TaleForm
from flask import render_template, flash, redirect, url_for
from models import storage
from models.tale import Tale
from flask_login import login_required, current_user

@app_views.route('/createtale', strict_slashes=False, methods=['GET', 'POST'])
@login_required
def create_tale():
    """ create_tale function """
    form = TaleForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        
        tale = Tale(title=title, content=content, user_username=current_user.username)
        tale.save()
        return redirect(f"/mingle/profile/{current_user.username}")
    return render_template("create_tale.html", form=form)
