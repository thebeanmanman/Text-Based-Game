#Import modules
from time import sleep 
import random
import os

# Import Dictionaries
from dictionaries import optionDict

#Control Variables
ClearTerminal = True

#Creates a text animation
def text(toprint) -> None:
    texttime = 0.6/(len(''.join(e for e in toprint if e.isalnum())))
    toprint = str(toprint)
    for char in toprint:
        print(char,flush=True,end='')
        if char == '.':
            sleep(texttime*20)
        else:
            sleep(texttime)
    print('\n',end='')

# Returns a Boolean based on a chance of something happening
def chance(percentage) -> bool:
    if percentage >= random.random():
        return True
    return False

#Clears the terminal based on wether 
def wipe():
    if ClearTerminal:
        os.system('cls')

#Returns a random item from a list
def randItem(list):
    if not list:
        return None
    else:
        return list[random.randint(0,len(list)-1)]

#Returns a players choice from a list of options
def Option(player=None,North=False,South=False,West=False,East=False,Map=False,Other=False,OtherList=[],Yes=False,No=False):
    choosing = True
    while choosing:
        choice = input('> ').lower()
        if North and choice in optionDict['north']:
            return choice
        elif South and choice in optionDict['south']:
            return choice
        elif West and choice in optionDict['west']:
            return choice
        elif East and choice in optionDict['east']:
            return choice
        elif Other and choice in OtherList:
            return choice
        elif Map and choice in optionDict['map']:
            player.DungLvl.printMap()
        elif Yes and choice in optionDict['yes']:
            return choice
        elif No and choice in optionDict['no']:
            return choice
        else:
            text('Unknown action. Please try again')