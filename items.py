from system import syst
from grammar import Plural

class Item():
    def __init__(self,name:str,desc:str) -> None:
        self.name = name.title()
        self.rawname = name.lower()
        self.desc = desc

    def showInfo(self):
        syst.text(f'Description: {self.desc}')
        self.onInfo()

class UsableItem(Item):
    def __init__(self, name: str, desc:str,useText:str,price:int,healAmt=0,dmg=0,defence=0,defenceDur=0,strength=0,strengthDur=0) -> None:
        super().__init__(name,desc)
        self.useText = useText
        self.price = price
        self.healAmt = healAmt
        self.dmg = dmg
        self.defence = defence
        self.defenceDur = defenceDur
        self.strength = strength
        self.strengthDur = strengthDur
    
    def use(self,player):
        syst.printStatus()
        syst.text(self.useText)
        syst.enterHint()
        
        if self.healAmt:
            player.heal(self.healAmt)
            syst.printStatus()
            syst.text(syst.col('heal',f'You healed {self.healAmt} health!'))
            syst.enterHint()

        if self.dmg:
            player.takeDamage(self.dmg)
            syst.printStatus()
            syst.text(syst.col('red',f'You took {self.dmg} damage!'))
            syst.enterHint()

        if self.defence:
            player.defence = self.defence
            player.defenceDur = self.defenceDur
            syst.printStatus()
            syst.text(syst.col('defence',f'You gained +{self.defence} defence for {self.defenceDur} {Plural(self.defenceDur,"turn")}!'))
            syst.enterHint()

        if self.strength:
            player.strength = self.strength
            player.strengthDur = self.strengthDur
            syst.printStatus()
            syst.text(syst.col('strength',f'You gained +{self.strength} strength for {self.strengthDur} {Plural(self.strengthDur,"turn")}!'))
            syst.enterHint()

    def onInfo(self):
        if self.healAmt:
            syst.text(syst.col('heal',f'Heals {self.healAmt} health.'))

        if self.dmg:
            syst.text(syst.col('red',f'Deals {self.dmg} damage to you when used.'))

        if self.defence:
            syst.text(syst.col('defence',f'Gives you +{self.defence} defence for {self.defenceDur} {Plural(self.defenceDur,"turn")}.'))

        if self.strength:
            syst.text(syst.col('strength',f'Gives you +{self.strength} strength for {self.strengthDur} {Plural(self.strengthDur,"turn")}.'))

class Weapon(Item):
    def __init__(self,name:str,desc:str,dmg:int,crtch=0,poisonCh=0,poisonDur=0,heal=0,healCh=0) -> None:
        super().__init__(name,desc)
        self.dmg = dmg
        self.crtch = crtch
        self.poisonCh = poisonCh
        self.poisonDur = poisonDur
        self.heal = heal
        self.healCh = healCh

class EnemyWeapon(Weapon):
    def __init__(self, name: str,dmg: int, crtch=0, stealch=0, steal=0,poisonCh=0,poisonDur=0,heal=0,healCh=0,defence=0,defencech=0,defenceDur=0,strength=0,strengthch=0,strengthDur=0) -> None:
        super().__init__(name,'',dmg,crtch,poisonCh,poisonDur,heal,healCh)
        self.stealch = stealch
        self.steal = steal
        self.defencech = defencech
        self.defence = defence
        self.defenceDur = defenceDur
        self.strengthch = strengthch
        self.strength = strength
        self.strengthDur = strengthDur

class PlayerWeapon(Weapon):
    def __init__(self, name: str, dmg: int,rarity='', desc='', crtch=0, poisonCh=0,poisonDur=0,heal=0,healCh=0) -> None:
        super().__init__(name, desc,dmg,crtch,poisonCh,poisonDur,heal,healCh)
        if rarity:
            self.rarname = syst.col(rarity,f'[{rarity.title()}] {self.name}')
            self.name = syst.col(rarity,self.name)

    def onInfo(self):
        syst.text(f'Damage: {self.dmg}')
        if self.crtch > 0:
            syst.text(f'Critical Hit Chance: {int(self.crtch*100)}%')

