# Describe the Concepts of Test-driven Development

## Unit Testing

Initial testing phase
Tests the individual units of code written
Should be:
- Granular
- Modular
- Automated (whenever possible)

Unit: The piece of code/automation being tested
Test case: The code performing the test on the unit
Test runner: The script/execution engine for automating test cases

### Python unittest Module

- Built-in unit testing framework
- Create test cases by subclassing unittest.TestCase
- Define tests by creating methods beginning with 'test'
- test functions will utilize assertion methods that will return a pass or a fail depending on the expected/desired results

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

### Postman

Uses the CHAI javascript assertion library
Behavior-driven design (BDD)

In the `Tests` tab for a request call the `pm.test` function

```
pm.test('Response code is 200', function(){
  pm.response.to.have.status(200);
});

pm.test('API Response Speed', function(){
  pm.expect(pm.response.responseTime).to.be.below(2000);
});
```
