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
        """
        clean up before starting the test so it does not affect our test
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

        my_keys = []
        for key in storage.all().keys():
            my_keys.append(key)

        for key in my_keys:
            del FileStorage._FileStorage__objects[key]

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
        self.assertTrue(hasattr(my_storage, "all"))
        self.assertTrue(hasattr(my_storage, "new"))
        self.assertTrue(hasattr(my_storage, "save"))
        self.assertTrue(hasattr(my_storage, "reload"))

    def test_fun(self):
        """
        tests if adding a new base instance affects the objects stored
        """

        my_storage = FileStorage()
        my_base = BaseModel()
        my_all = my_storage.all()
        key = my_base.__class__.__name__ + "." + my_base.id
        self.assertTrue(key in my_all)

    def test_save(self):
        """
        tests if it saves to a file or not
        """
        my_storage = FileStorage()
        my_base = BaseModel()
        my_base.save()
        my_storage.reload()
        key = my_base.__class__.__name__ + "." + my_base.id
        self.assertTrue(key in my_storage.all())
        my_base2 = BaseModel()
        my_storage.reload()
        key = my_base2.__class__.__name__ + "." + my_base2.id
        self.assertFalse(key in my_storage.all())
        my_storage.new(my_base2)
        self.assertTrue(key in my_storage.all())

    def test_newattr(self):
        """
        tests if new attr updates the dictionaty stored
        if it works the attributes should be included
        """
        my_storage = FileStorage()
        my_base = BaseModel()
        my_base.name = "ephi"
        my_base.age = 23
        key = my_base.__class__.__name__ + "." + my_base.id
        self.assertTrue(key in my_storage.all())
        self.assertTrue(hasattr(my_storage.all()[key], "name"))
        self.assertTrue(hasattr(my_storage.all()[key], "age"))
        my_storage.new(my_base)
        self.assertTrue(key in my_storage.all())

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
        my_storage = FileStorage()
        key = my_base.__class__.__name__ + "." + my_base.id
        self.assertIsInstance(my_storage.all(), dict)
        self.assertIsInstance(my_storage.all()[key], BaseModel)
