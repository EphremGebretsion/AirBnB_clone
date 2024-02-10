"""
This test module is a unit test for
base_model module
"""
from unittest import TestCase
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class TestBaseModle(TestCase):

    def test_init(self):
        """
        tests for a cottect initialization
        """

        my_base = BaseModel()
        self.assertIsInstance(my_base, BaseModel)
        self.assertTrue(hasattr(my_base, "id"))
        self.assertTrue(hasattr(my_base, "created_at"))
        self.assertTrue(hasattr(my_base, "updated_at"))
        self.assertIsInstance(my_base.created_at, datetime)
        self.assertIsInstance(my_base.updated_at, datetime)
        self.assertIsInstance(my_base.id, str)
        self.assertTrue(my_base.created_at <= my_base.updated_at)
        my_base1 = BaseModel()
        self.assertNotEqual(my_base.id, my_base1.id)

    def test_str(self):
        """
        checks the __str__ return value is as needed
        """

        my_base = BaseModel()
        my_str = '[{}] ({}) {}'.format(my_base.__class__.__name__,
                                       my_base.id, my_base.__dict__)
        self.assertEqual(my_base.__str__(), my_str)

    def test_save(self):
        """
        checks if save changes the updated_at time
        """

        my_base = BaseModel()
        old = my_base.updated_at
        my_base.save()
        self.assertNotEqual(old, my_base.updated_at)

    def test_todict(self):
        """
        tests to_dict whether it generates correct output
        or not and to call it in __init__ constructor
        """

        my_base = BaseModel()
        my_json = my_base.to_dict()
        self.assertIsInstance(my_json, dict)
        self.assertTrue("updated_at" in my_json)
        self.assertTrue("created_at" in my_json)
        self.assertTrue("id" in my_json)
        self.assertTrue("__class__" in my_json)
        self.assertIsInstance(my_json["updated_at"], str)
        self.assertIsInstance(my_json["created_at"], str)
        self.assertIsInstance(my_json["id"], str)
        self.assertIsInstance(my_json["__class__"], str)
        new_base = BaseModel(**my_json)
        self.assertIsInstance(new_base, BaseModel)
        self.assertFalse(new_base is my_base)
        self.assertTrue(new_base.created_at == my_base.created_at)
        self.assertTrue(new_base.updated_at == my_base.updated_at)
        self.assertTrue(new_base.id == my_base.id)

    def test_save(self):
        """
        checks if save(self) saves the file into a file
        """
        my_base = BaseModel()
        key = my_base.__class__.__name__ + "." + my_base.id
        self.assertTrue(key in storage.all())
        my_base.save()
        my_base2 = BaseModel()
        key2 = my_base2.__class__.__name__ + "." + my_base2.id
        storage.reload()
        self.assertTrue(key2 not in storage.all())
        my_base2.new = "new attr"
        my_base2.save()
        storage.reload()
        my_all = storage.all()
        self.assertTrue(key2 in my_all)
        my_dict = my_all[key2]
        self.assertTrue("new" in my_dict)
