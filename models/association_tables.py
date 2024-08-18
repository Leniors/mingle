#!/usr/bin/python3
""" collections_tales """
import models
from sqlalchemy import Table, Column, ForeignKey, String
from models.base_model import Base

if models.storage_t == 'db':
    collections_tales = Table(
        'collections_tales', Base.metadata,
        Column('collection_id', String(60), ForeignKey('collections.id'), primary_key=True),
        Column('tale_id', String(60), ForeignKey('tales.id'), primary_key=True)
    )
