# SED
```bash
# SED Description
usage: sed.py [-h] sed [expression] [[input_file] [[input_file] ...]] [[output_file] [[output_file] ...]]


This is implementation of 'sed' command in linux


positional arguments:

  sed            The linux command will be execute once assigned to command
                 line. Accepting 'S' attribute: to string change/
								 
  [expression]   Expression represent the command 'sed' use. Example:
                 's/old_word/new_word/'
								 
  [input_file]   The file 'sed' will extract data from. If argument not
                 specified: accept 'pipe' string input.
								 
  [output_file]  The file 'sed' write the changes to. If argument not
                 specified: the line will be printed to command line.


optional arguments:

  -h, --help     show this help message and exit

```

__author__ = "Itay Atas"
__email__ = "itayatas10@gmail.com"
__status__ = "Production"
