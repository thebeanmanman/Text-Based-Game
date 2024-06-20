#Import modules
from time import sleep 
import random

def text(toprint) -> None:
    texttime = 0.5/len(toprint)
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

def col(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"