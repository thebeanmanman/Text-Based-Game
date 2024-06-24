from functions import col

iconDict = {
    'Enemy Room': '[E]',
    'Start Room': '[O]',
    'Player' : f'[{col.red("X")}]'
}
moveDict = {
    'north': ['north','up','w'],
    'south': ['south','down','s'],
    'west': ['west','left','a'],
    'east': ['east','right','d'],
}