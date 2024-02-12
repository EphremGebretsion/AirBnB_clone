#!/usr/bin/python3
"""
tests State class
"""
from unittest import TestCase
from models.state import State
from models.base_model import BaseModel
from models import storage


class TestState(TestCase):
    """
    tests State class for correctness and error
    """
    def test_attr(self):
        """checks the attribute it has"""
        self.assertTrue(hasattr(State, "name"))

    def test_store(self):
        """checks if it is properly stored"""
        my_state = State()
        key = my_state.__class__.__name__ + "." + my_state.id
        self.assertTrue(key in storage.all().keys())
