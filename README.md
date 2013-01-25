utility
=======

xopen.py (open files from pasteboard on the text editor of your choice) usage:
1. Copy either the file name from current directory or full path 
2. python xopen
 
Because there are different program which opens different files sometimes you just want to use only one editor for all files in your code

xdiff.py (opens the opendiff/FileMerge program in Mac):
1. In terminal export the base i.e the different prefixed path of the 2 files to be compared as cmp1 and cmp2
 e.g.
export cmp2=/Users/ahaleem/utility/ 
export cmp1=/Users/ahaleem/utility2/

2. Then every time you want to compare command-c copy the common part of the path of the 2 files e.g. command-c to_compare_file.cpp
3. then on terminal just write ./xdiff.py or python xdiff.py

If you feel you want to open the first/second file in your choosen text editor type:
4. ./xopen.py --index 1 or ./xopen.py --index 2

xcopyd.py (copy the first file onto the second path selected in xdiff.py run earlier):

1. Just type ./xcopyd.py

To avoid copying file names many times.


