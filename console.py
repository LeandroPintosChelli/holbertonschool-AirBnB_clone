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
        """Creates an instance"""
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in storage.Classes():
            print("** class doesn't exist **")
        else:
            p = storage.Classes()[arg]()
        # pone el argumento que le paso
        # a la consola y lo transforma en una instancia de la clase que le paso
            p.save()
            print(p.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        # Do the print if the class name is missing.
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            # Split the Classes based on the id and class name
            # if no one is the id, do the print.
            words = arg.split(' ')
            if words[0] not in storage.Classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                # If key is not found in storage.all, return the list of key.
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            words = arg.split(' ')
        if words[0] not in storage.Classes():
                print("** class doesn't exist **")
        elif len(words) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(words[0], words[1])
            if key not in storage.all():
                print("** no instance found **")
            # If key is found delete it.
            else:
                del storage.all()[key]
                storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
