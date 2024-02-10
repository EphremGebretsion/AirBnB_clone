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
        """
        key = obj.__class__.__name__ + obj.id
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, mode="w") as my_file:
            json.dump(FileStorage.__objects, my_file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if
        the JSON file (__file_path) exists ; otherwise,
        do nothing. If the file doesn’t exist,
        """
        try:
            with open(FileStorage.__file_path, mode="r") as my_file:
                FileStorage.__objects = json.load(my_file)
        except FileNotFoundError:
            pass
