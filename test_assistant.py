from io import StringIO
from unittest.mock import patch
import unittest
import assistant


class TestAssistant(unittest.TestCase):
    @patch('sys.stdin', StringIO('10 10\n'))
    def test_sum(self):
        args = None
        user = assistant.sum_command(args)
        expected_out = '20'
        self.assertEqual(user, expected_out)
    ############################
    @patch('sys.stdin', StringIO('-10 20\n'))
    def test_average(self):
        args = None
        user = assistant.avg_command(args)
        expected_out = '5.0'
        self.assertEqual(user, expected_out)
    ###########################
    def test_help(self):
        args = None
        string = assistant.help_command(args)
        expected_out = string.find('python')
        self.assertGreaterEqual(expected_out, 0)
    ########################

    '''def test_file(self):
        args = None
        file = assistant.file_command(args)
        expected_out = file.find(args)
        self.assert'''
    
        


if __name__ == '__main__':
    unittest.main()



