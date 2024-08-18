#!/usr/bin/python3
""" class Collection """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.association_tables import collections_tales

class Collection(BaseModel, Base):
    """Representation of a collection"""
    if models.storage_t == 'db':
        __tablename__ = 'collections'
        title = Column(String(128), nullable=False)
        description = Column(String(500), nullable=True)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        tales = relationship('Tale', secondary=collections_tales, backref='collections')

    def __init__(self, *args, **kwargs):
        """Initializes collection"""
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = super().to_dict()
        if "tales" in new_dict:
            new_dict["tales"] = [tale.id for tale in self.tales]
        return new_dict
