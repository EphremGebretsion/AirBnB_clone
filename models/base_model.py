#!/usr/bin/python3
""" this module includes BaseModel class for managing Airbnb web project"""


import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """ a class will make a model with a unique id with a time stamp"""

    def __init__(self, *args, **kwargs):
        """this is the constructor of the BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = self.created_at
        if (kwargs):
            for key, value in kwargs.items():
                if (key == '__class__'):
                    continue
                if (key in ['created_at', 'updated_at']):
                    form = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(value, form))
                else:
                    setattr(self, key, value)

        storage.new(self)

    def __str__(self):
        """ returns class name id and the dictionart of the class """
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """ updates the updated time of the instance """
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """ converts into a suitable dictionary for making a json file """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = "BaseModel"
        temp = new_dict.pop('created_at')
        new_dict['created_at'] = temp.isoformat()
        temp = new_dict.pop('updated_at')
        new_dict['updated_at'] = temp.isoformat()
        return new_dict
