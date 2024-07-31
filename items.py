from colours import col
from functions import text
from entity import Entity
from system import syst
from dictionaries import enemyDescDict

class Item():
    def __init__(self,name:str,desc:str) -> None:
        self.name = name.title()
        self.rawname = name.lower()
        self.desc = desc

    def showInfo(self):
        text(f'Description: {self.desc}')
        self.onInfo()

class UsableItem(Item):
    def __init__(self, name: str, desc:str,useText:str,price:int) -> None:
        super().__init__(name,desc)
        self.useText = useText
        self.price = price
    
    def use(self,player):
        print(self.useText)
        self.onUse(player)


class HealItem(UsableItem):
    def __init__(self, name: str, desc:str, useText:str,healAmt:int,price:int) -> None:
        super().__init__(name,desc,useText,price)
        self.healAmt = healAmt
    
    def onUse(self,player):
        player.heal(self.healAmt)
        syst.printStatus()
        print(col.name('heal',f'You healed {self.healAmt} health!'))

    def onInfo(self):
        text(col.name('heal',f'Heals {self.healAmt} health.'))

class Weapon(Item):
    def __init__(self,name:str,desc:str,dmg:int,crtch=0,poisonCh=0,poisonDmg=0,poisonDur=0,heal=0,healCh=0) -> None:
        super().__init__(name,desc)
        self.dmg = dmg
        self.crtch = crtch
        self.poisonCh = poisonCh
        self.poisonDmg = poisonDmg
        self.poisonDur = poisonDur
        self.heal = heal
        self.healCh = healCh

class EnemyWeapon(Weapon):
    def __init__(self, name: str,dmg: int, crtch=0, stealch=0, steal=0,poisonCh=0,poisonDmg=0,poisonDur=0,heal=0,healCh=0) -> None:
        super().__init__(name,'',dmg,crtch,poisonCh,poisonDmg,poisonDur,heal,healCh)
        self.stealch = stealch
        self.steal = steal

class PlayerWeapon(Weapon):
    def __init__(self, name: str, dmg: int, desc='', rarity=0, crtch=0, poisonCh=0,poisonDmg=0,poisonDur=0,heal=0,healCh=0) -> None:
        super().__init__(name, desc,dmg,crtch,poisonCh,poisonDmg,poisonDur,heal,healCh)
        self.assignRarity(rarity)

    def assignRarity(self, rarity):
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

    def onInfo(self):
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


### Item Dictionary ###
# '': {'desc':'','useText':'','healAmt': ,'price':}
itemDict = {
    'heal': {
        'apple': {'desc':'A red juicy apple','useText':'You eat the apple.','healAmt': 2,'price':3},
        'golden apple': {'desc':'A apple coated in gold','useText':'You lose a tooth as you bite into the apple.\nWho even came up with the idea of golden apples in the first place?','healAmt': 6,'price':10}
    }
}

### Enemy Types ###
# '': {'maxhp': , 'gold': , 'xp': , 'attacks': [], 'attacksch': [],  'desc': enemyDescDict[''], 'spawnch': 1},
enemyDict = {
    'misc':
    {
        'Mimic': {'maxhp': 10, 'gold': 6, 'xp': 6, 'attacks': [EnemyWeapon(name='Chomp',dmg=5,crtch=0.15),EnemyWeapon(name='Lunge',dmg=6)], 'attacksch': [2,1]},
    },

    # Floors
    1:
    {
        'Goblin': {'maxhp':4, 'gold':2, 'xp':1, 'attacks':[EnemyWeapon(name='Stab',dmg=2,crtch=0.1),EnemyWeapon(name='Steal',dmg=0,steal=1,stealch=1)], 'attacksch':[2,1],  'desc': enemyDescDict['Goblin'], 'spawnch': 1},
        'Slime': {'maxhp': 5, 'gold': 1, 'xp': 2, 'attacks': [EnemyWeapon(name='Roll',dmg=1),EnemyWeapon(name='Reshape',dmg=0,heal=1,healCh=0.5)], 'attacksch': [3,2], 'desc': enemyDescDict['Slime'], 'spawnch': 1},
        'Baby Spider': {'maxhp': 3, 'gold': 1, 'xp': 1, 'attacks': [EnemyWeapon(name='Bite',dmg=1,crtch=0.05),EnemyWeapon(name='Poisonous Bite',dmg=0,poisonCh=1,poisonDmg=1,poisonDur=3)], 'attacksch': [2,1],  'desc': enemyDescDict['Baby Spider'], 'spawnch': 1},
    }
}