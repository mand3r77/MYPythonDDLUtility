
#!/usr/bin/python

import colorama
from colorama import Fore,Back,Style
import os

def cls():
    os.system('cls')

def errorText(error):
    input(Fore.RED+error+Style.RESET_ALL)               
    cls()

def allCompleteText(complete):
    input(Fore.GREEN+complete+Style.RESET_ALL)               
    cls()

def completeText(complete):
    print(Fore.GREEN+complete+Style.RESET_ALL)               
    cls()  
    

def checkLength(item,desiredMinimumLength):
    
    if len(item) >= desiredMinimumLength:
        validLength = True
    else :
        cls()
        errorText('Invalid schema length !!')        
        validLength = False
    
    return validLength