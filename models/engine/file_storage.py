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
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
