#!/usr/bin/python3
""" City Module for HBNB project """


from os import getenv
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    '''the city class, contains state ID and name'''

    __tablename__ = 'cities'
    if getenv('HBNB_TYPE_STORAGE') is not None:
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', cascade='all, delete', backref='cities',
                              passive_deletes=True)
    else:
        state_id = ""
        name = ""
