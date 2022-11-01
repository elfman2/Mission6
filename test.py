from io import StringIO
from unittest.mock import patch
import unittest
from assistant import *


class TestAssistant(unittest.TestCase):
    @patch('sys.stdin', StringIO('10 10\n'))
    def test_sum(self):
        args = None
        expected_out = '20'
        self.assertEqual(sum_command(args), expected_out)
    ############################
    @patch('sys.stdin', StringIO('-10 20\n'))
    def test_average(self):
        args = None
        expected_out = '5.0'
        self.assertEqual(avg_command(args), expected_out)
    ###########################
    def test_help(self):
        args = None
        string = help_command(args)
        expected_out = string.find('python')
        self.assertGreaterEqual(expected_out, 0)
    ########################

    def test_file_nominal(self):
        args = None
        file = file_command(['test.dat'])
        expected_out = file.find('Fichier')
        self.assertGreaterEqual(expected_out, 0)
    

    def test_file_error2(self):
        file = file_command(['testhuhu.dat'])
        expected_out = file.find('Erreur 2')
        self.assertGreaterEqual(expected_out, 0)
    
    def test_file_error1(self):
        file = file_command([])
        expected_out = file.find('Erreur 1')
        self.assertGreaterEqual(expected_out, 0)
    ##########################
    @patch('sys.stdin', StringIO('jhdjshf\n'))
    def test_commands_function_error3(self):
        command = commands_function()
        expected_out = command.find("Erreur 3:")
        self.assertGreaterEqual(expected_out, 0)

    @patch('sys.stdin', StringIO('help'))
    def test_command_fonction_nominal(self):
        command = commands_function()
        expected_out = command.find('usage')
        self.assertGreaterEqual(expected_out, 0)

















    '''def test_dictionary_command(self):
        input = dictionary_command([])'''
