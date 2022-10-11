#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def func_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def func_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
