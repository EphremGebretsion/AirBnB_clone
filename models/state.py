#!/usr/bin/python3
"""
this module inherits from BaseModel
to create State class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class with name public class attribute
    """
    name = ""
