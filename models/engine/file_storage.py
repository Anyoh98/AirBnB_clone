#!/usr/bin/env python3
"""
This script contatins code that will convert python
object to json string and json string back to python object
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Class that serializes instances to Json files and deserializes
    Json files to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the whole dictionary"""
        return self.__objects

    def new(self, obj):
        """
        This function want to add newly create dobject to the
        dictionary
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        This use the to_dict function to convertthe dictionary to
        our own dict format and then will
        open/create and empty JSON file wo we can
        write or put the dictionary in the file to save it.
        """
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as j_file:
            json.dump(obj_dict, j_file)

    def reload(self):
        """
        Deserializes the json file back to the
        orginal python dictionary.
        """
        try:
            if os.path.exists(FileStorage.__file_path):
                with open(FileStorage.__file_path, 'r') as j_file:
                    py_obj_dict = json.load(j_file)
                    for key, value in py_obj_dict.items():
                        class_name, obj_id = key.split(".")
                        py_obj = eval(class_name)(**value)
                        FileStorage.__objects[key] = py_obj
        except FileNotFoundError:
            pass
