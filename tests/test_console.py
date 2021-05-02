#!/usr/bin/python3
"""model unitest for base model"""
from console import HBNBCommand
import unittest
import pep8


class TestConsole(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.Checker("console.py", source_code=True)
        result = pep8style.check_all()
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
