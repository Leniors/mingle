#!/usr/bin/python3
""" createcollection route file """

from . import app_views
from .forms import CollectionForm
from flask import render_template, redirect, flash
from models import storage
from models.collections import Collection  # Make sure this model exists
from flask_login import login_required, current_user
import requests

@app_views.route('/createcollection', strict_slashes=False, methods=['GET', 'POST'])
@login_required
def create_collection():
    """ Create a new collection """
    form = CollectionForm()
    if form.validate_on_submit():
        url = "http://localhost:5001/api/v1/collections"  # Adjust URL to your API endpoint
        data = {
            "title": form.title.data,
            "description": form.description.data,
            "user_id": current_user.id  # Add user association if needed
        }
        response = requests.post(url, json=data)
        if response.status_code == 201:  # Adjust according to your API response
            return redirect(f"/mingle/profile/{current_user.username}")
        else:
            # Handle error, e.g., flash a message
            flash("Error creating collection", "error")
    return render_template("create_collection.html", form=form)

@app_views.route('/collection/<id>', strict_slashes=False, methods=['GET'])
def collections(id):
    """ Collctions function """
    collection = storage.get(Collection, id)
    return render_template("collection.html", collection=collection)
