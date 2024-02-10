"""init file to store and reloading from storage file"""
from models.engine import file_storage
storage = file_storage.FileStorage()
storage.reload()
