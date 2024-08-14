iconDict = {
    'EnemyRoom': '[E]',
    'StartRoom': '[O]',
    'TreasureRoom': '[T]',
    'Unknown Room': '[?]',
    'Blank': '   ',
    'BossRoom': '[B]',
    'Default' : '[*]'
}

roomDescDict = {
    1: {'EnemyRoom' : 'You enter a dimly lit room.\nA sense of unease fills you as you step further in the room.',
        'TreasureRoom' : 'You enter a room with a large treasure chest inside.',
        'StartRoom': 'You enter the dungeon...',
        'ReEnterStartRoom' : 'You enter the room that you started in.\nAre you sure your not lost?',
        'BossRoom' : 'You cautiously enter the room before you...'
    },
    2: {
        'EnemyRoom' : 'You enter a dimly lit room.\nA sense of unease fills you as you step further in the room.',
        'TreasureRoom' : 'You enter a room with a large treasure chest inside.',
        'StartRoom': 'You find yourself in a dark forest, surrounded by pine trees looming over you...',
        'ReEnterStartRoom' : 'This place feels familiar...\nAre you sure your not lost?'
    }
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
    'coloursoff': ['colours off','colour off','no colours','disable colours','text colours off'],
    'colourson': ['colours on','colour on','enable colours','text colours on'],
    'drop': ['drop','drop weapon','equip fists'],
    'weaponinfo' : ['weapon info','weaponinfo','wi','weapon damage','weapon dmg','weapon name','weapon crit','equip info'],
    'exit': ['exit','leave'],
    'buy': ['purchase','buy'],
    'open inventory': ['open invetory','inventory','items','item','open items','open bag','bag'],
    'close inventory': ['close inventory','close items','done','inventory','items','close bag','bag','close','leave','exit','exit inventory','leave inventory'],
    'exit shop': ['exit','leave','exit shop', 'leave shop','exit the shop','leave the shop','exit store','leave store','leave the store','exit the store'],
    'reroll items' : ['rr','reroll','reroll items','reroll shop','refresh','refresh shop','refresh items','reroll the shop','refresh the shop']
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