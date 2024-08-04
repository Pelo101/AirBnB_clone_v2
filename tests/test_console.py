#!/usr/bin/python3
import unittest
import models
from unittest.mock import patch, MagicMock
from io import StringIO
import sys


from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    @patch('console.HBNBCommand.classes', new_callable=dict)
    def test_do_create(self, mock_classes):
        """Setup mock class and instance"""

        mock_class = MagicMock()
        mock_instance = MagicMock()
        mock_instance.id = "1234"

        """Configure the mock class to return"""

        mock_class.return_value = mock_instance
        mock_classes['MyClass'] = mock_class

        command = HBNBCommand()

        """Capture the output of the print statement"""

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:

            """Test argument"""

            command.do_create('MyClass key="value" number=42')

            mock_class.assert_called_once()
            mock_instance.configure_mock(**{'key': 'value', 'number': 42})
            self.assertEqual(mock_instance.key, 'value')
            self. assertEqual(mock_instance.number, 42)
            mock_instance.save.assert_called_once()

            """check the printed output"""
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "1234")


if __name__ == '__main__':
    unittest.main()
