#!/usr/bin/python3
"""
Collections Page
"""

from . import app_views
from flask import render_template, redirect, flash, url_for
from models import storage
from models.collections import Collection
from models.tale import Tale
from .forms import AddTalesToCollectionForm
from flask_login import login_required, current_user

@app_views.route('/collections', strict_slashes=False, methods=['GET'])
@login_required
def books():
    """ Collections function """
    return render_template("collections.html")

@app_views.route('/collection/<collection_id>/add_tales', methods=['GET', 'POST'])
def add_tales_to_collection(collection_id):
    collection = storage.get(Collection, collection_id)
    if not collection:
        flash('Collection not found', 'danger')
        return redirect(f'/mingle/profile/{current_user.username}')

    form = AddTalesToCollectionForm()
    
    # Ensure that all IDs are strings
    form.tales.choices = [(str(tale.id), tale.title) for tale in current_user.tales]

    if form.validate_on_submit():
        print("We are loading...")
        selected_tales = form.tales.data
        
        # Convert tale_id to the appropriate type if needed
        for tale_id in selected_tales:
            tale = storage.get(Tale, tale_id)
            if tale:
                collection.tales.append(tale)
        storage.save()
        flash('Tales added to collection successfully!', 'success')
        return redirect(f'/mingle/profile/{current_user.username}')
    
    if form.errors:
        flash('Form validation failed!', 'danger')
        print("Form validation failed:", form.errors)

    return render_template('add_tales_to_collection.html', form=form, collection=collection)