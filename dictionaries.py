iconDict = {
    'EnemyRoom': '[E]',
    'StartRoom': '[O]',
    'TreasureRoom': '[T]',
    'Unknown Room': '[?]',
    'Blank': '   ',
    'BossRoom': '[B]',
    'Default' : '[✓]'
}

roomDescDict = {
    1: {'clearText': 'It seems you have already cleared this room.',
        'onClear': 'You have cleared this room.',
        'EnemyRoom' : 'You enter a dimly lit room.\nA sense of unease fills you as you step further in the room.',
        'TreasureRoom' : 'You enter a room with a large treasure chest inside.',
        'StartRoom': 'As you enter the dungeon, the air turns cold and damp.\nThe flickering torches cast eerie shadows on the moss-covered walls, and the sound of your footsteps echoes through the darkness.\nThe silence is broken only by the distant drip of water and the skittering of unseen creatures.\nAhead, the passageway splits into multiple paths, each leading deeper into the unknown.\nYour journey into the dungeon begins, and with it, the promise of both danger and reward.',
        'ReEnterStartRoom' : 'You enter the room that you started in.\nAre you sure your not lost?',
        'BossRoom' : 'You cautiously enter the room before you...'
    },
    2: {
        'clearText': 'Judging by the human sized footprints in the soil, you seem to already have been here.',
        'onClear': 'You have cleared this area.',
        'EnemyRoom' : 'As you trek onwards, you stop suddenly as the feeling you are being watched washes over you...',
        'TreasureRoom' : 'Amid some tangled vines, a glint catches your eye.\nYou brush aside the vines to reveal an old, moss-covered chest, seemingly still intact.',
        'StartRoom': "The hard stone beneath your feet transitions to a soft spongy moss, muffling your steps.\nTall trees tower above you, their dense canopy blocking out all but a few shafts of light.\nThis casts the forest floor in a perpetual twilight, shrouding all of the forests secrets in darkness.\nThe sounds of rustling leaves and distant animal calls replace the silence of the dim dungeon, yet something deeply unsettles you about this place.\nThe path ahead spreads out in all directions through the thick forest.\nYet you stop to wonder what may be lurking in the shadows.",
        'ReEnterStartRoom' : 'This place feels familiar...\nAre you sure your not lost?',
        'BossRoom' : 'You cautiously enter the room before you...'
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
    'animationsoff': ['animations off','animation off','no animations','disable animations','text animations off'],
    'animationson': ['animations on','animation on','enable animations','text animations on'],
    'drop': ['drop','drop weapon','equip fists'],
    'weaponinfo' : ['weapon info','weaponinfo','wi','weapon damage','weapon dmg','weapon name','weapon crit','equip info'],
    'exit': ['exit','leave'],
    'buy': ['purchase','buy'],
    'open inventory': ['open invetory','inventory','items','item','open items','open bag','bag'],
    'close inventory': ['close inventory','close items','done','inventory','items','close bag','bag','close','leave','exit','exit inventory','leave inventory'],
    'exit shop': ['exit','leave','exit shop', 'leave shop','exit the shop','leave the shop','exit store','leave store','leave the store','exit the store'],
    'reroll items' : ['rr','reroll','reroll items','reroll shop','refresh','refresh shop','refresh items','reroll the shop','refresh the shop']
}

def levelStat(maxhp=0,dmg=0,crtCh=0):
    return [maxhp,dmg,crtCh]

LevelDict = {
    1:levelStat(maxhp=2),
    2:levelStat(maxhp=2,crtCh=0.01),
    3:levelStat(maxhp=1,dmg=1),
    4:levelStat(maxhp=2),
    5:levelStat(maxhp=2,crtCh=0.02),
    6:levelStat(maxhp=4),
    7:levelStat(maxhp=3,dmg=1),
    8:levelStat(maxhp=5),
    9:levelStat(maxhp=4,dmg=1,crtCh=0.02),
    10:levelStat(maxhp=4,dmg=1,crtCh=0.01),
    11:levelStat(maxhp=5),
    12:levelStat(maxhp=4,dmg=1),
    13:levelStat(maxhp=3,dmg=1,crtCh=0.02),
    14:levelStat(maxhp=5),
    15:levelStat(maxhp=6),
    16:levelStat(maxhp=7),
    17:levelStat(maxhp=8),
    18:levelStat(maxhp=9),
    19:levelStat(maxhp=10),
    20:levelStat(maxhp=11)
}