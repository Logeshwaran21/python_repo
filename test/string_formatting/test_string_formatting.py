import unittest
from python_repo.src.string_formating.util import string_formatting

class MyTestCase(unittest.TestCase):
    "testcase for correct input"
    def test_string_format(self):
        expect_out = ''' 1       1       1       1\n 2       2       2      10\n 3       3       3      11\n 4       4       4     100\n'''
        self.assertEqual(string_formatting(4), expect_out)

    "For Invalid input"
    def test_string_format_invalid_input(self):
        # Test case for invalid input (k < 1)
        self.assertEqual(string_formatting(0), '')
if __name__ == '__main__':
    unittest.main()


