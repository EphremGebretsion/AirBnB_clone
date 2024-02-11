#!/usr/bin/python3
"""
this script create CLI class for making a custom command interpriter
and starts the CLI when excuted
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    my custom CLI class to use
    """
    doc_header = 'Documented Commands (type halp <topic>):'
    ruler = '='
    prompt = '(hbnb) '

    def do_quit(self, line):
        """quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """used to exit when called or when interupt key entered"""
        print("")
        return True

    def help_EOF(self):
        """prints help for EOF comand"""
        print("exits when EOF commond or ctrl + D is encountered\n")

    def help_quit(self):
        """print a help for quit command"""
        print("Quit command to exit the program\n")

    def emptyline(self):
        """do nothing when empity line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
