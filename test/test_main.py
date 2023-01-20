import unittest
from main import StringCalculator



class TestStringCalculator(unittest.TestCase):

    def setUp(self):
        self.main_class = StringCalculator()
        'creating a default instance of the class'

    def test_1_successful_sumNumbers(self):
        """
        run test successful test for comma separated string
        """
        _test_result = self.main_class.Add('1,2,3,4,,,5,6,7,8,9,10')
        self.assertEqual(_test_result, 55)


    def test_2_empty_string(self):
        """
        check for an empty input
        """
        _test_result = self.main_class.Add('')
        self.assertEqual(_test_result, 0)

    def test_3_addNumber(self):
        """
        check for addition of numbers between new lines
        """
        _test_result = self.main_class.Add("1\n2,3")
        print(_test_result)
        self.assertTrue(_test_result == 6)

    def test_4_negativeValues(self):
        """
        check for negative numbers error
        """
        self.assertRaises(Exception,  self.main_class.Add, '-3')
    def test_5_number1000(self):
        """
        check for numbers above 1000
        """
        _test_result =self.main_class.Add('1,2,,5,100,1001')
        self.assertEqual(_test_result, 108)

    def test_6(self):
        _test_result = self.main_class.Add('//;\n1;2')
        self.assertTrue(_test_result == 3)

    def test_7(self):
        _test =self.main_class.Add('//[***]\n1***2***3')
        self.assertEqual(_test, 6)


    def test_8(self):
        _test =self.main_class.Add('//[*][%]\n1*2%3')
        self.assertEqual(_test, 6)




