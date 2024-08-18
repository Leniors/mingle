#!/usr/bin/python3
"""
Handle Book objects
"""
from flask import jsonify, abort, request
from models import storage
from models.collections import Collection
from api.v1.views import app_views

@app_views.route('/collections', methods=['GET'], strict_slashes=False)
def get_collections():
    """Retrieve all collections"""
    collections = storage.all(Collection)
    return jsonify([collection.to_dict() for collection in collections.values()]), 200

@app_views.route('/collections', methods=['POST'], strict_slashes=False)
def create_collection():
    """Create a new collection"""
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.json
    # Ensure 'user_id' is provided in the request data
    if 'user_id' not in data:
        abort(400, description="Missing user_id")
    
    new_collection = Collection(**data)
    new_collection.save()
    return jsonify(new_collection.to_dict()), 201

@app_views.route('/collections/<id>', methods=['GET'], strict_slashes=False)
def get_collection(id):
    """Retrieve a colleection by id"""
    collection = storage.get(Collection, id)
    if collection:
        return jsonify(collection.to_dict()), 200
    else:
        abort(404)

@app_views.route('/collections/<id>', methods=['PUT'], strict_slashes=False)
def update_collection(id):
    """Update a collection by id"""
    collection = storage.get(Collection, id)
    if collection is None:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    
    data = request.json
    ignore_keys = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(collection, key, value)
    collection.save()
    return jsonify(collection.to_dict()), 200

@app_views.route('/collections/<id>', methods=['DELETE'], strict_slashes=False)
def delete_collection(id):
    """Delete a collection by id"""
    collection = storage.get(Collection, id)
    if collection is None:
        abort(404)
    collection_dict = collection.to_dict()
    storage.delete(collection)
    storage.save()
    
    return jsonify(collection_dict), 204
