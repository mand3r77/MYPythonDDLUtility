#!/usr/bin/python
import re
import os
import sqlparse
import Text_Operations
import Text_Screens

def ceateCompleteDDL(savePath,searchPath,searchDirectory,schemaNameReplace):
    for dirpath, dnames, fnames in os.walk(searchPath+"/"):
        for directory in dnames:
            for dirpath, dnames, fnames in os.walk(searchPath+"/"+directory+"/"):    
                if directory == searchDirectory:
                    for f in fnames:
                        fileName = f.upper().replace('.SQL','')
                        
                        file = open(searchPath+"/"+directory+"/"+fileName+".SQL",'r')
                        newFile = open(savePath+'/'+directory+".SQL",'a')
                        replacedSchema = file.read().replace('$(schemaName)',schemaNameReplace)
                        newFile.write(replacedSchema+"\n\n") 
                        newFile.close()


def createIndividualDDls(savePath,searchPath,schemaNameReplace,ddlSelection):
    
    ddlExit = False
    while ddlExit == False:      
        Text_Operations.cls()
        ddlSelection = Menu_Selection.ddlSelectMenu()
        
        if ddlSelection == '1':
            
            searchDirectory = 'Tables'
            ceateCompleteDDL(savePath,searchPath,searchDirectory,schemaNameReplace)
            Text_Operations.completeText('complete')
           
        if ddlSelection == '2':
            
            searchDirectory = 'Constraints'
            ceateCompleteDDL(savePath,searchPath,searchDirectory,schemaNameReplace)
            Text_Operations.completeText('complete')
            
        if ddlSelection == '3':
           
            searchDirectory = 'Indexes'
            ceateCompleteDDL(savePath,searchPath,searchDirectory,schemaNameReplace)
            Text_Operations.completeText('complete')
            
        if ddlSelection == '4':
            
            searchDirectory = 'Sequences'
            ceateCompleteDDL(savePath,searchPath,searchDirectory,schemaNameReplace)
            Text_Operations.completeText('complete')
            
        if ddlSelection == '5':
            
            searchDirectory = 'Stored_Procedures'
            ceateCompleteDDL(savePath,searchPath,searchDirectory,schemaNameReplace)
            Text_Operations.completeText('complete')
            
        if ddlSelection == '6':
            
            searchDirectory = 'Views'
            ceateCompleteDDL(savePath,searchPath,searchDirectory,schemaNameReplace)
            Text_Operations.completeText('complete')
            
        if ddlSelection == '7':
            
            ddlName = input("Enter the name for the DDL:  ")
            checkNameReg = re.compile("\.SQL",re.IGNORECASE)
            
            if re.search(checkNameReg,ddlName) == None:
                ddlName = ddlName +".SQL"
            
                
            directoryList = ['Tables','Constraints','Indexes','Sequences','Views','Stored_Procedures']
            
            for searchDirectory in directoryList:
                print("Adding " + searchDirectory +" to the DDL....")
                ceateCompleteDDL(savePath,searchPath,searchDirectory,schemaNameReplace)
                Text_Operations.completeText(searchDirectory +' complete')
            
            if os.path.exists(savePath+"/EWM_DDL.SQL"):
                os.remove(savePath+"/EWM_DDL.SQL")                
            
            for ddls in directoryList:
                buildDDl(ddls,savePath)
                
        if ddlSelection == '8':
        
            Text_Screens.mainMenu()       
       
            
           