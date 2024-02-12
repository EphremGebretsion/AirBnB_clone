#!/usr/bin/python3
"""
this module creates new Amenity class fro base_model
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class with name public class attribute
    """
    name = ""
