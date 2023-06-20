#!/usr/bin/python3
'''module:
this module instantiates an object of:
  4 class FileStorage, or DBStorage based off environment varibale value
'''
from os import environ

if environ.get('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
