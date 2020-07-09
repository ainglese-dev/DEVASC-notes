# Construct a Python Unit Test

```
#!/usr/bin/env python

import unittest

def foo():
    return "bar"


class TestRunner2049(unittest.TestCase):
    def test_foo_bar(self):
        self.assertEqual(foo(), "bar")

    def test_for_notbar(self):
        self.assertNotEqual(foo(), "baz")

unittest.main()
```

[See here](../../code_samples/python_and_rest/unit_test.py) for a concrete example.
