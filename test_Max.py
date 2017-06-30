import unittest
from Max import Max,my_min

class PerfectNumTest(unittest.TestCase):
    
    def test_Max1(self):
        expected_value = ['6421', '8723', '9239']
        test_file="sample1.dat"
        value = Max(test_file)
        self.assertEqual(value, expected_value)

    def test_Max2(self):
        expected_value = ['9867667676', '98676', '9793764']
        test_file="sample2.dat"
        value = Max(test_file)
        self.assertEqual(value, expected_value)

    def test_Max3(self):
        expected_value = ['1111111111111111111111111', '11111111111111111111111111', '111111111111111111111111111']
        test_file="sample3.dat"
        value = Max(test_file)
        self.assertEqual(value, expected_value)

    def test_Max4(self):
        expected_value = ['700','800','900']
        test_file="sample4.dat"
        value = Max(test_file)
        self.assertEqual(value, expected_value)



if __name__ == '__main__':
    unittest.main()
