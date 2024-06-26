#!/usr/bin/python3
"""
handle Tale objects
"""
from flask import jsonify, abort, request
from models import storage
from models.tale import Tale
from api.v1.views import app_views

@app_views.route('/tales', methods=['GET'], strict_slashes=False)
def get_tales():
    tales = storage.all(Tale)
    """for tale in tales.values():
        print(tale.user.username)
    print(tales)"""
    return jsonify([tale.to_dict() for tale in tales.values()]), 200

@app_views.route('/tales', methods=['POST'], strict_slashes=False)
def create_tale():
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.json
    new_tale = Tale(**data)
    new_tale.save()
    return jsonify(new_tale.to_dict()), 201

"""
@app_views.route('/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict()), 200


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_amenity(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200

@app_views.route('/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def update_amenity(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.json
    ignore_keys = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(amenity, key, value)
    amenity.save()
    return jsonify(amenity.to_dict()), 200
"""
