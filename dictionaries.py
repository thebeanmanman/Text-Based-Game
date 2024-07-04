from colours import col

iconDict = {
    'Enemy Room': '[E]',
    'Start Room': '[O]',
    'Player' : f'[{col.red("X")}]',
    'Treasure Room': '[T]'
}
optionDict = {
    'north': ['north','up','n'],
    'south': ['south','down','s'],
    'west': ['west','left','w'],
    'east': ['east','right','e'],
    'yes': ['yes','y','yeah','yea'],
    'open': ['open','open chest'],
    'no': ['no','n','nah','never'],
    'map': ['map','m','dungeon','rooms']
}