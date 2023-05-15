#!/usr/bin/python3

""" this sctipt includes a program for command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ this is a class for our interactive comand interpreter for HBNB"""

    prompt = "(hbnb) "

    def remove_quotes(self, lists):
        lis = lists[:]
        index = 0

        for s in lis:
            if s[0] == '"':
                ll = len(s) - 1
                lis[index] = s[1:ll]
            index += 1
        return lis

    def spliter(self, st):
        i = 0
        lis = []
        count = 0
        big = 0
        inside_q = False

        if st != "":
            if st[0] == '"':
                inside_q = True
            for c in st:
                if (c == '"' and count > 0):
                    inside_q = not inside_q

                count += 1
                if inside_q is True:
                    continue

                if c == " ":
                    lis.append(st[big: count - 1])
                    big = count
                    i += 1
            lis.append(st[big:])

        return self.remove_quotes(lis)

    def get_real(self, val):
        try:
            new = int(val)
        except ValueError:
            try:
                new = float(val)
            except ValueError:
                new = val
        return new

    def do_EOF(self, line):
        """EOF command to exit the program
        """

        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """

        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """ creates a new base model and adds to the JSON file
        """

        if line == "":
            print("** class name missing **")
        elif line not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        else:
            if line == "User":
                new = User()
            else:
                new = BaseModel()
            storage.new(new)
            print(new.id)
            storage.save()

    def do_show(self, line):
        args = self.spliter(line)
        ll = len(args)
        bm = None

        if (ll < 1):
            print("** class name missing **")
        elif (args[0] not in ["BaseModel", "User"]):
            print("** class doesn't exist **")
        elif (ll < 2):
            print("** instance id missing **")
        else:
            k = args[0] + "." + args[1]
            all_stored = storage.all()

            if k in all_stored:
                bm = all_stored[k]
                if args[0] == "User":
                    rl = User(**bm)
                else:
                    rl = BaseModel(**bm)
                print(rl)
            else:
                print("** no instande found **")

    def do_destroy(self, line):
        args = self.spliter(line)
        ll = len(args)

        if (ll < 1):
            print("** class name missing **")
        elif (args[0] != "BaseModel"):
            print("** class doesn't exist **")
        elif (ll < 2):
            print("** instance id missing **")
        else:
            k = "BaseModel." + args[1]
            all_stored = storage.all()

            if k in all_stored:
                all_stored.pop(k)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        if line == "BaseModel" or line == "":
            all_stored = storage.all()
            lis = []
            for key in all_stored:
                bm = all_stored[key]
                rl = BaseModel(**bm)
                lis.append(str(rl.__str__()))

            print(lis)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        args = self.spliter(line)
        ll = len(args)

        if (ll < 1):
            print("** class name missing **")
        elif (args[0] != "BaseModel"):
            print("** class doesn't exist **")
        elif (ll < 2):
            print("** instance id missing **")
        else:
            k = "BaseModel." + args[1]
            all_stored = storage.all()

            if k in all_stored:
                if (ll < 3):
                    print("** attribute name missing **")
                elif (ll < 4):
                    print("** value missing **")
                else:
                    real_val = self.get_real(args[3])
                    all_stored[k][args[2]] = real_val
                    storage.save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
