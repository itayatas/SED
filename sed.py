#!/usr/bin/env python
# This module is implementation of "SED" function in linux via Python
__author__ = "Itay Atas"
__version__ = "1.0.0"
__email__ = "itayatas10@gmail.com"
__status__ = "Production"

import argparse
import os.path
import re
import sys


# re - Regular Expression is the basic usage of "SED" command.
# Import sys for getting argument via console
# argparse module add much more functional to command line/

# /g == global, all words in testfile / piped string
# /i == ignore cases (upper, lower)
# /p == printing the string / text file
# /w == specific file

# Reading arguments from command line, removing the first "sed.py" argument.
def sed(expression, input_file=None, output_file=None):
    """

    """
    # Converting expression iterable list again.
    expression = "".join(expression)
    expression = re.sub("[^\w]", " ", expression).split()

    if not input_file:
        if piped():
            input_file = sys.stdin.read()
            print(input_file)
        else:
            raise argparse.ArgumentTypeError("Cant find any 'string'(Pipe) OR 'input_file'. Please enter valid "
                                             "arguments")
    # Finding the pattern in function. expecting "S" or "s" for replacing.
    # function = re.compile('\w+').findall(arguments[0])
    # sorce = arguments[1:]
    # print(self.sorce)
    # # if self.function[0].lower == "s":
    # print(self.function)


def sedChecker(string):
    """
    accept: 'sed' only. (VERSION 1.0.0)
    @param string: The entered value.
    @raise
    """
    if string != 'sed':
        raise argparse.ArgumentTypeError("%s is not excepted. Please add 'sed'." % string)
    return string


def expressionChecker(string):
    """
    accept valid expression only. Example: 's/old_word/new_word/'
    @param string: The entered value.
    @raise
    """
    # if string.count('/') != 3:
    #     raise argparse.ArgumentTypeError("Please make sure your expression has the right amount of '/'")
    # string = re.sub(r'[^\w]', ' ', string)
    # getting all arguments within 'argument/' expression. meaning, must be a 'slash after the argument'
    arguments = re.findall(r'[a-zA-Z]+/', string)

    # If the expression has any non-alphabetic or '/' symbol in expression. FINDING ONLY ![A-Z]+! symbols
    # Accepting quotes ("",'') only at the end and edges of string.
    if re.sub(r'[a-zA-Z]+/', "", string).replace("'", "").replace('"', "") != "":
        raise argparse.ArgumentTypeError("Please make sure only alphabetic chars or '/' symbol added to expression. ("
                                         "Quotes can be added only to edges)")

    # Deletes all slash in arguments
    arguments = [a.replace('/', '') for a in arguments]
    if arguments[0] != 's':
        raise argparse.ArgumentTypeError(
            "Please make sure your expression has the attribute 's'. example 's/old_word/new_word'")
    if len(arguments) != 3:
        raise argparse.ArgumentTypeError(
            "Please make sure your expression has 3 attributes. example: 's/old_word/new_word'")

    return " ".join(arguments)


def inputFileChecker(string):
    """
    @param string: The entered value.
    Checking if input_file OR 'string' via 'PIPE' entered. if not, raise error.
    If the found file, returns the name of the file.
    else: checking if the string entered via PIPE: example: "echo hey | sed 'expression'"
    """
    if os.path.isfile('%s' % string):
        "print"
        return string
    else:
        raise argparse.ArgumentTypeError("Cant find any file named: %s" % string)


def outputFileChecker(string):
    """
    Checking if there is outfile. if not, creating new one.
    @param string: The entered value.
    """
    if os.path.isfile('%s' % string):
        return
    else:
        open('%s' % string, "a")


def piped():
    if not os.isatty(0):
        return True
    else:
        print("standard behavior")
        return False


# Using parser module for extra functional in command lines.
# argparse.ArgumentParser is the "command" and description of it. auto added -h flag.
# foo = 'sed' function. metavar == 'sed' -> shows in command line.
# expression = '/s/old_word/new_word'. metavar == 'expression' -> shows in command line.
# input_file = the file will be modified. metavar == 'input_file' -> shows in command line.
#   IF NOT ASSIGN: require 'pipe' data. (echo, cat, etc...)
# output_file = the file will initialize with new data. metavar == 'output_file' -> shows in command line.
#   IF NOT ASSIGN: the changes will be printed to command line.


parser = argparse.ArgumentParser(description="This is implementation of 'sed' command in linux")
parser.add_argument('foo', type=sedChecker, metavar='sed',
                    help="The linux command will be execute once assigned to command line. Accepting 'S' attribute: "
                         "to string change/")
parser.add_argument('expression', type=expressionChecker, nargs=1, metavar="[expression]",
                    help="Expression represent the command 'sed' use. "
                         "Example: 's/old_word/new_word/' ")
parser.add_argument('input_file', type=inputFileChecker, nargs="*", metavar='[input_file]',
                    help="The file 'sed' will extract data from. \n If argument not specified: accept 'pipe' string "
                         "input.")
parser.add_argument('output_file', type=outputFileChecker, nargs='*', metavar='[output_file]',
                    help="The file 'sed' write the changes to.\n If argument not specified: the line will be printed "
                         "to command line.")
args = parser.parse_args()
sed(args.expression, args.input_file, args.output_file)
