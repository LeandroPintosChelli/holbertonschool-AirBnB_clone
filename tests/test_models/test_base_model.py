#!/usr/bin/python3
""""Base_model tests"""

import unittest
import json
from models.base_model import BaseModel
from time import sleep
from models.engine.file_storage import FileStorage
import os


class TestBaseModel(unittest.TestCase):

    def test_base_model_save(self):
        Base = BaseModel()
        var = Base.updated_at
        sleep(0.01)
        Base.save()
        self.assertLess(var, Base.updated_at)

    def test_save2(self):
        base = BaseModel()
        var1 = base.updated_at
        sleep(0.01)
        base.save()
        var2 = base.updated_at
        self.assertLess(var1, var2)
        sleep(0.05)
        base.save()
        self.assertLess(var2, base.updated_at)
    
    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_id(self):
        self.assertEqual(type(BaseModel().id), str)
    
    def test_to_dict(self):
        Base = BaseModel()
        Base_dict = dict(Base.__dict__)
        Base_dict["__class__"] = "BaseModel"
        Base_dict["created_at"] = Base_dict["created_at"].isoformat()
        Base_dict["updated_at"] = Base_dict["updated_at"].isoformat()
        self.assertEqual(Base_dict, Base.to_dict())

    def test__init__(self):
        args = [i for i in range(1000)]
        Base = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        Base = BaseModel(*args)
