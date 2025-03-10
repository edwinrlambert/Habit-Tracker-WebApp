from flask import Flask
from config import Config
from .extensions import db, migrate, login_manager
from .auth.routes import auth
from .habits.routes import habits

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize Extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    # Register Blueprints
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(habits, url_prefix='/habits')
    
    return app