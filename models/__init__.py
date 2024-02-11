#!/usr/bin/python3
"""
init file to store and reloading from the json storage file
this will excute any time the module is imported
so it adds the json file content to the storage instance
"""


from models.engine import file_storage
storage = file_storage.FileStorage()
storage.reload()