# Player Weapon Dictionary 
# Stores the stats for each weapon when instantiated
weaponDict = {
    'common': {
        'wooden sword': {
            'dmg':2,
            'crtch':0.05,
            'desc':'A sword made of wood.'
        },
        'stick' : {
            'dmg':1,
            'crtch':0.05,
            'desc': 'Utterly useless.'
        }
    },
    'uncommon': {
        'short bow':{
            'dmg':2,
            'crtch':0.2,
            'desc': 'A short bow'
        }
    },
    'rare' : {
        'iron sword': {
            'dmg':3,
            'crtch':0.09,
            'desc': 'A sword made of iron.'
        }
    },
    'epic' : {
        'great sword' : {
            'dmg':4,
            'crtch':0.05,
            'desc': 'A great sword.'
        }
    },
    'legendary': {
        'diamond sword': {
            'dmg':6,
            'crtch':0.07,
            'desc': 'A sword made of diamonds.'
        },
        'golden stick' : {
            'dmg':4,
            'crtch':1,
            'desc': 'Golden, sticky and WHAAAAT 100% Crtical Hit Chance?!'
        }
    }
}

### Item Dictionary ###
itemDict = {
    # Healing Items
    'apple': {'desc':'A red juicy apple',
              'useText':'You eat the apple.',
              'healAmt': 2,
              'price':3},

    'golden apple': {'desc':'A apple coated in gold',
                     'useText':'You lose a tooth as you bite into the apple.\nWho even came up with the idea of golden apples in the first place?',
                     'healAmt': 8,
                     'dmg' : 1,
                     'price':10},

    'luscious liquorice': {'desc':"This luxurious sweet is known for it's incredible healing capabilities, as well as it's exquisite flavour.",
                           'useText':'You eat the luscious liquorice.',
                           'healAmt':5,
                           'price':6},

    # Defense Items
    'milk' : {'desc':'High in calcium for big strong bones',
              'useText':'You drink the milk.',
              'defence':1,
              'defenceDur':2,
              'price':4},

    'dense durian' : {'desc':'Rumoured to give whoever eats it incredible defensible capabilities.\nAlthough it is also rumoured to be the worst smelling fruit in the land.',
              'useText':'You eat the dense durian, trying your best to ignore the stench...',
              'defence':2,
              'defenceDur':2,
              'price':6},

    'iron ingot' : {'desc':"This doesn't seem very edible...",
                     'useText':'You hesitantly bite into the chunk of iron... Ouch...',
                     'dmg':3,
                     'defence':3,
                     'defenceDur':2,
                     'price':7
    },

    # Strength Items
    'strength potion' : {'desc':"Brewed by the town's local alchemist.\nIt isn't too potent though...",
              'useText':'You drink the strength potion...',
              'strength':1,
              'strengthDur':2,
              'price':4},

    'mighty mango' : {'desc':"Rumoured to give whoever eats it immense strength.\nIt is also renowned for it's incredible flavour.",
              'useText':'You eat the mighty mango...',
              'strength':2,
              'strengthDur':2,
              'price':6},


}
### Enemy Types ###
# '': {'maxhp': , 'gold': , 'xp': , 'attacks': [], 'attacksch': [], 'spawnch': 1},
enemyDict = {
    'misc':
    {
        'Mimic': {'maxhp': 6,
                  'gold': 6,
                  'xp': 6,
                  'attacks': [EnemyWeapon(name='Chomp',dmg=2,crtch=0.15),EnemyWeapon(name='Lunge',dmg=3)],
                  'attacksch': [2,1],
                  'desc' : '',
        }

    },

    # Floors
    1:
    {
        'Goblin': {'maxhp':4,
                   'gold':2,
                   'xp':1,
                   'attacks':[EnemyWeapon(name='Stab',dmg=2,crtch=0.1),EnemyWeapon(name='Steal',dmg=0,steal=1,stealch=1)],
                   'attacksch':[2,1],
                   'spawnch': 1,
                   'desc' : 'You hear a mischievous snicker from behind you.\nYou quickly turn around to see a small green creature brandishing a crudely crafted knife staring intensly at your gold pouch.',
                   },

        'Slime': {'maxhp': 5,
                  'gold': 1,
                  'xp': 2,
                  'attacks': [EnemyWeapon(name='Roll',dmg=1),EnemyWeapon(name='Reshape',dmg=0,heal=1,healCh=0.5)],
                  'attacksch': [3,2],
                  'spawnch': 1,
                  'desc' : "Standing before you, there is a green gelatinous blob.\nThrough its translucent skin, you can see partially digested bones floating in what seems to be it's stomach."
                  },

        'Baby Spider': {'maxhp': 3,
                        'gold': 1,
                        'xp': 1,
                        'attacks': [EnemyWeapon(name='Bite',dmg=1,crtch=0.05),EnemyWeapon(name='Poisonous Bite',dmg=0,poisonCh=1,poisonDur=3)],
                        'attacksch': [2,1],
                        'spawnch': 1,
                        'desc' : 'A faint scuttling sound makes your skin crawl.\nYou glance upward to find a large, sinister spider descending from its web, its beady eyes locked onto you with predatory focus.',
                        },

        'Skeleton' : {'maxhp': 5,
                      'gold': 2,
                      'xp': 2,
                      'attacks': [EnemyWeapon(name='Slash',dmg=1,crtch=0.25),EnemyWeapon(name='Drink Milk',dmg=0,defence=1,defencech=1,defenceDur=2)],
                      'attacksch': [3,1],
                      'spawnch': 1,
                      'desc' : "You hear the clattering of bones echoing throughout the room.\nAs you spin around, you see a gaunt figure emerging from the shadows...\nIts hollow inanimate eye sockets are fixed on you with a menacing gleam.\nThe skeletal remains rattle as it raises an ancient, rusted sword, with its intentions clear."
                      },
    },
    2:
    {
        'Ent' : {
            'maxhp':6,
            'gold':1,
            'xp':3,
            'attacks':[EnemyWeapon(name='Slam',dmg=2),EnemyWeapon(name='Grow Bark',dmg=0,defence=2,defencech=0.5,defenceDur=2)],
            'attacksch':[2,1],
            'spawnch':1,
            'desc' : "A massive figure steps forward, its bark-covered limbs resembling twisted roots.\nIts old weathered eyes depict that it has seen centuries pass and absorbed countless wisdom."
        },
        'Giant Spider': { # Maybe add web ability
            'maxhp': 7,
            'gold':2,
            'xp':4,
            'attacks':[EnemyWeapon(name='Venom Spit',dmg=0,poisonCh=0.4,poisonDur=4),EnemyWeapon(name='Shove',dmg=3),EnemyWeapon(name='IDk',dmg=0,poisonCh=1,poisonDur=4)],
            'attacksch': [2,3,1],
            'spawnch':1,
            'desc' : "A deep, unsettling silence falls over the forest.\nYou turn just in time to see a massive spider emerging from the shadows, its monstrous size making you quiver at the sight of it..."
        },
        'Minotaur' : {
            'maxhp': 8,
            'gold':3,
            'xp':5,
            'attacks':[EnemyWeapon(name='Hoof Stomp',dmg=1,crtch=0.25),EnemyWeapon(name='Axe Chop',dmg=3,crtch=0.1),EnemyWeapon(name='Bull Charge',dmg=2,crtch=0.1)],
            'attacksch': [3,1,2],
            'spawnch':1,
            'desc' : "Rushing out from the shadows, a massive beast with the head of a bull and the body of a warrior snorts angrily, its horns gleaming in the dim light.\nThe beasts eyes lock onto you, and it tightens its grip on a brutal, spiked axe."
        }
        # Minotaur
        # Earth Golem
    }
}

bossDict = {
    1:
    {
        'Cyclops' : {
            'maxhp':12,
            'gold':4,
            'xp':5,
            'attacks':[EnemyWeapon(name='Stomp',dmg=4),EnemyWeapon(name='Boulder Toss',dmg=2,crtch=0.1),EnemyWeapon(name='Roar',dmg=0,strengthch=1,strength=1,strengthDur=2)],
            'attacksch':[2,3,1],
            'desc' : "You feel the ground tremble beneath your feet.\nBefore you stands a towering pale blue figure with a single glaring eye, its gaze locked on you with fierce determination.\nClutched in its massive hand is a jagged boulder, ready to be hurled at anyone who dares challenge its strength."
        }
        # Dragon
    }
}