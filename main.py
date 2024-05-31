#!/usr/bin/python3
"""
mingle home root file
"""
from flask import Flask, render_template
from flask_cors import CORS
from . import app_views
from flask_login import LoginManager
from models import storage
from models.user import User
from .utils import time_ago_in_words

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mingle'

app.jinja_env.filters['time_ago_in_words'] = time_ago_in_words

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'app_views.login'

@login_manager.user_loader
def load_user(id):
    return storage.get_user_by_id(User, id)

CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(app_views)

@app.route('/mingle', strict_slashes=False)
def mingle():
    """ mingle """
    return render_template("mingle.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
