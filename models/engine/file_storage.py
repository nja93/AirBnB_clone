#!/usr/bin/python3
"""File Storage Class"""


import datetime
import json
import os
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class FileStorage:
    """
    This class provides a file storage module for serializing instances
    to a JSON file and deserializing JSON files to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all objects.
        """
        return self.__objects

    def new(self, obj):
        """
        In the __objects dict the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes the objects dictionary to a JSON file.

        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            data = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
            json.dump(data, file)

    def reload(self):
        """
        Deserializes the JSON file and updates the objects dictionary.
        If JSON file exists read the file
        and load objects.
        If file doesn't exist, do nothing.
        """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
            my_dict = json.load(file)
            my_dict = {key: self.classes()[val["__class__"]](**val)
                        for key, val in my_dict.items()}

            FileStorage.__objects = my_dict

    def classes(self):
        """Return key value pairs of classes and values """

        class_dict = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                    "Review": Review}

        return class_dict

