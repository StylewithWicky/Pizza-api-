from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from _init_ import app

# Local imports
from .config import Config
from .models import db
from .controllers import register_routes

# Initialize Flask extensions
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Load config
    app.config.from_object(Config)

    # Initialize database and migrations
    db.init_app(app)
    migrate.init_app(app, db)

    # Register all routes via blueprint registration function
    register_routes(app)

if __name__=='__main__':
    app.run(debug=True)
