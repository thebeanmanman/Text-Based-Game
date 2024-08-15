import random

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