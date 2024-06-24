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