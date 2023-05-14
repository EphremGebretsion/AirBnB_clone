""" this is a unit test module for base_model module """
import unittest
from models.base_model import BaseModel
from datetime import datetime


class BaseModelTest(unittest.TestCase):
    """ test class for BaseModel class"""
    def test_value(self):
        """test the values of the time stamps"""
        bb = BaseModel()
        self.assertEqual(bb.created_at, bb.updated_at)
        bb.save()
        self.assertNotEqual(bb.created_at, bb.updated_at)

    def test_types(self):
        """ tests if id is string of not """
        bb = BaseModel()
        self.assertIsInstance(bb.id, str)
        self.assertIsInstance(bb.created_at, datetime)
        self.assertIsInstance(bb.updated_at, datetime)

    def test_to_dict(self):
        """ tests if to_dict returns the right information"""
        bb = BaseModel()
        bb.te = "ephi"
        tes = bb.to_dict()
        self.assertEqual(tes['__class__'], 'BaseModel')
        self.assertIsInstance(tes['created_at'], str)
        self.assertIsInstance(tes['updated_at'], str)
        self.assertEqual(tes['te'], "ephi")


if __name__ == "__main__":
    unittest.main()
