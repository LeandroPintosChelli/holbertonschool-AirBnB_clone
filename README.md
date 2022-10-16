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
| Commands  | Sample Usage                                  | Functionality                              |
| --------- | --------------------------------------------- | ------------------------------------------ |
| `help`    | `help`                                        | displays all commands available            |
| `create`  | `create <class>`                              | creates new object (ex. a new User, Place) |
| `update`  | `User.update('123', {'name' : 'Greg_n_Mel'})` | updates attribute of an object             |
| `destroy` | `User.destroy('123')`                         | destroys specified object                  |
| `show`    | `User.show('123')`                            | retrieve an object from a file, a database |
| `all`     | `User.all()`                                  | display all objects in class               |
| `count`   | `User.count()`                                | returns count of objects in specified class|
| `quit`    | `quit`                                        | exits                                      |
