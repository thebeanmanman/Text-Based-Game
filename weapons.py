from colours import col
from functions import text

class Item():
    def __init__(self,rarity:int,name:str,desc:str) -> None:
        self.name = name
        self.desc = desc
        self.assignRarity(rarity)

    def assignRarity(self, rarity):
        if rarity == 1:
            common.append(self)
            self.rarname = f'{col.commont} {col.common(self.name)}'
            self.name = col.common(self.name)
        elif rarity == 2:
            uncommon.append(self)
            self.rarname = f'{col.uncommont} {col.uncommon(self.name)}'
            self.name = col.uncommon(self.name)
        elif rarity == 3:
            rare.append(self)
            self.rarname = f'{col.raret} {col.rare(self.name)}'
            self.name = col.rare(self.name)
        elif rarity == 4:
            epic.append(self)
            self.rarname = f'{col.epict} {col.epic(self.name)}'
            self.name = col.epic(self.name)
        elif rarity == 5:
            legendary.append(self)
            self.rarname = f'{col.legt} {col.leg(self.name)}'
            self.name = col.leg(self.name)

class Weapon(Item):
    def __init__(self, name:str, type:str, dmg:int,desc='',rarity=0, goldvalue=0,crt=0) -> None:
        super().__init__(name=name,desc=desc,rarity=rarity)
        self.type = type
        self.dmg = dmg
        self.goldvalue = goldvalue
        self.crt = crt
    
    def showStats(self):
        text(f'Description: {self.desc}')
        text(f'Damage: {self.dmg}')
        if self.crt > 0:
            text(f'Critical Hit Chance: {int(self.crt*100)}%')

common = []
uncommon = []
rare = []
epic = []
legendary = []

### Weapons ###
# Common
woodenSword = Weapon(name='Wooden Sword',type='Sharp',dmg=2,crt=0.05,rarity=1,desc='A sword made of wood.')
stick = Weapon(name='Stick',type='Blunt',dmg=1,desc='Utterly Useless',crt=0.01,rarity=1)

# Uncommon
shortBow = Weapon(name='Short Bow',type='Ranged',dmg=2,crt=0.2,desc='A short bow',rarity=2)

# Rare
ironSword = Weapon(name='Iron Sword',type='Sharp',dmg=4,crt=0.09,rarity=3,desc='A sword made of iron.')

# Epic
greatSword = Weapon(name='Great Sword',type='Sharp',dmg=5,crt=0.05,rarity=4,desc='A great sword.')

# Legendary
diamondSword = Weapon(name='Diamond Sword',type='Sharp',dmg=6,crt=0.01,rarity=5,desc='A sword made of diamonds.')
goldenStick = Weapon(name='Golden Stick',type='Blunt',dmg=4,crt=1,rarity=5,desc='Golden, sticky and WHAAAAT 100% Crtical Hit Chance?!')

# Unobtainable Weapons / Enemy Weapons
fists = Weapon(name='Fists',type='Blunt',dmg=1,desc='Punchy Punchy',rarity=0)
goblinDagger = Weapon(name='Dagger',type='Sharp',dmg=2,crt=0.1,rarity=0)
mimicJaws = Weapon(name='Jaws',type='Sharp',dmg=5,crt=0.15,rarity=0)
spiderFangs = Weapon(name='Fangs',type='Sharp',dmg=1,rarity=0) # Add Poison Chance