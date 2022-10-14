#!/usr/bin/python3
"""Defines the HBnB console."""
from ast import Not
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
        """Prints the string representation of an instance
        based on the class name and id"""
        # Do the print if the class name is missing.
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            # Split the Classes when found a space
            # and compare the arg with the class in Classes 
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

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        if arg is not "":
            words = arg.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                # If it is equal, search it in storage and print it into string. 
                lis = [str(obj) for key, obj in storage.all().items()
                    if type(obj).__name__ == words[0]]
                print(lis)
        else:
            # If found an arg equal to a class print it
            lis = [str(obj) for key, obj in storage.all().items()]
            print(lis)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
