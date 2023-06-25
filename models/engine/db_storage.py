#!/usr/bin/python3
'''
DBStorage module for HBNB project
'''

from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage():
    '''DBStorage
    class for managing database storage
    '''

    __engine = None
    __session = None

    def __init__(self):
        '''initialize DBStorage'''
        db_user = environ.get('HBNB_MYSQL_USER')
        password = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST', 'localhost')
        db = environ.get('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            f'mysql+mysqldb://{db_user}:{password}@{host}/{db}',
            pool_pre_ping=True
            )

        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def all(self, cls=None):
        '''query all objects from the database'''
        objects = {}

        classes = {'State': State, 'City': City, 'User': User, 'Place': Place,
                   'Review': Review, 'Amenity': Amenity}

        if cls:
            if isinstance(cls, str) and cls in classes:
                cls = eval(cls)
            if cls in classes:
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = f'{type(obj).__name__}.{obj.id}'
                    objects[key] = obj
        else:
            for key in classes.keys():
                objs = self.__session.query(classes[key]).all()
                for obj in objs:
                    key = f'{type(obj).__name__}.{obj.id}'
                    objects[key] = obj
        return objects

    def new(self, obj):
        '''add a new object to the database session'''
        self.__session.add(obj)

    def save(self):
        '''commit changes in the database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete an object from the database session'''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''reload database tables and create a new session'''
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
