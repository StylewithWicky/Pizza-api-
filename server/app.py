from flask import Flask
from flask_migrate import Migrate
from .config import Config
from .models import db
from .controllers import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    register_routes(app)

    return app

