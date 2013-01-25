#!/usr/bin/env python

from AppKit import *
import os
import pickle

command = "opendiff"
datafile = "~/.xdiff_shared"

pasteb = NSPasteboard.generalPasteboard()
copiedsubpath = pasteb.stringForType_(NSStringPboardType)

print "compare: "+copiedsubpath

base1 = os.getenv("cmp1")
base2 = os.getenv("cmp2")

path1 = copiedsubpath
path2 = copiedsubpath

if path1[0] == "/":
    path1 = path1[1:]
if path2[0] == "/":
   path2 = path2[1:]

path1 = os.path.join(base1,path1)
path2 = os.path.join(base2,path2)

shared = {"cmppath1":path1,"cmppath2":path2}
fp = open(".xdiff_shared","w+")
pickle.dump(shared,fp)
fp.close()
    
commandline = command+ " "+path1+" "+path2

print commandline

os.system(commandline)
