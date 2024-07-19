#!/usr/bin/python3
"""
handle User objects
"""
from flask import jsonify, abort
from models import storage
from models.user import User
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    users = storage.all(User)
    return jsonify([user.to_dict() for user in users.values()]), 200

@app_views.route('/users/<username>', methods=['GET'], strict_slashes=False)
def get_user(username):
    user = storage.get_user_by_username(User, username)
    if  user:
        return jsonify(user.to_dict()), 200
    else:
        abort(404)
