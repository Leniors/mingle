#!/usr/bin/python
""" holds class category"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String


class Category(BaseModel, Base):
    """Representation of Category"""
    if models.storage_t == 'db':
        __tablename__ = 'categories'
        name = Column(String(128), nullable=False)

    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
