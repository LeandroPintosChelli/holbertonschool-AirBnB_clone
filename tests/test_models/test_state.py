#!/usr/bin/python3
"""Defines unittests for models/state.py."""
import os
import models
import unittest
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestState_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def test_name_is_public_class_attribute(self):
        self.assertEqual(str, type(State.name))
