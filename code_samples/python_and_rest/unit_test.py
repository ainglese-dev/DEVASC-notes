#!/usr/bin/env python

import unittest

from rest_with_class_example import SWAPI


class TestSWAPI(unittest.TestCase):
    """
    """

    SWAPI_OBJ = SWAPI()

    def test_find_person_results(self):
        person = self.SWAPI_OBJ.find_person(1)
        self.assertEqual(person["name"], "Luke Skywalker")

    def test_find_person_result_type(self):
        person = self.SWAPI_OBJ.find_person(1)
        self.assertIsInstance(person, dict)

    def test_find_person_invalid_input(self):
        with self.assertRaises(ValueError) as exe:
            self.SWAPI_OBJ.find_person("Luke Skywalker")
        self.assertEqual(
            "Hey dummy you need the person ID, not the name!", str(exe.exception)
        )


unittest.main()
