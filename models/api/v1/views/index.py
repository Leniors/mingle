#!/usr/bin/python3
"""
index file
"""
from api.v1.views import app_views
from flask import jsonify
import models
from models.category import Category
from models.base_model import BaseModel, Base
from models import storage


@app_views.route('/status', strict_slashes=False)
def get_status():
    """status of the request"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def get_stats():
    """stats"""
    classes = {"Category": Category}
    stats = {}
    for cls in classes.keys():
        if cls == "Category":
            stats["categories"] = storage.count(classes[cls])
    return jsonify(stats)
