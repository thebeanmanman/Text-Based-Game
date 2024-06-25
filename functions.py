#Import modules
from time import sleep 
import random
import os

# Import Dictionaries
from dictionaries import moveDict

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
    if percentage/100 >= random.random():
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
def option(optionList):
    choice = input('> ').lower()
    if choice in optionList:
        return choice
    else:
        text('Unknown action. Please try again')
        return option(optionList)

def moveOption(optionList,player):
    choosing = True
    expandedMoves = moveDict[optionList[0]]
    optionList.pop(0)
    for option in optionList:
        expandedMoves += moveDict[option]
    while choosing:
        choice = input('> ').lower()
        if choice in expandedMoves:
            return choice
        elif choice == 'map':
            player.DungLvl.printMap()
        else:
            text('Unknown action. Please try again')