#!/usr/bin/python3
"""
this script create CLI class for making a custom command interpriter
and starts the CLI when excuted
"""
from models import storage
from models.base_model import BaseModel
import sys
import cmd


def split_str(line):
    """splits strings from the given line"""
    splited = line.split()
    res = []
    index = 0
    while index < len(splited):
        my_str = splited[index]
        if ("'" in my_str) or ('"' in my_str):
            if my_str[0] in ["'", '"']:
                last = len(my_str) - 1
                if my_str[last] in ["'", '"']:
                    res.append(my_str)
                else:
                    jindex = index + 1
                    tmp = splited[index]
                    while jindex < len(splited):
                        jlast = len(splited[jindex]) - 1
                        if splited[jindex][jlast] in ["'", '"']:
                            tmp += " " + splited[jindex]
                            res.append(tmp)
                            index = jindex
                            break
                        tmp += " " + splited[jindex]
                        jindex += 1
                    if jindex >= len(splited):
                        res.append(my_str)
            else:
                res.append(my_str)
        else:
            res.append(my_str)

        index += 1

    done_res = []
    for my_str in res:
        last = len(my_str) - 1
        if my_str[0] in ["'", '"'] and my_str[last] in ["'", '"']:
            done_res.append(my_str[1:last])
        else:
            done_res.append(my_str)
    return done_res


class HBNBCommand(cmd.Cmd):
    """
    my custom CLI class to use
    """

    if sys.stdin.isatty():
        prompt = '(hbnb) '
    else:
        prompt = ''

    def preloop(self):
        """adds prompt before loop starts if not in stdin"""
        if not sys.stdin.isatty():
            print('(hbnb) ')

    def do_quit(self, line):
        """quit command to exit the program"""
        exit()

    def do_EOF(self, line):
        """used to exit when called or when interupt key entered"""
        print("")
        exit()

    def help_EOF(self):
        """prints help for EOF comand"""
        print("exits when EOF commond or ctrl + D is encountered\n")

    def help_quit(self):
        """print a help for quit command"""
        print("Quit command to exit the program\n")

    def emptyline(self):
        """do nothing when empity line is entered"""
        pass

    def do_create(self, class_name):
        """creates an instance of a class and stores it in json file"""
        if not class_name:
            print("** class name missing **")
        elif class_name != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def help_create(self):
        """prints the help info of create command"""
        info = "Creates the specified class\n "
        "prints the id then saves it to json the file\n"
        use = "Usage: create <class name>\n"
        print(info, use)

    def do_show(self, line):
        """finds an instance with specified id and prints its string form"""
        class_name = None
        instance_id = None
        args = []
        if line:
            args = split_str(line)
        if args:
            class_name = args[0]
        if len(args) >= 2:
            instance_id = args[1]
        if not class_name:
            print("** class name missing **")
        elif class_name != "BaseModel":
            print("** class doesn't exist **")
        elif not instance_id:
            print("** instance id missing **")
        else:
            my_key = class_name + "." + instance_id
            if my_key in storage.all().keys():
                print(storage.all()[my_key])
            else:
                print("** no instance found **")

    def help_show(self):
        """prints help for show command"""
        info = "searches for an instance with specified id and class name\n"
        "then prints its string format"
        use = "Usage: show <class name> <instance id>\n"
        print(info, use)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
