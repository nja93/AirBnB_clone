#!/usr/bin/python3
"""This Module is responsible for the CLI."""

import cmd
import re
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):

    """Class for the CLI."""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Type Quit to exit the program"""

        return True

    def do_EOF(self, line):
        """Type Ctrl + D : Handles End Of File."""

        print()
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER."""

        pass

    def do_create(self, line):
        """The command Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""

        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            bnb = storage.classes()[line]()
            bnb.save()
            print(bnb.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id."""

        if line == "" or line is None:
            print("** class name missing **")
        else:
            text = line.split(' ')
            if text[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(text) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(text[0], text[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""

        if line == "" or line is None:
            print("** class name missing **")
        else:
            text = line.split(' ')
            if text[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(text) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(text[0], text[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based on the class name or not."""

        if line != "":
            text = line.split(' ')
            if text[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                inst_list = [str(obj) for key, obj in storage.all().items()
                             if type(obj).__name__ == text[0]]
                print(inst_list)
        else:
            n_list = [str(obj) for key, obj in storage.all().items()]
            print(n_list)

    def do_update(self, line):
        """Updates an instance by adding or updating attribute."""

        if line == "" or line is None:
            print("** class name missing **")
            return

        regx = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(regx, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                atts = storage.attributes()[classname]
                if attribute in atts:
                    value = atts[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_count(self, line):
        """Returns a Count of class instance."""

        text = line.split(' ')
        if not text[0]:
            print("** class name missing **")
        elif text[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            count = [
                num for num in storage.all() if num.startswith(
                    text[0] + '.')]
            print(len(count))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
