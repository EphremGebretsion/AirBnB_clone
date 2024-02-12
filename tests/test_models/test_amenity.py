#!/usr/bin/python3
"""
test amenity module fro amenity class
"""
from unittest import TestCase
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(TestCase):
    """
    tests for correctness and erros for Amenity
    """
    def test_attr(self):
        """checks attribute existance"""
        self.assertTrue(hasattr(Amenity, "name"))

    def test_value(self):
        """test for correct initial value of Amenity attributes"""
        self.assertTrue(Amenity.name == "")

    def test_store(self):
        """tests if instance is added to storage"""
        my_amenity = Amenity()
        key = my_amenity.__class__.__name__ + "." + my_amenity.id
        self.assertTrue(key in storage.all().keys())
