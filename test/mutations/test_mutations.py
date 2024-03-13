import logging
import unittest
from python_repo.src.mutations.util import mutate_string

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(mutate_string("loeesh",2,"g"),"logesh")
    def test_case_2(self):
        self.assertEqual(mutate_string("abracadabra",5,"k"),"abrackdabra")
    def test_case_3(self):
        self.assertEqual(mutate_string("sabasree",1,"u"),"subasree")
if __name__ == '__main__':
    unittest.main()
