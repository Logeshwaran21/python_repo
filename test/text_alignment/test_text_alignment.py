import unittest
from unittest.mock import patch
from io import StringIO
from python_repo.src.text_alignment.util import text_alignment

class TestTextAlignment(unittest.TestCase):
    def test_text_alignment(self):
        # Expected output
        expected_result = [
            '  H  ',
            ' HHH ',
            'HHHHH',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHHHHHHHHHHHHHH  ',
            ' HHHHHHHHHHHHHHH  ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            '            HHHHH ',
            '             HHH  ',
            '              H   ',
        ]

        # Redirect stdout to capture output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            # Provide an input of 3
            with patch('builtins.input', return_value='3'):
                text_alignment()

        # Get the output and compare
        actual_output = fake_out.getvalue()
        self.assertEqual(actual_output, expected_result)

if __name__ == '__main__':
    unittest.main()
