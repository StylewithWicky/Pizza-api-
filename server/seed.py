
from server.models import db, Restaurant, Pizza, RestaurantPizza
from server.app import create_app

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Domino's", address="123 Pizza Street")
    p1 = Pizza(name="Pepperoni", ingredients="Cheese, Tomato, Pepperoni")
    rp = RestaurantPizza(price=12, pizza=p1, restaurant=r1)

    db.session.add_all([r1, p1, rp])
    db.session.commit()
