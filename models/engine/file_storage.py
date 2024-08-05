#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from datetime import datetime

classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity,
           'Review': Review}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects

        if isinstance(cls, type):
            list_obj = {}
            for key, value in self.__objects.items():
                if isinstance(value, cls):
                    list_obj[key] = value
            return list_obj

        return {}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage file"""
        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, 'r') as f:
                    temp = json.load(f)
                    for key, val in temp.items():
                        cls_name = val['__class__']
                        if cls_name in classes:
                            val['created_at'] = datetime.fromisoformat(
                                val['created_at'])
                            val['updated_at'] = datetime.fromisoformat(
                                val['updated_at'])
                            self.__objects[key] = classes[cls_name](**val)
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error loading file: {e}")
        else:
            with open(FileStorage.__file_path, 'w') as f:
                json.dump({}, f)

    def delete(self, obj=None):
        """Deletes objects"""

        if obj is not None:

            obj_key = f"{obj.__class__.__name__}.{obj.id}"

            if obj_key in self.__objects:

                del self.__objects[obj_key]
