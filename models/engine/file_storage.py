#!/usr/bin/python3
"""File Storage"""
import json
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.state import State
from models.user import user
from models.amenity import Amenity
from models.city import City

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
                for i in new_obj.values():
                    cls_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(cls_name)(**i))
        except FileNotFoundError:
            pass

    def Classes(self):
        """Dictionary of valid classes"""
        Classes = {"BaseModel": BaseModel,
                    "Amanity": Amenity,
                    "City": City,
                    "Place": Place,
                    "Review": Review,
                    "State": State,
                    "User": user}
        return Classes
