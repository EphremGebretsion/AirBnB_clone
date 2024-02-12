#!/usr/bin/python3
"""
test place module fro Place class
"""
from unittest import TestCase
from models import storage
from models.base_model import BaseModel
from models.place import Place


class TestPlace(TestCase):
    """
    tests for correctness and erros for Place
    """
    def test_attr(self):
        """checks attribute existance"""
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "amenity_ids"))

    def test_store(self):
        """tests if instance is added to storage"""
        my_place = Place()
        key = my_place.__class__.__name__ + "." + my_place.id
        self.assertTrue(key in storage.all().keys())
