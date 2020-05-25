#!/usr/bin/env python
# This module is implementation of "SED" function in linux via Python
__author__ = "Itay Atas"
__version__ = "1.0.0"
__email__ = "itayatas10@gmail.com"
__status__ = "Production"

import argparse
import os
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


# Using parser module for extra functionals in command lines.
# argparse.ArgumentParser is the "command" and description of it. auto added -h flag. | usage = initialize expression
parser = argparse.ArgumentParser(prog='sed', usage='%(prog)s [options]')
parser.add_argument('-e', '--expression', type=str, metavar='', help="Expression represent the command 'sed' use. "
                                                                     "Example: 's/hi/bye/' ")
parser.add_argument('input_file', type=str, metavar='', help="The file 'sed' will extract data from")
parser.add_argument('input_file', type=str, metavar='', help="The file 'sed' write the changes to.")
args = parser.parse_args()

args = parser.parse_args()
# checking if the sed is execute via "pipe", meaning a string incoming.
if not os.isatty(0):
    cmd = sys.stdin.read()
else:
    cmd = 0

# Initialize new SED object. future features to detect different flags.
# sed = Sed(script_arguments)
