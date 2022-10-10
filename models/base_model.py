#!/usr/bin/python3
"""Defines the BaseModel class."""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Represents the BaseModel of the project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args: Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, t_format)
                else:
                    self.__dict__[key] = value


    def __str__(self):
        """Print the str representation of the BaseModel instance."""
        z = self.__class__.__name__
        x = "[{}] ({}) {}".format(z, self.id, self.__dict__)
        return x

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def __repr__(self):
        return "Retorno esto {}\n{}\n{}\n".format(self.id, self.created_at, self.updated_at)

x = BaseModel()
print(x)
