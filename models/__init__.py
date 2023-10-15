#!/usr/bin/env python3
""" This script contains a unique instance of the File Storag eclass """


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
