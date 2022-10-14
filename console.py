#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models import storage

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program."""
        exit()

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print("")
        exit()

    def emptyline(self):
        """Do nothing when receiving an empty line."""
        pass

    def do_create(self, arg):
        print(arg)
        """Creates an instance"""
        if arg == "" or arg is None:
             print("** class name missing **")
        elif arg not in storage.Classes():
            print("** class doesn't exist **")
        else:
            p = storage.Classes()[arg]() # pone el argumento que le paso
         # a la consola y lo transforma en una instancia de la clase que le paso
            p.save()
            print(p.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
