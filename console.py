#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json

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

    # def do_create(self, arg):
    #     """Creates an instance"""
    #     if arg == "" or arg is None:
    #         print("** class name missing **")
    #     elif arg not in storage.Classes():
    #         print("** class doesn't exist **")
    #     else:
    #         p = storage.Classes()[arg]() # pone el argumento que le paso
    #         # a la consola y lo transforma en una instancia de la clase que le paso
    #         p.save()
    #         print(p.id)
