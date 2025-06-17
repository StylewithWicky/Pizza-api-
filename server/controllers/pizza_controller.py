from flask import Blueprint, jsonify

pizza_bp = Blueprint('pizza_bp', __name__)

# Optional test route
@pizza_bp.route('/pizzas')
def get_pizzas():
    return jsonify([])  # dummy data
