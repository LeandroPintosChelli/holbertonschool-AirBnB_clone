#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
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

    def do_create(self, arg):
        """Creates an instance"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else: 
            if arg in self.Classes:
                new = eval("{}()".format(arg))
                new.save()
                print("{}".format(new.id))
            else:
                print("** class doesn't exist **")

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
