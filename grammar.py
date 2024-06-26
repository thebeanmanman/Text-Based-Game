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

def AreIs(number):
    if number == 1:
        return 'is'
    elif number == 0 or number > 1:
        return 'are'
    else:
        print('Invalid number')

def Plural(num,word):
    if num == 1:
        return word
    elif num > 1 or num == 0:
        if word == 'enemy':
            return 'enemies'