#!/usr/bin/python3
"""
tales Page
"""

from . import app_views
from flask import render_template
from models import storage
from models.tale import Tale

@app_views.route('/tales/<id>', strict_slashes=False, methods=['GET'])
def tales(id):
    """ Tales function """
    tale = storage.get_tale_by_id(Tale, id)
    print(tale)
    return render_template("tale.html", tale=tale)