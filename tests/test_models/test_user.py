#!/usr/bin/python3
"""
this test module tests Unit class
from unit module
"""
from unittest import TestCase
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestUser(TestCase):
    """
    tests User for correct attribute and storage integration
    """

    def test_subclass(self):
        """test for checking is subclass of BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_attr(self):
        """test for existance and correct value of attribute"""
        my_user = User()
        self.assertIsInstance(my_user, User)
        key = my_user.__class__.__name__ + "." + my_user.id
        self.assertTrue(key in storage.all())
        self.assertTrue(hasattr(my_user, "id"))
        self.assertTrue(hasattr(my_user, "created_at"))
        self.assertTrue(hasattr(my_user, "updated_at"))
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))
        self.assertIsInstance(my_user.created_at, datetime)
        self.assertIsInstance(my_user.updated_at, datetime)
        self.assertIsInstance(my_user.id, str)
        self.assertTrue(my_user.created_at <= my_user.updated_at)
        my_user1 = User()
        self.assertNotEqual(my_user.id, my_user1.id)

    def test_store(self):
        """tests if instance is added when created"""
        my_user = User()
        key = my_user.__class__.__name__ + "." + my_user.id
        self.assertTrue(key in storage.all().keys())
