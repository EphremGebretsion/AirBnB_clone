"""
tests the storage engine file_storage
using each attribute and methods
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from unittest import TestCase
import os


class TestFileStorage(TestCase):
    """
    test for FileStorage that is used to serialization and decerialization
    witch tests for apropriate values and types for a file
    """

    def tearDown(self):
        """clean up after each test"""
        my_keys = []
        for key in storage.all().keys():
            my_keys.append(key)
        for key in my_keys:
            del FileStorage._FileStorage__objects[key]

        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_attr(self):
        """
        tests for private class attributes
        whether they can be accessed or not
        """

        with self.assertRaises(AttributeError):
            storage.__file_path
        with self.assertRaises(AttributeError):
            storage.__objects()
        with self.assertRaises(AttributeError):
            FileStorage.__file_path
        with self.assertRaises(AttributeError):
            FileStorage.__objects()
        self.assertTrue(hasattr(storage, "all"))
        self.assertTrue(hasattr(storage, "new"))
        self.assertTrue(hasattr(storage, "save"))
        self.assertTrue(hasattr(storage, "reload"))

    def test_fun(self):
        """
        tests if adding a new base instance affects the objects stored
        """

        my_base = BaseModel()
        key = my_base.__class__.__name__ + "." + my_base.id
        self.assertTrue(key in storage.all())

    def test_save(self):
        """
        tests if it saves to a file or not
        """
        my_base = BaseModel()
        my_base.save()
        storage.reload()
        key = my_base.__class__.__name__ + "." + my_base.id
        self.assertTrue(key in storage.all())
        my_base2 = BaseModel()
        storage.reload()
        key = my_base2.__class__.__name__ + "." + my_base2.id
        self.assertFalse(key in storage.all())
        storage.new(my_base2)
        self.assertTrue(key in storage.all())

    def test_newattr(self):
        """
        tests if new attr updates the dictionaty stored
        if it works the attributes should be included
        """
        my_base = BaseModel()
        my_base.name = "ephi"
        my_base.age = 23
        key = my_base.__class__.__name__ + "." + my_base.id
        self.assertTrue(key in storage.all())
        self.assertTrue(hasattr(storage.all()[key], "name"))
        self.assertTrue(hasattr(storage.all()[key], "age"))
        storage.new(my_base)
        self.assertTrue(key in storage.all())

    def test_empity(self):
        """
        tests what is reloaded from empity file
        """
        storage.reload()
        self.assertEqual(storage.all(), {})

    def test_type(self):
        """
        tests the type stored in __objects
        and what check __object is dict
        """
        my_base = BaseModel()
        key = my_base.__class__.__name__ + "." + my_base.id
        self.assertIsInstance(storage.all(), dict)
        self.assertIsInstance(storage.all()[key], BaseModel)
