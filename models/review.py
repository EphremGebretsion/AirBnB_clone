#!/usr/bin/python3
"""
Review class created by inheriting from base_model
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class with Place.id, User.id, text
    """
    place_id = ""
    user_id = ""
    text = ""
