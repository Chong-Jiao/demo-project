import unittest
from demoproj.comm import dec_inc

class TestIndDec(unittest.TestCase):

    def test_increase(self):
        self.assertEqual(dec_inc.increase(1), 2, 'Should Equal 2')
    
    def test_decrease(self):
        self.assertEqual(dec_inc.decrease(2), 1, 'Should Equal 1')
