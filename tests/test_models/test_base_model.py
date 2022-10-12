#!/usr/bin/python3
""""Base_model tests"""

import unittest
import json
from models.base_model import BaseModel
from time import sleep
from models.engine.file_storage import FileStorage
import os


class TestBaseModel(unittest.TestCase):

    def test_base_model_1(self):
        Base = BaseModel()
        var = Base.updated_at
        sleep(0.01)
        Base.save()
        self.assertLess(var, Base.updated_at)

    def test_id(self):
        self.assertEqual(type(BaseModel().id), str)
    
    def test_to_dict(self):
        Base = BaseModel()
        Base_dict = dict(Base.__dict__)
        Base_dict["__class__"] = "BaseModel"
        Base_dict["created_at"] = Base_dict["created_at"].isoformat()
        Base_dict["updated_at"] = Base_dict["updated_at"].isoformat()
        self.assertEqual(Base_dict, Base.to_dict())

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_3_init_many_args(self):
        """Tests __init__ with many arguments."""
        self.resetStorage()
        args = [i for i in range(1000)]
        b = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        b = BaseModel(*args)
