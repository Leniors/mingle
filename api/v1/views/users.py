#!/usr/bin/python3
"""
handle User objects
"""
from flask import jsonify, abort, request
from models import storage
from models.user import User
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    users = storage.all(User)
    return jsonify([user.to_dict() for user in users.values()]), 200