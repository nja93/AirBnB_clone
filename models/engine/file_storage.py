#!/usr/bin/python3
"""File Storage Class"""


import datetime
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
    This module is responsible for serialization and deserialization of
    class instances.
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
        key = "{}.{}".format(type(obj).__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the objects dictionary to a JSON file.

        """
        with open(self.__file_path, "w", encoding="utf-8") as file:
            data = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(data, file)

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

    def attributes(self):
        """Returns a dictionary of attributes and their types based in class_name"""

        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes

    def reload(self):
        """
        Deserializes the JSON file and updates the objects dictionary.
        If JSON file exists read the file
        and load objects.
        If file doesn't exist, do nothing.
        """
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r", encoding="utf-8") as file:
            my_dict = json.load(file)
            my_dict = {key: self.classes()[val["__class__"]](**val)
                        for key, val in my_dict.items()}

            self.__objects = my_dict



