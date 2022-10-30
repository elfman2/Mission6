import unittest
from unittest.mock import patch
from io import StringIO
import assistant as a
# ref https://ryip.me/posts/python/unittest-stdout-stderr/

class TestCLI(unittest.TestCase):

    @patch('sys.stdout', new_callable = StringIO)
    def test_prompt(self,stdout):
       a.prompt()
       expected_out = '> '
       self.assertEqual(stdout.getvalue(),expected_out)

    def test_sum(self):
      out=a.sum_command(['1', '2','3'])
      index= out.find('6')
      self.assertGreater(index,0)

if __name__ == '__main__':
    unittest.main()
