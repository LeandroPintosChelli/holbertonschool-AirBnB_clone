#!/usr/bin/python3
"""File Storage"""
import cmd
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """serializes and deserialzes json files"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the list of objects of a class."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets a new instance or object and adds it to the __objects dict."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialzes __objects to JSON file."""
        # Store the objects dictionary
        # provided by the 'to_dict' method.
        # a copy of the dict is created
        # Convert the dict into a json file
        new_dict = {}
        
        for key, obj in self.__objects.items():
            new_dict[key] = obj.to_dict()        
        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """If json file exists, read it and 
        convert object dicts back to instances"""
        # Open the file 
        # Converts the file into a dictionary
        # Create the objects and stores them in the class variable
        try:
            with open(self.__file_path, 'r') as f:    
                new_obj = json.load(f)
                for key, val in new_obj.values():
                    self.new(eval(new_obj['__class__'])(**key))
        except FileNotFoundError:
            pass

    # def Classes(self):
    #     """Dictionary of valid classes"""
    #     from models.base_model import BaseModel
    #     from models.place import Place
    #     from models.review import Review
    #     from models.state import State
    #     from models.user import User
    #     from models.amenity import Amenity
    #     from models.city import City

    #     Classes = {"BaseModel": BaseModel,
    #                 "Amanity": Amenity,
    #                 "City": City,
    #                 "Place": Place,
    #                 "Review": Review,
    #                 "State": State,
    #                 "User": User}
    #     return Classes
    def Classes(self, arg):
        """Dictionary of valid classes"""
        from models.base_model import BaseModel
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        from models.amenity import Amenity
        from models.city import City

        Classes = {"BaseModel": BaseModel(),
                    "Amanity": Amenity(),
                    "City": City(),
                    "Place": Place(),
                    "Review": Review(),
                    "State": State(),
                    "User": User()}
        return Classes[arg]