#Import modules
from time import sleep 
import random

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

class Colour():
    @staticmethod
    def rgb(r, g, b, text):
        return f"\033[38;2;{r};{g};{b}m{text}\033[0m"
    
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