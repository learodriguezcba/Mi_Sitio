import unittest
from unittest.mock import MagicMock
import sut
import math

class TestMock1(unittest.TestCase):
    def test_1(self):
        math.exp=MagicMock(return_value=2)
        math.sqrt=MagicMock(return_value=4)
        self.assertEqual(sut.supercalc(3),6     )
        
if __name__ == '__main__':
    unittest.main()
