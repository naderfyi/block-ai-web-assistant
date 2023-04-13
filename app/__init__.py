from flask import Flask
from .db import db

def create_app():
    app = Flask(__name__)

    # Load configuration settings
    app.config.from_object('config.Config')

    # Initialize Firestore
    with app.app_context():
        db

    # Import and register routes
    from .routes import main
    app.register_blueprint(main)

    return app

app = create_app()
