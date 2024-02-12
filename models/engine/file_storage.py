#!/usr/bin/python3
"""
serialization and decerialixation
of json file to instances / instances to json file
"""
import json


class FileStorage:
    """
    serialization and decerialization of instances and files
    to the specified path in this class
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects that are saved from
        or to be saved to the file __file_path
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        used as adding and updating the __objects
        """

        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects that has been added
        to the JSON file (path: __file_path)
        """

        serializable_obj = {}

        for k in FileStorage.__objects.keys():
            serializable_obj[k] = FileStorage.__objects[k].to_dict()

        with open(FileStorage.__file_path, mode="w") as my_file:
            json.dump(serializable_obj, my_file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if
        the JSON file (__file_path) exists ; otherwise,
        do nothing. If the file doesn’t exist,
        """

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        type_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                     "City": City, "Amenity": Amenity, "Place": Place,
                     "Review": Review}
        try:
            deserialized_obj = {}
            with open(FileStorage.__file_path, mode="r") as my_file:
                dict_obj = json.load(my_file)

                for k in dict_obj.keys():
                    my_class = type_dict[dict_obj[k]["__class__"]]
                    deserialized_obj[k] = my_class(**dict_obj[k])
                    FileStorage.__objects = deserialized_obj

        except FileNotFoundError:
            pass
