#!/usr/bin/python3
"""Module for users Class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class representing an user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
