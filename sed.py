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

# /g == global, all words in textfile / string
# /i == ignore cases (upper, lower)
# /p == printing the string / text file
# /w == specific file

# Reading arguments from command line, removing the first "sed.py" argument.

class Sed:
    """
    Sed class is implementation of 'sed' command in Linux environment.
    This class initialize the functional of 'set' command by detecting flags and input/output files/strings
    """

    def __init__(self, arguments):
        """

        """
        # Finding the pattern in function. expecting "S" or "s" for replacing.
        self.function = re.compile('\w+').findall(arguments[0])
        self.sorce = arguments[1:]
        print(self.sorce)
        # if self.function[0].lower == "s":
        print(self.function)


def sedChecker(string):
    """
    @param string: The entered value. accept: 'sed' only.
    @raise
    """
    if string != 'sed':
        raise argparse.ArgumentTypeError("%s is not excepted. Please add 'sed'." % string)
    return string


def expressionChecker(string):
    """
    @param string: The entered value. accept valid expression only. Example: 's/old_word/new_word/'
    @raise
    """
    if string != 'exp':
        raise argparse.ArgumentTypeError("'%s' is not valid expression. Please write valid expression." % string)
    return string


def inputFileChecker(string):
    """
    @param string: The entered value. Checking if input_file OR 'string' via 'PIPE' entered. if not, raise error.
    If the found file, returns the name of the file.
    else: checking if the string entered via PIPE: example: "echo hey | sed 'expression'"
    """
    if os.path.isfile('%s' % (string)):
        return string
    else:
        if not os.isatty(0):
            return sys.stdin.read()
        else:
            raise argparse.ArgumentTypeError("Please enter 'input_file' or pipe a string via command.")


def outputFileChecker(string):
    if os.path.isfile('%s' % (string)):
        return
    else:
        open('%s' % string, "a")
        print("created new file")


# Using parser module for extra functionals in command lines.
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
parser.add_argument('expression', type=expressionChecker, metavar="'expression'",
                    help="Expression represent the command 'sed' use. "
                         "Example: 's/old_word/new_word/' ")
parser.add_argument('input_file', type=inputFileChecker, metavar='input_file',
                    help="The file 'sed' will extract data from. \n If argument not specified: accept 'pipe' string "
                         "input.")
parser.add_argument('output_file', type=outputFileChecker, metavar='output_file',
                    help="The file 'sed' write the changes to.\n If argument not specified: the line will be printed "
                         "to command line.")
args = parser.parse_args()

# checking if the sed is execute via "pipe", meaning a string incoming.

print(cmd)
# Initialize new SED object. future features to detect different flags.
# sed = Sed(script_arguments)
