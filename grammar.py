# Modifies text based on how many pieces of text there are
def orChoice(list,And=False):
    text = ''
    if len(list) > 1:
        if And:
            text += ', '.join(list[:-1])
            text += f' and {list[-1]}'
        else:
            text += ', '.join(list[:-1])
            text += f' or {list[-1]}'
    else:
        text += list[0]
    return text

# Returns grammatically correct text based on the number provided
def AreIs(number):
    if number == 1:
        return 'is'
    elif number == 0 or number > 1:
        return 'are'
    else:
        print('Invalid number')

# Returns the plural of a word if the number is more than one
def Plural(num,word):
    if num == 1:
        return word
    elif num > 1 or num == 0:
        return pluralDict[word]

pluralDict = {
    'enemy' : 'enemies',
    'turn' : 'turns'
}