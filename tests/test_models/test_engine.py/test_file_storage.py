#!/usr/bin/python3

import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "file.json"
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    # def test_all_method_empty(self):
    #     self.assertEqual(self.storage.all(), {})

    def test_new_method(self):
        model = BaseModel()
        model_id = model.id
        self.storage.new(model)
        objects = self.storage.all()
        self.assertIn(f"BaseModel.{model_id}", objects)

    def test_save_method(self):
        model = BaseModel()
        model_id = model.id
        self.storage.new(model)
        self.storage.save()
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            key = f"BaseModel.{model_id}"
            self.assertIn(key, data)

    def test_reload_method(self):
        model = BaseModel()
        model_id = model.id
        self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        objects = self.storage.all()
        key = f"BaseModel.{model_id}"
        self.assertIn(key, objects)
        self.assertTrue(isinstance(objects[key], BaseModel))

if __name__ == '__main__':
    unittest.main()
    
