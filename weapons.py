from colours import col
from functions import text
from entity import Enemy,Entity
from system import syst
from dictionaries import enemyDescDict

class Item():
    def __init__(self,name:str) -> None:
        self.name = name

class Potion(Item):
    def __init__(self, name: str, desc:str) -> None:
        super().__init__(name)
        self.desc = desc
    
    def drink(self,player):
        print(f'You drink the {self.name}!')
        self.onDrink(player)

class HealthPotion(Potion):
    def __init__(self, name: str, desc:str, healAmt:int) -> None:
        super().__init__(name,desc)
        self.healAmt = healAmt
    
    def onDrink(self,player):
        player.heal(self.healAmt)
        syst.printStatus()
        print(f'You healed {self.healAmt} health!')

class Weapon(Item):
    def __init__(self,name:str,dmg:int,crtch=0,poisonCh=0,poisonDmg=0,poisonDur=0,heal=0,healCh=0) -> None:
        super().__init__(name)
        self.dmg = dmg
        self.crtch = crtch
        self.poisonCh = poisonCh
        self.poisonDmg = poisonDmg
        self.poisonDur = poisonDur
        self.heal = heal
        self.healCh = healCh

class EnemyWeapon(Weapon):
    def __init__(self, name: str, dmg: int, crtch=0, stealch=0, steal=0,poisonCh=0,poisonDmg=0,poisonDur=0,heal=0,healCh=0) -> None:
        super().__init__(name,dmg,crtch,poisonCh,poisonDmg,poisonDur,heal,healCh)
        self.stealch = stealch
        self.steal = steal

class PlayerWeapon(Weapon):
    def __init__(self, name: str, dmg: int, desc='', rarity=0, crtch=0, poisonCh=0,poisonDmg=0,poisonDur=0,heal=0,healCh=0) -> None:
        super().__init__(name, dmg,crtch,poisonCh,poisonDmg,poisonDur,heal,healCh)
        self.desc = desc
        self.assignRarity(rarity)

    def assignRarity(self, rarity):
        self.rawname = self.name.lower()
        if rarity == 1:
            common.append(self)
            self.rarname = f'{col.commont} {col.name("common",self.name)}'
            self.name = col.name('common',self.name)
        elif rarity == 2:
            uncommon.append(self)
            self.rarname = f'{col.uncommont} {col.name("uncommon",self.name)}'
            self.name = col.name('uncommon',self.name)
        elif rarity == 3:
            rare.append(self)
            self.rarname = f'{col.raret} {col.name("rare",self.name)}'
            self.name = col.name('rare',self.name)
        elif rarity == 4:
            epic.append(self)
            self.rarname = f'{col.epict} {col.name("epic",self.name)}'
            self.name = col.name('epic',self.name)
        elif rarity == 5:
            legendary.append(self)
            self.rarname = f'{col.legt} {col.name("leg",self.name)}'
            self.name = col.name('leg',self.name)

    def showStats(self):
        text(f'Description: {self.desc}')
        text(f'Damage: {self.dmg}')
        if self.crtch > 0:
            text(f'Critical Hit Chance: {int(self.crtch*100)}%')

common = []
uncommon = []
rare = []
epic = []
legendary = []

### Player Weapons ###
# Common
woodenSword = PlayerWeapon(name='Wooden Sword',dmg=2,crtch=0.05,rarity=1,desc='A sword made of wood.')
stick = PlayerWeapon(name='Stick',dmg=1,desc='Utterly Useless',crtch=0.01,rarity=1)

# Uncommon
shortBow = PlayerWeapon(name='Short Bow',dmg=2,crtch=0.2,desc='A short bow',rarity=2)

# Rare
ironSword = PlayerWeapon(name='Iron Sword',dmg=3,crtch=0.09,rarity=3,desc='A sword made of iron.')

# Epic
greatSword = PlayerWeapon(name='Great Sword',dmg=4,crtch=0.05,rarity=4,desc='A great sword.')

# Legendary
diamondSword = PlayerWeapon(name='Diamond Sword',dmg=6,crtch=0.01,rarity=5,desc='A sword made of diamonds.')
goldenStick = PlayerWeapon(name='Golden Stick',dmg=4,crtch=1,rarity=5,desc='Golden, sticky and WHAAAAT 100% Crtical Hit Chance?!')

### Unobtainable Weapons
fists = PlayerWeapon(name='Fists',dmg=1,desc='Punchy Punchy')
Entity.fists = fists


### Enemy Attacks ###
# Goblin Weapons
goblinStab = EnemyWeapon(name='Stab',dmg=2,crtch=0.1)
goblinSteal = EnemyWeapon(name='Steal',dmg=0,steal=1,stealch=1)

# Mimic Weapons
mimicJaws = EnemyWeapon(name='Chomp',dmg=5,crtch=0.15)
mimicLunge = EnemyWeapon(name='Lunge',dmg=6)

# Baby Spider Weapons
babyspiderFangs = EnemyWeapon(name='Bite',dmg=1,crtch=0.05)
babyspiderPoison = EnemyWeapon(name='Poisonous Bite',dmg=0,poisonCh=1,poisonDmg=1,poisonDur=3)

# Slime Weapons
slimeRoll = EnemyWeapon(name='Roll',dmg=1)
slimeHeal = EnemyWeapon(name='Reshape',dmg=0,heal=1,healCh=0.5)


### Enemy Dictionary ###

# '': {'maxhp': , 'gold': , 'xp': , 'attacks': [], 'attacksch': [],  'desc': enemyDescDict[''], 'spawnch': 1},
enemyDict = {
    'misc':
    {
        'Mimic': {'maxhp': 10, 'gold': 6, 'xp': 6, 'attacks': [mimicJaws,mimicLunge], 'attacksch': [2,1]},
    },

    # Floors
    1:
    {
        'Goblin': {'maxhp':4, 'gold':2, 'xp':1, 'attacks':[goblinStab,goblinSteal], 'attacksch':[2,1],  'desc': enemyDescDict['Goblin'], 'spawnch': 1},
        'Slime': {'maxhp': 5, 'gold': 1, 'xp': 2, 'attacks': [slimeRoll,slimeHeal], 'attacksch': [3,2], 'desc': enemyDescDict['Slime'], 'spawnch': 1},
        'Baby Spider': {'maxhp': 3, 'gold': 1, 'xp': 1, 'attacks': [babyspiderFangs,babyspiderPoison], 'attacksch': [2,1],  'desc': enemyDescDict['Baby Spider'], 'spawnch': 1},
    }
}