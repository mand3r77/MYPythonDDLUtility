#!/usr/bin/python

import Text_Operations
import sys
import DDL_Menu_Selection


def MainMenuSelection(mainSelection):
    searchPath = ''
    schemaNameReplace = ''
    minimumSchemaLength = 0
    
    if mainSelection == '1':
        DDL_Menu_Selection.getDDLMenu()
    elif mainSelection == '2':
        isValidPath = False     
        while isValidPath == False :
            sqlFilePath = input("Enter SQL file path : ")
            if os.path.exists(sqlFilePath) and len(sqlFilePath) >= 3:
                sqlFilePath = sqlFilePath.replace('\\','/')
                isValidPath = True
            else:
                os.system('cls')
                errorText('Invalid Path !!')  
        
        isValidPath = False        
        while isValidPath == False :
            sqlFileName = input("Enter bulk sql file name : ")
            if os.path.exists(sqlFilePath+'/'+sqlFileName):
                isValidPath = True
            else:
                os.system('cls')
                errorText('File name not found !!')           
        
        isValidPath = False
        while isValidPath == False:
    
            os.system('cls')
            savePath = input('Enter the sql save path: ').upper()
    
            if os.path.exists(savePath) and len(savePath) >= 3:
                savePath = savePath.replace('\\','/')
                isValidPath = True
            else:  
                try:
                    mkdir_p(savePath)
                except OSError as exc:  # Python >2.5
                    if exc.errno == errno.EEXIST and os.path.isdir(path):
                        isValidPath = True
                    else:
                        errorText('Invalid Path !!')
                        isValidPath = False                
                
        mkdir_p(savePath)
        buildDir(savePath)
        crerateSql(sqlFilePath,sqlFileName,savePath)

    elif mainSelection == '3':
        print('3')
    elif mainSelection == '4':
        sys.exit(input('Goodbye !!'))