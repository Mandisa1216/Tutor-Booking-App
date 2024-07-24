from flask import Flask
from flask_pymongo import PyMongo
from .config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)
    with app.app_context():
        from.routes import user_routers
        from.routes import tutordetails
        from .routes import booking_routes

        app.register_blueprint(user_routers.app)
        app.register_blueprint(tutordetails.app)
        app.register_blueprint(booking_routes.app)
    
    return app
        
