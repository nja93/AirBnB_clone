#!/usr/bin/python3

"""
Create class FileStorage
"""
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import json


class FileStorage:
    """
    Class FileStorage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj
        """
        class_name = obj.__class__.__name__
        self.__objects[f"{class_name}.{obj.id}"] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        non_ser_dict = self.__objects
        ser_dict = {}

        for obj_id in non_ser_dict.keys():
            ser_dict[obj_id] = non_ser_dict[obj_id].to_dict()

        with open(self.__file_path, "w") as json_file:
            json.dump(ser_dict, json_file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path) as json_file:
                ser_dict = json.load(json_file)
                for values in ser_dict.values():
                    cls_name = values["__class__"]
                    del values["__class__"]
                    self.new(eval(cls_name)(**values))

        except FileNotFoundError:
            return
        
