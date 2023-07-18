#!/usr/bin/python3

"""Create class BaseModel"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    class BaseModel
    """
    def __init__(self, *args, **kwargs):
        """Constructor method"""
        from models import storage
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))

                else:
                    setattr(self, key, value)

    def __str__(self):
        """String representation"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Updates attr updated_at with current time"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns dictionary of key values of instance"""
        my_dict = self.__dict__.copy()
        # my_dict['id'] = self.id
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict

