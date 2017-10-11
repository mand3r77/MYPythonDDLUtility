#!/usr/bin/python
import Text_Screens
import Main_Menu_Selection

mainExit = False


while mainExit == False: 
    
    mainSelection = None
    mainSelection = Text_Screens.mainMenu()
    if mainSelection is not None:  
        Main_Menu_Selection.MainMenuSelection(mainSelection)    
                 
    

               
       