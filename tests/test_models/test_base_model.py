#!/usr/bin/python3
""""Base_model tests"""

import unittest
import json
from models.base_model import BaseModel
from time import sleep


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
