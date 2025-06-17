from flask import Blueprint, jsonify

restaurant_bp = Blueprint('restaurant_bp', __name__)

# Example route (you can remove or edit it)
@restaurant_bp.route('/restaurants')
def get_restaurants():
    return jsonify([])  # Dummy data for testing
