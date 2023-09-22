#!/usr/bin/python3
'''
module - file_storage:
this module defines a class to manage file storage for hbnb clone
'''
import json


class FileStorage:
    '''class manages storage of hbnb models in JSON format
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        '''all
        returns a list of objects of one type of if class name arg exist
        else returns dictionary of models currently in storage
        '''
        if cls:
            cls_objects = {}
            for key, value in self.__objects.items():
                if isinstance(value, cls):
                    cls_objects[key] = value
            return cls_objects
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        '''saves storage dictionary to file'''
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        '''Loads storage dictionary from file'''
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        '''delete
        remove/delete an object from __objects if it exists
        '''
        if obj is not None:
            obj_key = f'{obj.__class__.__name__}.{obj.id}'
            if obj_key in self.__objects:
                del self.__objects[obj_key]
        else:
            pass

    def close(self):
        '''This refreshes the FileStorage'''
        self.reload()
