#!/usr/bin/python3
""" """
from models.base_model import BaseModel
from models import storage
import unittest
import datetime
from uuid import UUID
import json
import os


class TestBaseModel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                                                       i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        dict_repr = i.to_dict()

        self.assertEqual(dict_repr, i.to_dict())

        if '_sa_instance_state' in dict_repr:
            dict_repr.pop('_sa_instance_state')
            self.assertNotIn('_sa_instance_state', dict_repr)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        try:
            new = self.value(**n)
            self.assertNotIn('Name', new.to_dict())
        except Exception as e:
            self.fail(f"Unexpected exception raised: {e}")

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_delete(self):
        """ """

        obj1 = self.value()
        obj1.id = '3341544b-43a8-4ac0-a5f4-c4003f6325dc'

        storage.new(obj1)
        storage.save()

        key = f"BaseModel.{obj1.id}"
        self.assertIn(key, storage.all())

        storage.delete(obj1)
        storage.save()

        self.assertNotIn(key, storage.all())


if __name__ == '__main__':
    unittest.main()
