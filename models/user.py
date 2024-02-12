#!/usr/bin/python3
"""
user module that inherit from base_model
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    this class inherits from BaseModel
    adds email, password, first_name, last_name of public class attribute
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
