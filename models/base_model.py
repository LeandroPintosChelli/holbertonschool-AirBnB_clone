#!/usr/bin/python3
"""Defines the BaseModel class."""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Represents the BaseModel of the project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args: Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        # Assing a uuid to the id and convert it intoastring.
        self.id = str(uuid4())
        # Print the date and time when an instance is created.
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            # Return the list with the keys and the values of the dict.
            for key, value in kwargs.items():
                # If the key is equal to the strings:
                # Create an object with date and time from a given string.
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, t_format)
                else:
                    # If the key is not equal to the string, equals it to te value.
                    self.__dict__[key] = value
        else:
            #Calls te method 'new' of the FileStorage class
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Converts an object into a dictionary.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        # Create a copy of the __dict__ and not only
        # reference it, to not modify the original 
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = dictionary["created_at"].isoformat()
        dictionary["updated_at"] = dictionary["updated_at"].isoformat()
        return dictionary

    def __str__(self):
        """Print the str representation of the object."""
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)
