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

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.json
    new_user = User(**data)
    new_user.save()
    return jsonify(new_user.to_dict()), 201

@app_views.route('/users/<username>', methods=['GET'], strict_slashes=False)
def get_user(username):
    user = storage.get_user_by_username(User, username)
    if  user:
        return jsonify(user.to_dict()), 200
    else:
        abort(404)
        
@app_views.route('/users/<username>', methods=['PUT'], strict_slashes=False)
def update_user(username):
    user = storage.get_user_by_username(User, username)
    if user is None:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.json
    ignore_keys = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict()), 200
        
@app_views.route('/users/<username>/tales', methods=['GET'], strict_slashes=False)
def get_user_tales(username):
    user = storage.get_user_by_username(User, username)
    if  user:
        user_tales = user.tales
        print(user_tales)
        return jsonify([tale.to_dict() for tale in user_tales]), 200
    else:
        abort(404)
