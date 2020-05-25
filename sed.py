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


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('sed', metavar='', type=str, help="This is implantation of Linux-'sed' command in python.")
parser.add_argument('--sum', dest='accumulate', action='store_const',const=sum, default=max, help='sum the integers (default: find the max)')

# checking if the sed is execute via "pipe", meaning a string incoming.
if not os.isatty(0):
    cmd = sys.stdin.read()
else:
    cmd = 0

# Initialize new SED object. future features to detect different flags.
# sed = Sed(script_arguments)
