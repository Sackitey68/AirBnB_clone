#!/usr/bin/python3
"""module defines a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing user instances"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
