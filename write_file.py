#! /bin/python3.6

from datetime import datetime
import os

f = open("testfile.txt","a+")

f.write("am primit 200 ok in " + str(datetime.now()) + "\r\n")
f.write(os.environ['my_param'] + "\r\n")
f.close()
