#!/usr/bin/python3
"""File Storage"""
import json
from models.base_model import BaseModel


class FileStorage:
    """serializes and deserialzes json files"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialzes __objects to JSON file."""
        new_dict = {}

        for key, obj in self.__objects.items():
            new_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """If json file exists, convert obj dicts back to instances"""
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
            for key, value in new_obj.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
