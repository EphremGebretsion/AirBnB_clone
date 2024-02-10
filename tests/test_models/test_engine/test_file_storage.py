"""
tests the storage engine file_storage
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from unittest import TestCase
import os


class TestFileStorage(TestCase):
    """
    test for FileStorage that is used to serialization and decerialization
    """

    def test_attr(self):
        """
        tests for private class attributes
        whether they can be accessed or not
        """

        my_storage = FileStorage()
        with self.assertRaises(AttributeError):
            my_storage.__file_path
        with self.assertRaises(AttributeError):
            my_storage.__objects()
        with self.assertRaises(AttributeError):
            FileStorage.__file_path
        with self.assertRaises(AttributeError):
            FileStorage.__objects()

    def test_fun(self):
        """
        tests if adding a new base instance affects the objects stored
        """

        my_storage = FileStorage()
        my_base = BaseModel()
        my_all = my_storage.all()
        key = my_base.__class__.__name__ + "." + my_base.id
        self.assertTrue(key in my_all)

    def test_empity(self):
        """
        tests what is reloaded from empity file
        """
        my_store = FileStorage()
        my_store.reload()
        self.assertEqual(my_store.all(), {})
