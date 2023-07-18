#!/usr/bin/python3

"""
Unittests for command interpreter
"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.cmd = HBNBCommand()

    def tearDown(self):
        self.cmd = None

    def test_quit_command_success(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cmd.onecmd('quit'))
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

    def test_quit_command_with_argument(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cmd.onecmd('quit some_argument'))
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

    # def test_quit_command_uppercase(self):
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         self.assertFalse(self.cmd.onecmd('QUIT'))
    #         output = fake_out.getvalue().strip()
    #         self.assertEqual(output, '')

    def test_quit_command_with_whitespace(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cmd.onecmd('  quit   '))
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

    def test_quit_command_invalid_argument(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertFalse(self.cmd.onecmd('quit123'))
            output = fake_out.getvalue().strip()
            self.assertIsNotNone(
                output, "Expected non-empty output for an invalid command.")

    def test_EOF_command_success(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cmd.onecmd('EOF'))
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

    def test_EOF_command_uppercase(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cmd.onecmd('EOF'))
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

    def test_EOF_command_with_argument(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cmd.onecmd('EOF some_argument'))
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

    def test_EOF_command_with_whitespace(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cmd.onecmd('  EOF   '))
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

    # def test_EOF_command_mixed_case_whitespace(self):
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         self.assertFalse(self.cmd.onecmd(' \n EOf   \n\n\n'))
    #         output = fake_out.getvalue().strip()
    #         self.assertEqual(output, '')

    def test_EOF_command_with_multiple_whitespace(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cmd.onecmd('EOF      '))
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

    def test_EOF_command_with_extra_arguments(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cmd.onecmd('EOF arg1 arg2'))
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

    def test_EOF_command_with_newline(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cmd.onecmd('EOF\n'))
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

    def test_EOF_command_with_multiple_newlines(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cmd.onecmd('EOF\n\n\n'))
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

    # def test_EOF_command_with_mixed_newlines_whitespace(self):
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         self.assertFalse(self.cmd.onecmd(' \n EOf   \n\n\n'))
    #         output = fake_out.getvalue().strip()
    #         self.assertEqual(output, '')

    def test_emptyline_command(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd('')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

    def test_emptyline_command_with_whitespace(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd('    ')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

    def test_emptyline_command_with_tabs(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd('\t\t\t')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

    def test_emptyline_command_with_newline(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd('\n')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

    def test_emptyline_command_with_multiple_newlines(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd('\n\n\n')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

    def test_emptyline_command_with_valid_command(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd('help')
            output_before = fake_out.getvalue().strip()
            self.cmd.onecmd('')
            output_after = fake_out.getvalue().strip()
            self.assertEqual(output_after, output_before)

    # def test_emptyline_command_with_arguments(self):
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         self.cmd.onecmd('help')
    #         output_before = fake_out.getvalue().strip()
    #         self.cmd.onecmd('   some_argument   ')
    #         output_after = fake_out.getvalue().strip()
    #         self.assertEqual(output_after, output_before)

    def test_emptyline_command_with_multiple_commands(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd('help')
            output_before = fake_out.getvalue().strip()
            self.cmd.onecmd('   ')
            self.cmd.onecmd('quit')
            output_after = fake_out.getvalue().strip()
            self.assertEqual(output_after, output_before)

    def test_create_command_success(self):
        classes = [
            'BaseModel', 'Amenity', 'City', 'Place', 'Review', 'State', 'User']
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.cmd.onecmd(f'create {class_name}')
                output = fake_out.getvalue().strip()
                self.assertTrue(output)

    def test_create_command_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd('create')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_create_command_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd('create InvalidClass')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

    def test_show_command_success(self):
        classes = [
            'BaseModel', 'Amenity', 'City', 'Place', 'Review', 'State', 'User']
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.cmd.onecmd(f'show {class_name} existing-id')
                output = fake_out.getvalue().strip()
                self.assertEqual(output, '** no instance found **')

    def test_show_command_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd('show')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_show_command_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd('show InvalidClass')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

    def test_show_command_missing_instance_id(self):
        classes = [
            'BaseModel', 'Amenity', 'City', 'Place', 'Review', 'State', 'User']
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.cmd.onecmd(f'show {class_name}')
                output = fake_out.getvalue().strip()
                self.assertEqual(output, '** instance id missing **')

    def test_destroy_command_success(self):
        classes = [
            'BaseModel', 'Amenity',
            'City', 'Place', 'Review', 'State', 'User']
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.cmd.onecmd(f'destroy {class_name} existing-id')
                output = fake_out.getvalue().strip()
                self.assertEqual(output, '** no instance found **')

    def test_destroy_command_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd('destroy')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_destroy_command_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd('destroy InvalidClass')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

    def test_destroy_command_missing_instance_id(self):
        classes = [
            'BaseModel', 'Amenity', 'City',
            'Place', 'Review', 'State', 'User']
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.cmd.onecmd(f'destroy {class_name}')
                output = fake_out.getvalue().strip()
                self.assertEqual(output, '** instance id missing **')

    def test_all_command_success(self):
        classes = [
            'BaseModel', 'Amenity', 'City',
            'Place', 'Review', 'State', 'User']
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.cmd.onecmd(f'all {class_name}')
                output = fake_out.getvalue().strip()
                self.assertTrue(output)

    def test_all_command_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd('all InvalidClass')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

    def test_update_command_success(self):
        classes = [
            'BaseModel', 'Amenity', 'City',
            'Place', 'Review', 'State', 'User']
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as fake_out:
                # Create an instance of the class and capture the instance ID
                self.cmd.onecmd(f'create {class_name}')
                instance_output = fake_out.getvalue().strip()
                instance_id = instance_output.split()[-1]

                # Test the update command with attribute name and value
                with patch('sys.stdout', new=StringIO()) as fake_out:
                    self.cmd.onecmd(
                         f'update {class_name} {instance_id}\
                             attribute_name "attribute_value"')
                    output = fake_out.getvalue().strip()
                    self.assertEqual(output, '')

    def test_update_command_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd('update')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_update_command_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd('update InvalidClass')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

    def test_update_command_missing_instance_id(self):
        classes = [
            'BaseModel', 'Amenity', 'City',
            'Place', 'Review', 'State', 'User']
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.cmd.onecmd(f'update {class_name}')
                output = fake_out.getvalue().strip()
                self.assertEqual(output, '** instance id missing **')

    def test_update_command_missing_attribute_name(self):
        classes = [
            'BaseModel', 'Amenity', 'City',
            'Place', 'Review', 'State', 'User']
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as fake_out:
                # Create an instance of the class and capture the instance ID
                self.cmd.onecmd(f'create {class_name}')
                instance_output = fake_out.getvalue().strip()
                instance_id = instance_output.split()[-1]

                # Test the update command without attribute name
                with patch('sys.stdout', new=StringIO()) as fake_out:
                    self.cmd.onecmd(f'update {class_name} {instance_id}')
                    output = fake_out.getvalue().strip()
                    self.assertEqual(output, '** attribute name missing **')

    def test_update_command_missing_value(self):
        classes = [
            'BaseModel', 'Amenity', 'City',
            'Place', 'Review', 'State', 'User']
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as fake_out:
                # Create an instance of the class and capture the instance ID
                self.cmd.onecmd(f'create {class_name}')
                instance_output = fake_out.getvalue().strip()
                instance_id = instance_output.split()[-1]

                # Test the update command without value
                with patch('sys.stdout', new=StringIO()) as fake_out:
                    self.cmd.onecmd(
                        f'update {class_name} {instance_id} attribute_name')
                    output = fake_out.getvalue().strip()
                    self.assertEqual(output, '** value missing **')

    def test_create_command_nonexistent_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd('create MyModel')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

    def test_show_command_no_instance_found(self):
        classes = [
            'BaseModel', 'Amenity', 'City',
            'Place', 'Review', 'State', 'User']
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.cmd.onecmd(f'show {class_name} 121212')
                output = fake_out.getvalue().strip()
                self.assertEqual(output, '** no instance found **')

    def test_destroy_command_no_instance_found(self):
        classes = [
            'BaseModel', 'Amenity', 'City',
            'Place', 'Review', 'State', 'User']
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.cmd.onecmd(f'destroy {class_name} 121212')
                output = fake_out.getvalue().strip()
                self.assertEqual(output, '** no instance found **')

    def test_all_command_nonexistent_class_name(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd('all MyModel')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '** class doesn\'t exist **')

    def test_update_command_no_instance_found(self):
        classes = [
            'BaseModel', 'Amenity', 'City', 'Place',
            'Review', 'State', 'User']
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.cmd.onecmd(f'update {class_name} 121212')
                output = fake_out.getvalue().strip()
                self.assertEqual(output, '** no instance found **')


if __name__ == '__main__':
    unittest.main()
    
