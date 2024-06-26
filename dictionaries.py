from colours import col

iconDict = {
    'Enemy Room': '[E]',
    'Start Room': '[O]',
    'Player' : f'[{col.red("X")}]',
    'Treasure Room': '[T]'
}
moveDict = {
    'north': ['north','up','n'],
    'south': ['south','down','s'],
    'west': ['west','left','w'],
    'east': ['east','right','e'],
}