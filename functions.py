#Import modules
from time import sleep 
import random

#Creates a smooth text animation
def text(toprint,end='\n') -> None:
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
        print(end,end='')

# Returns a Boolean based on a chance of something happening
def chance(percentage) -> bool:
    if percentage >= random.random():
        return True
    return False

#Returns a random item from a list
def randItem(list):
    if not list:
        return None
    else:
        return list[random.randint(0,len(list)-1)]