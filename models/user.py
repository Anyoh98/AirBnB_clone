#!/usr/bin/env python3
""" This script contains code for the user cllas that inherits from base """

from models.base_model import BaseModel


class User(BaseModel):
    """
    This is the user class that inherits from teh basmodel class.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
