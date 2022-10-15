#!/usr/bin/python3
"""Defines unittests for models/review.py."""
import os
import models
import unittest
from datetime import datetime
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_place_id_is_public_class_attribute(self):
        self.assertEqual(str, type(Review.place_id))

    def test_user_id_is_public_class_attribute(self):
        self.assertEqual(str, type(Review.user_id))

    def test_text_is_public_class_attribute(self):
        self.assertEqual(str, type(Review.text))
