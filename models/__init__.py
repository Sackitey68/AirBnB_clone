#!/usr/bin/python3
"""__init__magic method for model directory"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
