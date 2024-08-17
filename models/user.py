#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Boolean
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy import func

class User(BaseModel, Base, UserMixin):
    """ Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        fullname = Column(String(20), nullable=True, unique=False)
        username = Column(String(20), nullable=False, unique=True)
        email = Column(String(128), nullable=False, unique=True)
        password = Column(String(1000), nullable=False)
        admin = Column(Boolean, default=False, nullable=False)
        super_admin = Column(Boolean, default=False, nullable=False)
        about = Column(String(256), nullable=True, unique=False)
        tales = relationship('Tale', backref='user')

    def __init__(self, *args, **kwargs):
        """initializes user"""
        # Set the default fullname if it's not provided
        if 'fullname' not in kwargs or not kwargs['fullname']:
            session = models.storage._DBStorage__session
            user_count = session.query(func.count(User.id)).scalar() or 0
            kwargs['fullname'] = f"User{user_count + 1}"
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        time = "%Y-%m-%dT%H:%M:%S.%f"
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if "password" in new_dict:
            del new_dict["password"]
        if "super_admin" in new_dict:
            del new_dict["super_admin"]
        return new_dict
