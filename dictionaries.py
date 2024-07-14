from colours import col

iconDict = {
    'Enemy Room': '[E]',
    'Start Room': '[O]',
    'Player' : f'[{col.red("X")}]',
    'Treasure Room': '[T]',
    'Unknown Room': '[?]',
    'Blank': '   ',
    'Stair Room': '[S]'
}
optionDict = {
    'north': ['north','up','n','u'],
    'south': ['south','down','s','d'],
    'west': ['west','left','w','l'],
    'east': ['east','right','e','r'],
    'yes': ['yes','y','yeah','yea','heck yeah','definitely','sure'],
    'open': ['open','open chest'],
    'no': ['no','n','nah','never'],
    'map': ['map','m','dungeon','rooms']
}