#!/usr/bin/python
from difflib import Differ
from pprint import pprint 
import re

d = Differ()
fileOne = open('c:/tstcomp/acct_num.sql', 'r')
fileTwo = open('c:/tstcomp/acct_num1.sql', 'r')
result = list(d.compare(fileOne.readlines(), fileTwo.readlines()))


added = re.compile('((\+) [^,]*)',re.MULTILINE)
subtracted = re.compile('((\-) [^,]*)',re.MULTILINE)

isIdentical = True
line = 1
for item in result:
    a = added.match(item)
    if a:
        print("File Name: \n"+a.group(1) + " Line Number: "+str(line))
        isIdentical = False

    b = subtracted.match(item)
    if b:
        print("File Name: \n"+b.group(1)+ " Line Number: "+str(line))
        isIdentical = False
       
    line+=1
if isIdentical == True:
    print("Identical File")