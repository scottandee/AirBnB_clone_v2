#!/usr/bin/python3
"""
State Module for HBNB project
"""
from os import getenv

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    '''
    State class
    subclasses BaseModel, declarative base
    '''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete",
                          backref="state", passive_deletes=True)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            '''getter attribute cities
            returns the list of City instances
            with state_id equals to the current State.id
            '''
            cities_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
