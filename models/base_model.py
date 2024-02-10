"""
This is a base model class for all the
classes created in this project
"""
from models import storage
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    defines all common attributes and methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        initializes
        id, created_at, updated_at
        and other attributes if specified
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        storage.new(self)

    def __str__(self):
        """
        returns [<class name>] (<self.id>) <self.__dict__> format
        """
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        updates the class and saves to the file
        also changes the updated_at to the current time
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        returns __dict__ but updates:
        adds '__class__' key with class name
        and modifies created_at and updated_at with isoformat
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
