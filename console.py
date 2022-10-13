#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import imp
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import user



class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    Classes = ["State", "City", "Amanity", "Place", "Review"]

    def do_quit(self, args):
        """Quit command to exit the program."""
        exit()

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print("")("")
        exit()

    def emptyline(self):
        """Do nothing when receiving an empty line."""
        pass

    def do_create(self, args):
        """Creates an instance"""
        if args is None:
            print("")("** class name missing **")
        else: 
            if args in self.Classes:
                new = eval("{}()".format(args))
                new.save()
                print("")("{}".format(args.id))
            else:
                print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
