#!/usr/bin/python3
""""Base_model tests"""

import unittest
import json
from models.base_model import BaseModel
from time import sleep


class TestBaseModel(unittest.TestCase):

    def test_base_model_1(self):
        Base = BaseModel()
        Base.updated_at
        sleep(0.01)
        Base.save()
