import unittest
from demoproj.libs import mul_inc

class TestMulInc(unittest.TestCase):

    def test_mul_inc(self):
        self.assertEqual(mul_inc.mul_increase(1), 3, 'Should Equal 3')
