from time import sleep 
from random import randint
def text(toprint) -> None:
    texttime = 0.03
    toprint = str(toprint)
    for char in toprint:
        print(char,flush=True,end='')
        if char == '.':
            sleep(texttime*20)
        else:
            sleep(texttime)
    print('\n',end='')

def chance(percentage) -> bool:
    if percentage >= randint(0,100):
        return True
    return False