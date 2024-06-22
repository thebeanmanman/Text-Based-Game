#Import modules
from time import sleep 
import random

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

def chance(percentage) -> bool:
    if percentage/100 >= random.random():
        return True
    return False

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
        option(optionList)

class Colour():
    @staticmethod
    def rgb(r, g, b, text):
        return f"\033[38;2;{r};{g};{b}m{text}\033[0m"
    
    # Regular Colours
    @staticmethod
    def red(text):
        return f"\033[38;2;{255};{0};{0}m{text}\033[0m"    
    
    # Rarity Colours
    @staticmethod
    def common(text):
        return f"\033[38;2;{5};{5};{5}m{text}\033[0m"
    
    @staticmethod
    def uncommon(text):
        return f"\033[38;2;{0};{185};{0}m{text}\033[0m"
    
    @staticmethod
    def rare(text):
        return f"\033[38;2;{0};{0};{255}m{text}\033[0m"
    
    @staticmethod
    def epic(text):
        return f"\033[38;2;{150};{0};{255}m{text}\033[0m"
    
    @staticmethod
    def leg(text):
        return f"\033[38;2;{239};{204};{0}m{text}\033[0m"    

col = Colour()