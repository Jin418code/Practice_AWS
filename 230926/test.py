import unittest
import myfunction

class MyTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(myfunction.sum(2, 5), 7)
    
    def test_multiple(self):
        self.assertEqual(myfunction.multiple(2, 5), 9)