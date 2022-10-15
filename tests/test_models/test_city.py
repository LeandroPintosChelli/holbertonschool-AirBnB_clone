#!/usr/bin/python3
"""Defines unittests for models/city.py."""

import os
import models
import unittest
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_state_id(self):
        self.assertEqual(str, type(City.state_id))

    def test_name(self):
        self.assertEqual(str, type(City.name))
