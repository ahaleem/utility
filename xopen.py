#!/usr/bin/env python

from AppKit import *
import os

command = "open"
program = "'Komodo Edit'"

pasteb = NSPasteboard.generalPasteboard()
copiedPath = pasteb.stringForType_(NSStringPboardType)

if not os.path.exists(copiedPath):
    copiedPath = os.getcwd+copiedPath
    
commandline = "open "+copiedPath+" -a "+program


if os.path.exists(copiedPath):
    print "xopen executing :: "+commandline
    os.system(commandline)
else:
    print "Cannot find file"
