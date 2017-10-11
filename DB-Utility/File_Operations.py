#!/usr/bin/python
import os
import Text_Operations
def checkPath(path):
    
    isValidPath = False
    
    if os.path.exists(path) and len(path) >= 3:
       
        isValidPath = True
        
    else:
        Text_Operations.cls()
        Text_Operations.errorText('Invalid Path !!')    
        isValidPath = False
    return isValidPath 
 
 
def makeNewSaveDir(svaePath):
    wasCreated = None
    try:
        os.makedirs(path)
    except OSError as exc:  
        if  not exc.errno:
            wasCreated = True
        else:
            wasCreated = False
    return wasCreated 