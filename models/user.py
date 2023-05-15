#!/usr/bin/python3

""" create a user class """

from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""


def __str__(self):
    return "[{}] ({}) {}".format("User", self.id, self.__dict__)


def to_dict(self):
    res = (self.__dict__).copy()
    res["__class__"] = "User"
    temp = self.created_at
    res["created_at"] = temp.isoformat()
    temp = self.updated_at
    res["updated_at"] = temp.isoformat()
    return res
