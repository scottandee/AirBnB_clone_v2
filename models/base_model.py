#!/usr/bin/python3
'''module for Base class:
for subclassing
this module defines a base class for all models in our hbnb clone'''

import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    '''A base class for all hbnb models'''
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        '''constructor
        instantiates a new model
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(value))
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        '''returns a string representation of the instance'''
        cls = self.__class__.__name__
        attributes = {k: v for k, v in self.__dict__.items()
                      if k != '_sa_instance_state'}
        return '[{}] ({}) {}'.format(cls, self.id, attributes)

    def save(self):
        '''
        updates updated_at with current timestamp when instance is changed
        '''
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        '''converts instance into dict format'''
        dictionary = self.__dict__.copy()
        dictionary.pop('_sa_instance_state', None)
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        '''deletes the current instance from storage'''
        from models import storage
        storage.delete(self)
