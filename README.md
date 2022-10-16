<p align="center">
  <img src="https://github.com/bdbaraban/AirBnB_clone/blob/master/assets/hbnb_logo.png" alt="HolbertonBnB logo">
</p>

<h1 align="center">AirBnB clone - The console</h1>

---

## Description:

HolbertonBnB is a complete web application, integrating database storage, 
a back-end API.

> This is the first phase of the Airbnb Clone: the console.
> This repository holds a command interpreter and classes (i.e. BaseModel class
> and several other classes that inherit from it: User, Amenity, City, State, Place,
> Review), and a command interpreter. The command interpreter, like a shell,
> can be activated, take in user input, and perform certain tasks
> to manipulate the object instances.

#### How to Use Command Interpreter
---
| Commands  | Functionality                              |
| --------- | ------------------------------------------ |
| `help`    | displays all commands available            |
| `create`  | creates new object (ex. a new User, Place) |
| `update`  | updates attribute of an object             |
| `destroy` | destroys specified object                  |
| `show`    | retrieve an object from a file, a database |
| `all`     | display all objects in class               |
| `count`   | returns count of objects in specified class|
| `quit`    | exits                                      |

HolbertonBnB utilizes the following classes:

|     | BaseModel | FileStorage | User | State | City | Amenity | Place | Review |
| --- | --------- | ----------- | -----| ----- | -----| ------- | ----- | ------ |
| **PUBLIC INSTANCE ATTRIBUTES** | `id`<br>`created_at`<br>`updated_at` | | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` |
| **PUBLIC INSTANCE METHODS** | `save`<br>`to_dict` | `all`<br>`new`<br>`save`<br>`reload` | "" | "" | "" | "" | "" | "" |
| **PUBLIC CLASS ATTRIBUTES** | | | `email`<br>`password`<br>`first_name`<br>`last_name`| `name` | `state_id`<br>`name` | `name` | `city_id`<br>`user_id`<br>`name`<br>`description`<br>`number_rooms`<br>`number_bathrooms`<br>`max_guest`<br>`price_by_night`<br>`latitude`<br>`longitude`<br>`amenity_ids` | `place_id`<br>`user_id`<br>`text` | 
| **PRIVATE CLASS ATTRIBUTES** | | `file_path`<br>`objects` | | | | | | |

## Storage

The above classes are handled by the abstracted storage engine defined in the 
[FileStorage](./models/engine/file_storage.py) class.

Every time the console is initialized, AirBnB instantiates an instance of 
`FileStorage` called `storage`. The `storage` object is loaded/re-loaded from 
any class instances stored in the JSON file `file.json`. As class instances are 
created, updated, or deleted, the `storage` object is used to register 
corresponding changes in the `file.json`.

### Using the Console

The AirBnB console can be run both interactively and non-interactively. 
To run the console in non-interactive mode, pipe any command(s) into an execution 
of the file `console.py` at the command line.

```
$ echo "help" | python console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)

```

To use the AirBnB console in interactive mode, run the 
file `console.py` by itself:

```
$ python console.py or ./console.py
```

While running in interactive mode, the console displays a prompt for input:

```
$ python console.py
(hbnb) 
```

To quit the console, enter the command `quit`, or input an EOF signal 
(`ctrl-D`).

```
$ python console.py
(hbnb) quit
$
```

```
$ python console.py
(hbnb) EOF
$
```
