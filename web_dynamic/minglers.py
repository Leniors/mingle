#!/usr/bin/python3
"""
Users Page
"""

from . import app_views
from flask import render_template

@app_views.route('/minglers', strict_slashes=False, methods=['GET'])
def minglers():
    """ Minglers function """
    return render_template("minglers.html")