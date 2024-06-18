import sys
import os
import unittest

# Add the src directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from type_checking import Statistics

class TestStatistics(unittest.TestCase):

    def setUp(self):
        self.data = [10.5, 14.2, 18.6, 20.1, 22.5]
        self.stats = Statistics(self.data)

    def test_mean(self):
        self.assertAlmostEqual(self.stats.mean(), 17.18, places=2)

    def test_median(self):
        self.assertAlmostEqual(self.stats.median(), 18.6, places=2)

    def test_variance(self):
        self.assertAlmostEqual(self.stats.variance(), 18.1924, places=2)

    def test_standard_deviation(self):
        self.assertAlmostEqual(self.stats.standard_deviation(), 4.263, places=2)

    def test_empty_data(self):
        with self.assertRaises(ValueError):
            empty_stats = Statistics([])
            empty_stats.mean()

if __name__ == "__main__":
    unittest.main()
