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
    'map': ['map','m','dungeon','rooms'],
    'quit': ['quit','quit game','end game','close game'],
    'hintsoff': ['hints off','hint off','no hints','disable hints'],
    'hintson': ['hints on','hint on','enable hints'],
    'drop': ['drop','drop weapon','equip fists'],
    'weaponinfo' : ['weapon info','weaponinfo','wi','weapon damage','weapon dmg','weapon name','weapon crit','equip info']
}

def levelStat(maxhp=0,fistdmg=0,fistcrt=0):
    return [maxhp,fistdmg,fistcrt]

LevelDict = {
    1:levelStat(maxhp=2),
    2:levelStat(maxhp=2,fistcrt=0.01),
    3:levelStat(maxhp=1,fistdmg=1),
    4:levelStat(maxhp=2),
    5:levelStat(maxhp=2,fistcrt=0.02),
    6:levelStat(maxhp=4),
    7:levelStat(maxhp=3,fistdmg=1),
    8:levelStat(maxhp=5),
    9:levelStat(maxhp=4,fistdmg=1,fistcrt=0.02),
    10:levelStat(maxhp=4,fistdmg=1,fistcrt=0.01),
    11:levelStat(maxhp=5),
    12:levelStat(maxhp=4,fistdmg=1),
    13:levelStat(maxhp=3,fistdmg=1,fistcrt=0.02),
    14:levelStat(maxhp=5),
    15:levelStat(maxhp=6),
    16:levelStat(maxhp=7),
    17:levelStat(maxhp=8),
    18:levelStat(maxhp=9),
    19:levelStat(maxhp=10),
    20:levelStat(maxhp=11)
}