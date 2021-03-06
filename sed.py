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
    This function is the sed implement engine. after checking few cases at the checkers below.
    Sed function also checking for input / out strategy. making sure there is some kind of input.
    IF no input argument found - the function checkes weather the command have been piped. ELSE: ERROR.
    IF no output file added - just print the changes.
    No changed found to initialize? raise errors.

    @param expression: The expression need to be executed from command shell.
    @param input_file: Input file to extract data from.
    @param output_file: Output file to initialize new data.
    """
    # Converting arguments to new string > lists > then creates old and new strings to implement.
    expression = "".join(expression)
    expression_arguments = re.sub("[^\w]", " ", expression).split()
    old_string = expression_arguments[1]
    new_string = expression_arguments[2]
    # Converting arguments from list to strings.
    input_file = "".join(input_file)
    output_file = "".join(output_file)
    #duplicate == IF PIPED AND GOT INPUTFILE.
    duplicate = False

    # Creating new string to initialize.
    # (Effects all the rest of the program, string initialize with pipe or data in input_file.
    string = ""

    # Case not founded file, trying to extract string from pipe. if both failed > raise error.
    if not input_file:
        if piped():
            string = sys.stdin.read()
        else:
            raise argparse.ArgumentTypeError("Cant find any 'string'(Pipe) OR 'input_file'. Please enter valid "
                                             "arguments")

    # Got input_file | Using try,except for making sure the file is 'edit-able'.
    else:
        if piped():  # Checking for multiplye inputs.
            print(sys.stdin.read())
            duplicate = True
        try:
            # Open a file: file
            file = open(input_file, mode='r')
            # read all lines at once
            string = file.read()
            # close the file
            file.close()
        except (OSError, ValueError) as error:
            print(error)

    # changing the expression as added.
    changed_string = re.sub(old_string, new_string, string)

    # Case output_file, trying to initialize the data. if failed > raise error.
    if output_file:
        try:
            # Open a file: file
            file = open(output_file, mode='w')
            file.write(string)
        except (OSError, ValueError) as error:
            print(error)

    # Printing all the changes.
    print("The new output:")
    print("--------------------------------")
    print(changed_string)
    print("--------------------------------")

    if old_string not in string:
        print("sed-engine: [Cant find match of '%s'" % old_string, "in input string.]")
    if duplicate:
        print("sed-engine: [Found 2 arguments, piped and from input_file. Priority == input_file]")


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
    """
    Checking if there is a string in 'piped' command line. example: echo 'hey' | sed '...' ->>> Returns True.
    """
    if not os.isatty(0):
        return True
    else:
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
# Initialize sed-engine:
sed(args.expression, args.input_file, args.output_file)
