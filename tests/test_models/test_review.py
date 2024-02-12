#!/usr/bin/python3
"""
test review module fro Review class
"""
from unittest import TestCase
from models import storage
from models.base_model import BaseModel
from models.review import Review


class TestCity(TestCase):
    """
    tests for correctness and erros for Review
    """
    def test_attr(self):
        """checks attribute existance"""
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(hasattr(Review, "user_id"))
        self.assertTrue(hasattr(Review, "text"))

    def test_store(self):
        """tests if instance is added to storage"""
        my_review = Review()
        key = my_review.__class__.__name__ + "." + my_review.id
        self.assertTrue(key in storage.all().keys())
