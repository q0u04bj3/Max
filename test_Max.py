import unittest
from Max import Max,my_min

class PerfectNumTest(unittest.TestCase):
    
    def test_Max(self):
        self.assertEqual(Max("sample1.dat"), '6421\n8723\n9239')
        
    def test_my_min(self):
        self.assertEqual(my_min([1,5,100]), 1)

if __name__ == '__main__':
    unittest.main()