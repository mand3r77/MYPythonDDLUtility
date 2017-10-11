#!/usr/bin/python

import Text_Operations
def mainMenu():
    mainSelection = None
    Text_Operations.cls()
    print('**********************************************************')
    print('*               1. Create DDL                            *')
    print('*               2. Create SQL files                      *')
    print('*               3. Merge Schemas                         *')
    print('*               4. Exit                                  *')
    print('**********************************************************') 
    
    mainSelection = input('\nSelection : ')  
    Text_Operations.cls()
    return mainSelection

def ddlSelectMenu():
    ddlSelection = None
    Text_Operations.cls()
    print('Select what group you would like to manke a DDL for')
    print('**********************************************************')
    print('*               1. Tables                                *')
    print('*               2. Constraints                           *')
    print('*               3. Indexes                               *')
    print('*               4. Sequences                             *')
    print('*               5. Stored Procedures                     *')
    print('*               6. Views                                 *')
    print('*               7. All                                   *')
    print('*               8. Main Menu                             *')
    print('**********************************************************') 
    ddlSelection = input('\nSelection : ')
    Text_Operations.cls()
    return ddlSelection

def compareMenu():
    compareSelection = None
    Text_Operations.cls()
    print('**********************************************************')
    print('*               1. Compare Idividual Files               *')
    print('*               2. Compare Files in two Directories      *')
    print('*               3. Main Menu                             *')
    print('**********************************************************') 
    
    compareSelection = input('\nSelection : ')  
    Text_Operations.cls()
    
