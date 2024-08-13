#!/usr/bin/python3
""" Mingle app views """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/mingle/')

from . import login
from . import sign_up
from . import logout
from . import user_profile
from . import change_password
from . import make_admin
from . import create_tale
from . import minglers