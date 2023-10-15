#!/usr/bin/env python3
""" This script contains the code for the Baseclass model """


from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    This is the super class tha all other classes will inherit from.

    Public instance attributes:
    - id: string - A unique identifier for each BaseModel instance.
    - created_at: datetime - The date and time when the instance is created.
    - updated_at: datetime - The date and time when the instance is last
    updated.

    Public instance methods:
    - __str__: Returns a human-readable string representation of the object.
    - save: Updates the 'updated_at' attribute with the current date
    and time.
    - to_dict: Converts the object's attributes into a dictionary for
    serialization.
    """

    def __init__(self, *args, **kwargs):
        """ Initializes all class attributes """
        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'updated_at':
                    value = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key == 'created_at':
                    value = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"
                    )
                if 'id' not in kwargs.keys():
                    self.id = str(uuid4())
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.now()
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Returns the string representatioin of instance of the class """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ function save"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Convert the BaseModel instance's attributes into a
        dictionary for serialization.

        Returns:
            A dictionary containing all instance attributes and
            additional keys:
            - '__class__': The class name of the object.
            - 'created_at': The 'created_at' attribute in ISO date-time
            format.
            - 'updated_at': The 'updated_at' attribute in ISO date-time
            format.
        """
        object_dic = self.__dict__.copy()
        object_dic["__class__"] = type(self).__name__
        object_dic["created_at"] = self.created_at.isoformat()
        object_dic["updated_at"] = self.updated_at.isoformat()
        return object_dic
