import unittest
import logging
from python_repo.src.finding_the_percentage import util
logging.basicConfig(level=logging.DEBUG, format="%(message)s" )

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        student_marks = {
            "Krishna": [67, 68, 69],
            "Arjun": [70, 98, 63],
            "Malika": [52, 56, 60]
        }
        query_name = "Malika"
        expected_average = 56.0
        calculated_average = util.calculate_average(student_marks, query_name)
        logging.debug(f"The average of {query_name} is {expected_average:.2f}")
        self.assertEqual(calculated_average, expected_average)
    def test_case_2(self):
        student_marks = {
            "logesh": [67, 68, 69],
            "suba": [70, 98, 63],
            "thillai": [52, 56, 60],
            "mani":[23,53,23]
        }
        query_name = "mani"
        expected_average = 33.0
        calculated_average = util.calculate_average(student_marks, query_name)
        logging.debug(f"The average of {query_name} is {expected_average:.2f}")
        self.assertEqual(calculated_average, expected_average)
    def test_case_3(self):
        student_marks = {
            "logesh": [67, 68, 69],
            "suba": [70, 98, 73],
            "thillai": [52, 55, 60],
            "mani":[23,53,24]
        }
        query_name = "suba"
        expected_average = 80.33
        calculated_average = util.calculate_average(student_marks, query_name)
        logging.debug(f"The average of {query_name} is {expected_average:.2f}")
        self.assertAlmostEquals(calculated_average, expected_average, places=2)
if __name__ == '__main__':
    unittest.main()
