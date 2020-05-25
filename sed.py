#!/usr/bin/env python
# This module is implementation of "SED" function in linux via Python
__author__ = "Itay Atas"
__version__ = "1.0.0"
__email__ = "itayatas10@gmail.com"
__status__ = "Production"

import re
# re - Regular Expression is the basic usage of "SED" command.
import sys

# Import sys for getting argument via console

# /g == global, all words in textfile / string
# /i == ignore cases (upper, lower)
# /p == printing the string / text file
# /w == specific file

# Reading arguments from command line, removing the first "sed.py" argument.

script_arguments = sys.argv[1:]
print(script_arguments)
if not script_arguments:
    sys.exit("Running this script via command-line only. Example: python 'sed s/...")
if script_arguments[0] != "sed":
    sys.exit("Please enter valid 'sed' function. Example: [sed 's/on/forward/' sample.txt] ")


class Sed:
    def __init__(self, *args, old_file=None, new_file=None):
        """

        """
