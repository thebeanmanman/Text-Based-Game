#Import modules
from time import sleep 
import random
import os

# Import Dictionaries
from dictionaries import optionDict

#Control Variables
ClearTerminal = True
Devmap = True

#Creates a smooth text animation
def text(toprint) -> None:
    for line in str(toprint).split('\n'):
        avoidValues = []
        i = 0
        while i < len(line):
            if line[i] == '\033':
                End = line.find('m',i)
                for j in range(i,End+1):
                    avoidValues.append(j)
                i = End+1
            else:
                i+=1
        texttime = 1/(len(line)-len(avoidValues))
        for charNum,char in enumerate(line):
            print(char,flush=True,end='')
            if char == '.':
                sleep(0.4)
            else:
                if charNum not in avoidValues:
                    sleep(texttime)
        print('\n',end='')

# Returns a Boolean based on a chance of something happening
def chance(percentage) -> bool:
    if percentage >= random.random():
        return True
    return False

#Controls whether the terminal will be cleared or not. Also allows for compatibility between operating systems (Debugging)
def wipe():
    if ClearTerminal:
        os.system('cls' if os.name=='nt' else 'clear')

#Returns a random item from a list
def randItem(list):
    if not list:
        return None
    else:
        return list[random.randint(0,len(list)-1)]

#Returns a players choice from a list of options
def Option(player=None,North=False,South=False,West=False,East=False,Map=False,Other=False,OtherList=[],Yes=False,No=False,Open=False):
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
            player.DungLvl.printHiddenMap(player)
        elif Yes and choice in optionDict['yes']:
            return choice
        elif No and choice in optionDict['no']:
            return choice
        elif Open and choice in optionDict['open']:
            return choice
        # Developer Tools
        elif Devmap and choice == 'devmap':
            player.DungLvl.printMap(player.DungLvl.dispMap)
        else:
            text('Unknown action. Please try again')