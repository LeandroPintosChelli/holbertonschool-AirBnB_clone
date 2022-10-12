#!/usr/bin/python3
"""Unittest module for the FileStorage class."""

import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json


class TestFileStorage(unittest.TestCase):

    def test_file_path_(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test__objects(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        var = storage.all().copy()
        storage.new(BaseModel())
        self.assertNotEqual(var, storage.all())
