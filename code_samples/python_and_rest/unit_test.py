#!/usr/bin/env python

import unittest

from rest_with_class_example import SWAPI


class TestSWAPI(unittest.TestCase):
    """
    By subclassing unittest.TestCase we can automatically run every test below
    so long as the method begins with test* when we run our test runner at the
    end.
    """

    # instantiate the SWAPI class
    SWAPI_OBJ = SWAPI()

    def test_find_person_results(self):
        """
        The results for person ID 1 should be about Luke Skywalker. Let's make
        sure the API returns the expected results.
        """
        person = self.SWAPI_OBJ.find_person(1)
        self.assertEqual(person["name"], "Luke Skywalker")

    def test_find_person_result_type(self):
        """
        The results of the find_person() function should be a dict. Let's make
        sure the right type of results are returned.
        """
        person = self.SWAPI_OBJ.find_person(1)
        self.assertIsInstance(person, dict)

    def test_find_person_invalid_input(self):
        """
        The find_person() function requires a numeric ID. Let's make sure our
        exception handling works if we pass alpha characters.

        This example is  little more complex. Since we expect an exception to
        be thrown, we wrap the call inside a context manager so we don't error
        out prior to the assertion. We can then reference the context manager
        object to read the raised exception.
        """
        with self.assertRaises(ValueError) as exe:
            self.SWAPI_OBJ.find_person("Luke Skywalker")
        self.assertEqual(
            "Hey dummy you need the person ID, not the name!", str(exe.exception)
        )


# Run all tests
unittest.main()
