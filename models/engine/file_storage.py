#!/usr/bin/python3

""" this is for serializing and deserializing a json file"""

import os
import json


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        if obj.__class__ == "User":
            FileStorage.__objects[("User." + obj.id)] = obj.to_dict()
        else:
            FileStorage.__objects[("BaseModel." + obj.id)] = obj.to_dict()

    def save(self):
        with open(FileStorage.__file_path, mode="w",
                  encoding="utf-8") as my_file:
            json.dump(FileStorage.__objects, my_file)

    def reload(self):
        if (os.path.isfile(FileStorage.__file_path)):
            fp = FileStorage.__file_path
            with open(fp, mode="r", encoding="utf-8") as mf:
                FileStorage.__objects = json.load(mf)
