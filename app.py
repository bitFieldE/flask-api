import os
from flask import Flask
from interface.routes import main_bp
from interface.extentions import db, migrate
from flask_cors import CORS

def create_app():
  """Create and configure the Flask application."""
  app = Flask(__name__)

  # Initialize extensions
  initialize_extentions(app)
  
  # Register blueprints
  register_blueprints(app)
  
  # Enable CORS
  CORS(app)

  return app

def initialize_extentions(app):
  """Initialize Flask extensions."""
  # Initialize SQLAlchemy
  db.init_app(app)
  
  # Initialize Flask-Migrate
  migrate.init_app(app, db)


def register_blueprints(app):
  """Register Flask blueprints."""
  app.register_blueprint(main_bp)

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000, debug=True)