#!/usr/bin/python3
"""Defines unittests for models/amenity.py."""
import os
import models
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_name_is_public_class_attribute(self):
        self.assertEqual(str, type(Amenity.name))
