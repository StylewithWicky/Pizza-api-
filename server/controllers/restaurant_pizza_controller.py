from flask import Blueprint, jsonify

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

# Optional route for testing
@restaurant_pizza_bp.route('/restaurant_pizzas')
def get_restaurant_pizzas():
    return jsonify([])  # placeholder response
