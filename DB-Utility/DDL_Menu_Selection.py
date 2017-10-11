import re
import Text_Screens
import File_Operations
import Text_Operations

isValidPath = False
ddlSelection = None


#Get search path for the file structure to create ddl from
def getSearchPath():
     isValidPath = False
     while isValidPath == False:
          Text_Operations.cls()
          searchPath = input('Enter the EWM-DB Git search path  \n (i.e C:/EWM-DB/): ').upper()
          searchPath = searchPath.replace('\\','/')
          isValidPath = File_Operations.checkPath(searchPath)
     return searchPath

#Get user input for the desired save path if path is valid but does not exsist give option to create     
def getSavePath():

     isValidPath = False
     while isValidPath == False:
          Text_Operations.cls()
          savePath = input('Enter the DLL save path: ').upper()
          savePath = savePath.replace('\\','/')
          isValidPath = File_Operations.checkPath(savePath)
          if isValidPath == False:
               createPath()
          else:
               return savePath   
          
#create new save path                    
def createPath():
     createPath = input('That path does not exsist would you like to try and create it? \n Y\N: ').upper()
     answerReg = re.compile('Y',re.IGNORECASE)
     answerMatch = re.match(createPath)
     if m:
          wasPathCreated = File_Operations.makeNewSaveDir(savePath)
          if wasPathCreated == True:
               return savePath
     else:
          getSavePath()
          
def createDllCall():
     
     ddlSelection = Text_Screens.ddlSelectMenu()
     DDL_Create.createIndividualDDls(savePath,searchPath,schemaNameReplace,ddlSelection)