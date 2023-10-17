#!/usr/bin/env python3
""" Unit tests for the FileStorage class """
import unittest
from os import path
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ Test the FileStorage class """

    def setUp(self):
        """ Set up test environment """
        try:
            remove('file.json')
        except Exception:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Clean up test environment """
        try:
            remove('file.json')
        except Exception:
            pass

    def test_empty_objects(self):
        """ Test when there are no objects """
        self.assertEqual(storage.all(), {})

    def test_all(self):
        """ Test the all() method """
        storage_instance = FileStorage()
        obj = storage_instance.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage_instance._FileStorage__objects)

    def test_save_create(self):
        """ Test the save method and object creation """
        obj = BaseModel()
        obj_key = 'BaseModel' + '.' + obj.id
        obj1 = User()
        obj1_key = 'User' + '.' + obj1.id
        obj2 = City()
        obj2_key = 'City' + '.' + obj2.id
        obj3 = Amenity()
        obj3_key = 'Amenity' + '.' + obj3.id
        obj4 = Place()
        obj4_key = 'Place' + '.' + obj4.id
        obj5 = Review()
        obj5_key = 'Review' + '.' + obj5.id
        obj6 = State()
        obj6_key = 'State' + '.' + obj6.id

        self.assertEqual(obj, storage.all()[obj_key])
        self.assertEqual(obj1, storage.all()[obj1_key])
        self.assertEqual(obj2, storage.all()[obj2_key])
        self.assertEqual(obj3, storage.all()[obj3_key])
        self.assertEqual(obj4, storage.all()[obj4_key])
        self.assertEqual(obj5, storage.all()[obj5_key])
        self.assertEqual(obj6, storage.all()[obj6_key])

    def test_new_empty(self):
        """ test the argument"""
        with self.assertRaises(TypeError):
            storage.new()

    def test_new_classes(self):
        """ Test the new method with valid arguments """
        obj = BaseModel(id='123')
        obj_key = 'BaseModel' + '.' + obj.id
        obj1 = User(id='01')
        obj1_key = 'User' + '.' + obj1.id
        obj2 = City(id='02')
        obj2_key = 'City' + '.' + obj2.id
        obj3 = Amenity(id='03')
        obj3_key = 'Amenity' + '.' + obj3.id
        obj4 = Place(id='04')
        obj4_key = 'Place' + '.' + obj4.id
        obj5 = Review(id='05')
        obj5_key = 'Review' + '.' + obj5.id
        obj6 = State(id='06')
        obj6_key = 'State' + '.' + obj6.id

        self.assertEqual(storage.all(), {})
        obj.id = 123
        storage.new(obj)
        storage.new(obj1)
        storage.new(obj2)
        storage.new(obj3)
        storage.new(obj4)
        storage.new(obj5)
        storage.new(obj6)
        self.assertEqual(obj, storage.all()[obj_key])
        self.assertEqual(obj1, storage.all()[obj1_key])
        self.assertEqual(obj2, storage.all()[obj2_key])
        self.assertEqual(obj3, storage.all()[obj3_key])
        self.assertEqual(obj4, storage.all()[obj4_key])
        self.assertEqual(obj5, storage.all()[obj5_key])
        self.assertEqual(obj6, storage.all()[obj6_key])

    def test_reload(self):
        """ Test the reload method """
        obj = BaseModel()
        obj_key = 'BaseModel' + '.' + obj.id
        obj1 = User()
        obj1_key = 'User' + '.' + obj1.id
        obj2 = City()
        obj2_key = 'City' + '.' + obj2.id
        obj3 = Amenity()
        obj3_key = 'Amenity' + '.' + obj3.id
        obj4 = Place()
        obj4_key = 'Place' + '.' + obj4.id
        obj5 = Review()
        obj5_key = 'Review' + '.' + obj5.id
        obj6 = State()
        obj6_key = 'State' + '.' + obj6.id
        storage.save()

        self.assertTrue(path.isfile('file.json'))
        FileStorage._FileStorage__objects = {}

        storage.reload()

        self.assertTrue(obj_key in storage.all().keys())
        self.assertEqual(obj.id, storage.all()[obj_key].id)
        self.assertTrue(obj1_key in storage.all().keys())
        self.assertEqual(obj1.id, storage.all()[obj1_key].id)
        self.assertTrue(obj2_key in storage.all().keys())
        self.assertEqual(obj2.id, storage.all()[obj2_key].id)
        self.assertTrue(obj3_key in storage.all().keys())
        self.assertEqual(obj3.id, storage.all()[obj3_key].id)
        self.assertTrue(obj4_key in storage.all().keys())
        self.assertEqual(obj4.id, storage.all()[obj4_key].id)
        self.assertTrue(obj5_key in storage.all().keys())
        self.assertEqual(obj5.id, storage.all()[obj5_key].id)
        self.assertTrue(obj6_key in storage.all().keys())
        self.assertEqual(obj6.id, storage.all()[obj6_key].id)
