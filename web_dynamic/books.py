#!/usr/bin/python3
"""
Books Page
"""

from . import app_views
from flask import render_template

@app_views.route('/books', strict_slashes=False, methods=['GET'])
def books():
    """ Books function """
    return render_template("books.html")