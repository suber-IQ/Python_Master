# 👉  Pickle Module 
# 🎏  The pickle module implements a fundamental, but powerful algorithm for serializing and de-serializing a python object structure.
# 🎏 Storing data with pickle:- Boolean, integers,floats, complex numbers, (normal and unicode) Strings,Tuples,Lists,Sets and Dectionaries
# 🎏 Pickle Function:- dump() :- dump is called to serialize an object hierarchy.
# 🎏 Pickle Function:- load() :- load is called to de-serialize a data stream.

import pickle

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

# l = ["orange","mango","apple"]

# file=open("writeData.txt","wb")
# pickle.dump(l,file)
# file.close()

# 🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠🌠

f = open("writeData.txt","rb")

l = pickle.load(f)

print(l)