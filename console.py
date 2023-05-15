#!/usr/bin/python3
"""contains entry point of the CLI"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Represents the console"""
    prompt = "(hbnb)"

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def do_quit(self, arg):
        """Exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
