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

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'mingle')
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
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    app.logger.error(f'Server error: {error}')
    return render_template('500.html'), 500

# Routes
@app.route('/mingle', strict_slashes=False)
def mingle():
    """ mingle """
    return render_template("mingle.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=os.environ.get('FLASK_DEBUG', 'True') == 'True')
