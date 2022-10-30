import unittest
from unittest.mock import patch
from io import StringIO
import assistant as a
class TestCLI(unittest.TestCase):

    @patch('sys.stdout', new_callable = StringIO)
    def test_prompt(self,stdout):
       a.prompt()
       expected_out = '> '
       self.assertEqual(stdout.getvalue(),expected_out)


if __name__ == '__main__':
    unittest.main()
