import unittest
from decorators_example import example_function, setup_logging

class TestDecorators(unittest.TestCase):

    def setUp(self):
        setup_logging()

    def test_example_function(self):
        # This test mainly checks if the function runs without errors
        example_function(1)

if __name__ == "__main__":
    unittest.main()
