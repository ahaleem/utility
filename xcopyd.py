#!/usr/bin/env python

import os
import pickle

datafile = "~/.xdiff_shared"

datafile = os.path.expanduser(datafile)
fp = open(datafile)
shared = pickle.load(fp)
fp.close();

path1 = shared["cmppath1"]
path2 = shared["cmppath2"]

commandline = "cp "+path1 + " "+path2
print commandline

os.system(commandline)

fp = open(datafile,"w")
shared["cmppath1"] = " "
shared["cmppath2"] = " "
pickle.dump(shared,fp)
fp.close()
