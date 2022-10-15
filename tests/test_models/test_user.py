#!/usr/bin/python3
"""Unittest module for the User Class."""
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json
import os
from models.user import User


class TestUser(unittest.TestCase):
    """Test Cases for the User class."""

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))
        