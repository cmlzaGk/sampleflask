import unittest

from bettermathlib import BetterRandom

class BetterMathTestCases(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_better_random(self):
        b = BetterRandom(50,100)
        x = b.random_int()
        self.assertTrue(x >= 50 and x <= 100)
