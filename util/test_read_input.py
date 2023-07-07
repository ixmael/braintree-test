import unittest

import os
import sys
import shutil

from .read_input import read_input

test_directory = './.test_input_dir'

_stdin = None

class TestInput(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        if not os.path.exists(test_directory):
            os.makedirs(test_directory)

    @classmethod
    def tearDownClass(self):
        shutil.rmtree(test_directory)

    def setUp(self) -> None:
        global _stdin
        _stdin = sys.stdin
    
    def tearDown(self) -> None:
        global _stdin
        sys.stdin = _stdin
    
    def test_no_parameters(self):
        """
        Test that it runs without parameters
        """
        # Simulate arguments of the script call
        sys.argv = [
            'main.py',
        ]

        # Check
        with self.assertRaises(Exception) as context:
            read_input()

        self.assertTrue('There is not a data source' in str(context.exception))

    def test_not_exists_file_parameter(self):
        """
        Test that it not found the file passed as parameter name/path
        """
        # Simulate arguments of the script call
        sys.argv = [
            'main.py',
            '{}/mock_file_not_exists.txt'.format(test_directory),
        ]

        # Check
        with self.assertRaises(Exception) as context:
            read_input()

        self.assertTrue('The file not exists' in str(context.exception))

    def test_not_content_parameter(self):
        """
        Test that it found the file and the content is empty
        """
        filename = '{}/mock_file.txt'.format(test_directory)
        open(filename, 'w').close()

        # Simulate arguments of the script call
        sys.argv = [
            'main.py',
            filename,
        ]

        # Check
        content = read_input()
        self.assertEqual('', content)

    def test_no_content_parameter(self):
        """
        Test that it found the file and the content is empty
        """
        # Simulate arguments of the script call
        sys.argv = [
            'main.py',
        ]

        # Set stdin
        filename = '{}/mock_stdin.txt'.format(test_directory)
        open(filename, 'w').close()
        sys.stdin = open(filename, 'r')

        # Check
        content = read_input()
        self.assertEqual('', content)

        sys.stdin.close()

if __name__ == '__main__':
    unittest.main()