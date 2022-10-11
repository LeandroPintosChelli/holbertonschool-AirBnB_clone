#!/usr/bin/python3
"""Defines the BaseModel class."""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Represents the BaseModel of the project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args: Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())  # Asigna un uuid al id y lo convierte en string
        self.created_at = datetime.now()  # Cuando se crea la instancia se imprime la fecha y hora
        self.updated_at = datetime.now()  # Cuando se crea la instancia se imprime la fecha y hora
        if len(kwargs) != 0:
            for key, value in kwargs.items():  # Devuelve la lista con las keys con valores del diccionario
                if key == "created_at" or key == "updated_at":  # Cuando la key es igual a los strings:
                    self.__dict__[key] = datetime.strptime(value, t_format)  # Strptime, crea un objeto de fecha y hora a partir de una cadena dada
                else:  # Si key no es igual a los strings, lo iguala al value
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()  # Actualiza el atributo publico con la fecha y hora actual
        models.storage.save()

    def to_dict(self):  # Retorna un diccionario con las keys y values de __dict__ de la instancia
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        dictionary = self.__dict__.copy()  # Hace una copia del diccionario
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = dictionary["created_at"].isoformat()  # Lo convierte en ISO format
        dictionary["updated_at"] = dictionary["updated_at"].isoformat()  # Lo convierte en ISO format
        return dictionary

    def __str__(self):
        """Print the str representation of the BaseModel instance."""
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)
