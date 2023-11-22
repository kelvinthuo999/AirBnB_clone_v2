#!/usr/bin/python3
"""module instantiates an object of class depending on HBNB_TYPE_STORAGE"""
import os
from models.engine.file_storage import FileStorage


HBNB_TYPE_STORAGE = os.environ.get('HBNB_TYPE_STORAGE')

if HBNB_TYPE_STORAGE == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
