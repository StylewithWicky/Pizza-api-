from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate

db=SQLAlchemy
migrate=Migrate()

def app_create():
    app=Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app,db)

    from controllers import register_routes
    register_routes(app)

    return app