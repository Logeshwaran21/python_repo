import unittest
import logging
from python_repo.src.collections_namedtuple.util import named_tuple
logging.basicConfig(level=logging.DEBUG, format="%(message)s" )

class MyTestCase(unittest.TestCase):
    def test_average_marks(self):
        self.assertEqual(named_tuple(), 0.0)  # Test with no students

        self.assertEqual(named_tuple(), 85.0)  # Test with one student whose marks are 85

        self.assertEqual(named_tuple(), 90.0)  # Test with one student whose marks are 90

if __name__ == '__main__':
    unittest.main()
