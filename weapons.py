from colours import col
from functions import text
from entity import *

class Item():
    def __init__(self,name:str) -> None:
        self.name = name

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
    def __init__(self, name: str, dmg: int,enemyClass,chance, crtch=0, stealch=0, steal=0,poisonCh=0,poisonDmg=0,poisonDur=0,heal=0,healCh=0) -> None:
        super().__init__(name,dmg,crtch,poisonCh,poisonDmg,poisonDur,heal,healCh)
        self.stealch = stealch
        self.steal = steal
        enemyClass.attacks.append(self)
        enemyClass.attacksch.append(chance)

class PlayerWeapon(Weapon):
    def __init__(self, name: str, dmg: int, desc='', rarity=0, crtch=0, poisonCh=0,poisonDmg=0,poisonDur=0,heal=0,healCh=0) -> None:
        super().__init__(name, dmg,crtch,poisonCh,poisonDmg,poisonDur,heal,healCh)
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
ironSword = PlayerWeapon(name='Iron Sword',dmg=4,crtch=0.09,rarity=3,desc='A sword made of iron.')

# Epic
greatSword = PlayerWeapon(name='Great Sword',dmg=5,crtch=0.05,rarity=4,desc='A great sword.')

# Legendary
diamondSword = PlayerWeapon(name='Diamond Sword',dmg=6,crtch=0.01,rarity=5,desc='A sword made of diamonds.')
goldenStick = PlayerWeapon(name='Golden Stick',dmg=4,crtch=1,rarity=5,desc='Golden, sticky and WHAAAAT 100% Crtical Hit Chance?!')

### Unobtainable Weapons
fists = PlayerWeapon(name='Fists',dmg=1,desc='Punchy Punchy')
Entity.fists = fists


### Enemy Attacks ###
# Goblin Weapons
goblinStab = EnemyWeapon(name='Stab',dmg=2,crtch=0.1,enemyClass=Goblin,chance=2)
goblinSteal = EnemyWeapon(name='Steal',dmg=0,steal=1,stealch=1,enemyClass=Goblin,chance=1)

# Mimic Weapons
mimicJaws = EnemyWeapon(name='Chomp',dmg=5,crtch=0.15,enemyClass=Mimic, chance=2)
mimicLunge = EnemyWeapon(name='Lunge',dmg=6,enemyClass=Mimic, chance=1)

# Baby Spider Weapons
babyspiderFangs = EnemyWeapon(name='Bite',dmg=1,crtch=0.05,enemyClass=BabySpider,chance=3)
babyspiderPoison = EnemyWeapon(name='Poisonous Bite',dmg=0,poisonCh=1,poisonDmg=1,poisonDur=3,enemyClass=BabySpider,chance=1)

# Slime Weapons
slimeRoll = EnemyWeapon(name='Roll',dmg=1,enemyClass=Slime, chance=3)
slimeHeal = EnemyWeapon(name='Reshape',dmg=0,enemyClass=Slime,chance=2,heal=1,healCh=0.5)