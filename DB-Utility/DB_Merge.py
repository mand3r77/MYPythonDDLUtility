#!/usr/bin/python
import os
import re
import difflib
import sqlparse


mergeFromFile = open()

mergeToNames = open('c:/tstindex/created/indexes/mergeTo.txt','r')
mergeToNamesStr = mergeToNames.read()
mergeToFileList = []

mergeFromNames = open('c:/tstindex/created/indexes/mergeFrom.txt','r')
mergeFromNamesStr = mergeFromNames.read()
mergeFromFileList = []

regex = re.compile('(([A-Z])\w+.sql)',re.MULTILINE)

for m in re.finditer(regex,mergeToNamesStr):
    
    mergeToFileList.append(m.group(1))

for m in re.finditer(regex,mergeFromNamesStr):
    
    mergeFromFileList.append(m.group(1))


