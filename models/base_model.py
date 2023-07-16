#!/usr/bin/python3
"""This script is the base model"""

from uuid import uuid4
from datetime import date, datetime
import models


class BaseModel:

    """Base Class for all other classes to inherit from"""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Public instance attribute updated_at is updated"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary of keys value pairs from __dict__"""

        myClass_dict = self.__dict__.copy()
        myClass_dict["__class__"] = type(self).__name__
        myClass_dict["created_at"] = myClass_dict["created_at"].isoformat()
        myClass_dict["updated_at"] = myClass_dict["updated_at"].isoformat()

        return myClass_dict
