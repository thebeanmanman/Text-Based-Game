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
def Option(player=None,North=False,South=False,West=False,East=False,Map=False,Other=False,OtherList=[]):
    choice = input('> ').lower()
    if North and choice in moveDict['north']:
        return choice
    elif South and choice in moveDict['south']:
        return choice
    elif West and choice in moveDict['west']:
        return choice
    elif East and choice in moveDict['east']:
        return choice
    elif Other and choice in OtherList:
        return choice
    elif Map and choice == 'map':
        player.DungLvl.printMap()
        return Option(player=player,North=North,South=South,West=West,East=East,Map=Map,Other=Other,OtherList=OtherList)
    else:
        text('Unknown action. Please try again')
        return Option(player=player,North=North,South=South,West=West,East=East,Map=Map,Other=Other,OtherList=OtherList)