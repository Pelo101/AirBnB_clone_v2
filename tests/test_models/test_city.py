#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.city import City


class test_City(TestBaseModel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
    print(f"state_id type: {type(new.state_id}")
    self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
    print(f"name type: {type(new.name)}")
    self.assertEqual(type(new.name), str)
