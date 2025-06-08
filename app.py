from flask import Flask
from interface.routes import main_bp

def create_app():
  """Create and configure the Flask application."""
  app = Flask(__name__)
  register_blueprints(app)
  return app

def register_blueprints(app):
  """Register Flask blueprints."""
  app.register_blueprint(main_bp)

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000, debug=True)