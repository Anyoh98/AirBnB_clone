#!/usr/bin/env python3
"""This script code for the command lien interpreter that will enable
the user interact with my program
"""


import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {'BaseModel': BaseModel}


class HBNBCommand(cmd.Cmd):
    """ This is the class for the CLI """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Command that exits the program """
        return True

    def do_EOF(self, arg):
        """ Command that exits the program using (Ctrl+D) """
        print()
        return True

    def emptyline(self):
        """ What to do when user hits "enter" w/o writing anything """
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name in classes.keys():
            new_instance = classes[class_name]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Function prints the string representaion of an instance """
        arguments = shlex.split(arg)
        if not arguments:
            print("** class name missing **")
            return
        class_name = arguments[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(arguments) < 2:
            print('** instance id missing **')
            return
        instance_id = arguments[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Function that deletes an instance """
        arguments = shlex.split(arg)
        if len(arguments) == 0:
            print("** class name missing **")
            return
        elif arguments[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(arguments) == 1:
            print("** instance id missing **")
            return
        else:
            key = "{}.{}".format(arguments[0], arguments[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
                return

    def do_all(self, arg):
        """
        Displays the string representaion of all instances, whether they
        belong to a specific class or not e.g $all Basemodel- or simply
        $all
        """
        args = shlex.split(arg)
        instances = []
        if len(args) == 0:
            for obj in storage.all().values():
                instances.append(str(obj))
            print(instances)
        elif args[0] in classes:
            print([str(obj) for obj in storage.all().values()])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        argument = shlex.split(arg)
        if len(argument) < 1:
            print("** class name missing **")
            return
        elif argument[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(argument) == 1:
            print("** instance id missing **")
            return
        elif len(argument) == 2:
            print("** attribute name missing **")
            return
        elif len(argument) == 3:
            print("** value missing **")
            return
        elif len(argument) == 4:
            key = "{}.{}".format(argument[0], argument[1])
            if key in storage.all().keys():
                obj = storage.all()[key]
                if hasattr(obj, argument[2]):
                    attr_type = type(getattr(obj, argument[2]))
                    attr_value = attr_type(argument[3])
                    setattr(obj, argument[2], argument[3])
                    obj.save()
                else:
                    print("** no instance found **")
            else:
                print("** no instance found **")
                return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
