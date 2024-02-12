#!/usr/bin/python3
"""
test city module fro City class
"""
from unittest import TestCase
from models import storage
from models.base_model import BaseModel
from models.city import City


class TestCity(TestCase):
    """
    tests for correctness and erros for City
    """
    def test_attr(self):
        """checks attribute existance"""
        self.assertTrue(hasattr(City, "state_id"))
        self.assertTrue(hasattr(City, "name"))

    def test_store(self):
        """tests if instance is added to storage"""
        my_city = City()
        key = my_city.__class__.__name__ + "." + my_city.id
        self.assertTrue(key in storage.all().keys())
