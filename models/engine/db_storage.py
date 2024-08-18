#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.user import User
from models.tale import Tale
from models.collections import Collection
from models.base_model import Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv

load_dotenv()

classes = {"Collection": Collection, "User": User, "Tale": Tale}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
        
    def rollback(self):
        self.__session.rollback()
        
    def get(self, cls, id):
        """get one object from a class"""
        obj = self.__session.query(cls).filter_by(id=id).first()
        return obj

    def get_user_by_email(self, cls, email):
        """Get a user by an email"""
        obj = self.__session.query(cls).filter_by(email=email).first()
        return obj

    def get_user_by_id(self, cls, id):
        """Get a user by an id"""
        obj = self.__session.query(cls).filter_by(id=id).first()
        return obj

    def get_user_by_username(self, cls, username):
        """Get a user by a username"""
        obj = self.__session.query(cls).filter_by(username=username).first()
        return obj

    def count(self, cls=None):
        """count number of elements"""
        objs = []
        if cls == None:
            objs.extend(self.all())
        else:
            objs.extend(self.__session.query(cls).all())
        return len(objs)
    
    def get_tale_by_id(self, cls, id):
        """Get a tale by an id"""
        obj = self.__session.query(cls).filter_by(id=id).first()
        return obj
