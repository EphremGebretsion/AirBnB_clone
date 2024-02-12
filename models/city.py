#!/usr/bin/python3
"""
this module creates City class by inheriting from base_model
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class with state_id and name
    """
    state_id = ""
    name = ""
