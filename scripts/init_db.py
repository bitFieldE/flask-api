"""
Database initialization script.
"""
import os
from flask import Flask
from interface.extensions import db

def init_db():
  """Initialize the database with schema and sample data."""
  app = Flask(__name__)

  # Set up PostgreSQL
  app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  # Ensure the instance folder exists
  os.makedirs(app.instance_path, exist_ok=True)

  # Initialize SQLAlchemy
  db.init_app(app)

  with app.app_context():
    # Create all tables
    db.create_all()

  if __name__ == "__main__":
    init_db()
