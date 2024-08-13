#!/usr/bin/python3
"""
mingle home root file
"""
from flask import Flask, render_template, jsonify
from flask_cors import CORS
from . import app_views
from flask_login import LoginManager
from models import storage
from models.user import User
from .utils import time_ago_in_words
import logging
from logging.handlers import RotatingFileHandler
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
print(os.getenv('SECRET_KEY'))
app.jinja_env.filters['time_ago_in_words'] = time_ago_in_words

# Setup Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'app_views.login'

@login_manager.user_loader
def load_user(id):
    return storage.get_user_by_id(User, id)

# Enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})

# Register blueprint
app.register_blueprint(app_views)

# Logging configuration
if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/mingle.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    
    app.logger.setLevel(logging.INFO)
    app.logger.info('Mingle startup')

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    app.logger.error(f'Not found: {error}')
    storage.rollback()
    return render_template('404.html'), 404

# Routes
@app.route('/mingle', strict_slashes=False)
def mingle():
    """ mingle """
    return render_template("mingle.html")

@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database again at the end of the request."""
    if exception:
        storage.rollback()
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=os.environ.get('FLASK_DEBUG', 'True') == 'True')
