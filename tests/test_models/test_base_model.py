""" this is a unit test module for base_model module """
import unittest
from models.base_model import BaseModel


class BaseModelTest(unittest.TestCase):
    """ test class for BaseModel class"""
    def test_types(self):
        """ tests if id is string of not """
        bb = BaseModel()
        self.assertEqual(type(bb.id), str)

if __name__ == "__main__":
    unittest.main()
