#!/usr/bin/python3
"""[summary]
"""

import sys
import models
import unittest
from io import StringIO
from console import HBNBCommand
from unittest.mock import create_autospec


class TestConsole(unittest.TestCase):
    """[summary]

    Args:
        unittest ([type]): [description]
    """
    def setUp(self):
        """[summary]
        """
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def create(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return HBNBCommand()

    def test_create(self):
        """[summary]
        """
        console = self.create()
        console.onecmd("create State")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))
