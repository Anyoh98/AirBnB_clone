#!/usr/bin/env python3
"""
This script containe unittest code for testing the methods of each
function in the BaseModel class

"""
import unittest
import os
import json
import time
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import uuid
import pep8


class Test_Basemodel(unittest.TestCase):
    """This lass contains the test cases for the base model"""

    def testcode_format(self):
        """ testing pycodestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        rest = pepstylecode.check_files([
            'models/base_model.py',
            'models/__init__.py',
            'models/engine/file_storage.py'
        ])

        self.assertEqual(rest.total_errors, 0,
                         "Found code style errors (and warnings).")

    @classmethod
    def setUpClass(cls):
        """Sets up conditions taht need to be performed for every test"""
        cls.base_model = BaseModel()

    def test_init(self):
        """ This tests the init method of the BaseModel class"""
        base_model = self.base_model
        b2_id = str(uuid.uuid4())
        base_model2 = BaseModel(id=b2_id, country="Cameroon")

        self.assertTrue(hasattr(base_model, 'id'))
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertTrue(hasattr(base_model, 'updated_at'))
        self.assertTrue(hasattr(base_model2, 'id'))
        self.assertTrue(hasattr(base_model2, 'created_at'))
        self.assertTrue(hasattr(base_model2, 'updated_at'))
        self.assertTrue(hasattr(base_model2, 'country'))

        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)
        self.assertIsInstance(base_model2.id, str)
        self.assertIsInstance(base_model2.created_at, datetime)
        self.assertIsInstance(base_model2.updated_at, datetime)
        self.assertIsInstance(base_model2.country, str)

    def test_str(self):
        """Test the __str__ fucntion of the BaseClass model"""

        dic = {
            'id': 'a1b2c3',
            'created_at': '2023-10-15T08:00:00.123456',
            '__class__': 'BaseModel',
            'updated_at': '2023-10-15T09:30:45.678910',
            'score': 95
        }

        object_test = BaseModel(**dic)
        out = "[{}] ({}) {}\n".format(
            type(object_test).__name__, object_test.id,
            object_test.__dict__
        )

    def test_save(self):
        """this tests the save method of the Baseclass model"""
        base_model = self.base_model
        start_time = datetime.now()
        time.sleep(1)
        base_model.save()
        end_time = datetime.now()
        self.assertTrue(start_time <= base_model.updated_at <= end_time)

    def test_to_dict(self):
        """This tests the to_dict method of the basemodle class"""
        obj = BaseModel(age=25)
        obj_dic = obj.to_dict()

        self.assertEqual(obj_dic['__class__'], 'BaseModel')
        self.assertEqual(obj_dic['id'], obj.id)
        self.assertEqual(obj_dic['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dic['updated_at'], obj.updated_at.isoformat())

        self.assertEqual(type(obj_dic['created_at']), str)
        self.assertEqual(type(obj_dic['updated_at']), str)

    def test_save_without_instance(self):
        """Check calling save directly on the class"""
        with self.assertRaises(TypeError):
            BaseModel.save()

    def test_save_with_arguments(self):
        """Check calling save with arguments on an instance."""
        base_model = BaseModel()
        with self.assertRaises(TypeError):
            base_model.save([1, 2, 3])

    def test_save_invalid_argument_numbers(self):
        """Test with invalid argument numbers"""
        base_model = BaseModel()
        with self.assertRaises(TypeError):
            base_model.save([455, 323232, 2323, 2323, 23332])

    def test_save_invalid_argument_string(self):
        """Test with invalid argument string"""
        base_model = BaseModel()
        with self.assertRaises(TypeError):
            base_model.save("THIS IS A TEST")

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
