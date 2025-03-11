"""Python initialization file for the chat application."""

from dotenv import load_dotenv
from flask import Flask
from flask_session import Session
from .config import Config
from .routes import main


def create_app():
    """Application factory function to create and configure the Flask app."""
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(Config.validate())

    # Initialize session management
    Session(app)

    # Register blueprints
    app.register_blueprint(main)

    return app
