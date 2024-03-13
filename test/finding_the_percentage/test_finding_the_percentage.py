import unittest
import logging
from python_repo.src.finding_the_percentage import util
logging.basicConfig(level=logging.DEBUG, format="%(message)s" )

class MyTestCase(unittest.TestCase):
    def Test_case_1(self):
        student_marks = {
            "Krishna": [67, 68, 69],
            "Arjun": [70, 98, 63],
            "Malika": [52, 56, 60]
        }
        query_name = "Malika"
        # Expected average score for Malika
        expected_average = 56.0
        # Calculate average using the function
        calculated_average = util.calculate_average(student_marks, query_name)
        logging.debug(f"The average of {query_name} is {expected_average:.2f}")
        # Assert that the calculated average matches the expected average
        self.assertEqual(calculated_average, expected_average)
    def Test_case_2(self):
        student_marks = {
            "logesh": [67, 68, 69],
            "suba": [70, 98, 63],
            "thillai": [52, 56, 60],
            "mani":[23,53,23]
        }
        query_name = "mani"
        # Expected average score for Malika
        expected_average = 33.0
        # Calculate average using the function
        calculated_average = util.calculate_average(student_marks, query_name)
        logging.debug(f"The average of {query_name} is {expected_average:.2f}")

        # Assert that the calculated average matches the expected average
        self.assertEqual(calculated_average, expected_average)
    def Test_case_3(self):
        student_marks = {
            "logesh": [67, 68, 69],
            "suba": [70, 98, 73],
            "thillai": [52, 55, 60],
            "mani":[23,53,24]
        }
        query_name = "suba"
        # Expected average score for Malika
        expected_average = 80.33
        # Calculate average using the function
        calculated_average = util.calculate_average(student_marks, query_name)
        # Assert that the calculated average matches the expected average
        self.assertEqual(calculated_average, expected_average)
if __name__ == '__main__':
    unittest.main()
