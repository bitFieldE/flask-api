import os
from flask import Flask
from interface.routes import main_bp
from interface.extensions import db, migrate
from flask_cors import CORS

def create_app():
  """Create and configure the Flask application."""
  app = Flask(__name__)

  # Set up PostgreSQL
  app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  # Initialize extensions
  initialize_extensions(app)
  
  # Register blueprints
  register_blueprints(app)
  
  # Enable CORS
  CORS(app, resources={r"/api/*": {"origins": "*"}})

  return app

def initialize_extensions(app):
  """Initialize Flask extensions."""
  # Initialize SQLAlchemy
  db.init_app(app)
  
  # Initialize Flask-Migrate
  migrate.init_app(app, db)

  # Create tables if they don't exist
  with app.app_context():
    db.create_all()

def register_blueprints(app):
  """Register Flask blueprints."""
  app.register_blueprint(main_bp)

if __name__ == "__main__":
  app = create_app()
  app.run(host="0.0.0.0", port=8000, debug=True)