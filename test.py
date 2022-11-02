from io import StringIO
from unittest.mock import patch
import unittest
from assistant import *


class TestAssistant(unittest.TestCase):
    def test_sum(self):
        args = None
        expected_out = '30'
        self.assertEqual(sum_command(['10', '10', '10']), '30')
        
     ############################
    def test_average(self):
        args = None
        expected_out = '5.0'
        self.assertEqual(avg_command(['-10', '20']), '5.0')
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
    
    ##########################
    def test_dictionary_command(self):
        args = None
        input = dictionary_command(args)
        expected_out = input.find('Erreur 5:')
        self.assertGreaterEqual(expected_out, 0)
    ##########################
    def test_dictionary_command(self):
        args = 'fsdde'
        input = dictionary_command(args)
        expected_out = input.find('Erreur 4:')
        self.assertGreaterEqual(expected_out, 0)
        

