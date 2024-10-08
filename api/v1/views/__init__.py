#!/usr/bin/python3
"""
init file
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from .index import *
from .tales import *
from .users import *
from .collections import *
