from colours import col

class Item():
    def __init__(self,rarity:int,name:str) -> None:
        self.name = name
        
        self.assignRarity(rarity)

    def assignRarity(self, rarity):
        if rarity == 1:
            common.append(self)
            self.rarname = f'{col.commont} {col.common(self.name)}'
        elif rarity == 2:
            uncommon.append(self)
            self.rarname = f'{col.uncommont} {col.uncommon(self.name)}'
        elif rarity == 3:
            rare.append(self)
            self.rarname = f'{col.raret} {col.rare(self.name)}'
        elif rarity == 4:
            epic.append(self)
            self.rarname = f'{col.epict} {col.epic(self.name)}'
        elif rarity == 5:
            legendary.append(self)
            self.rarname = f'{col.legt} {col.leg(self.name)}'

class Weapon(Item):
    def __init__(self, name:str, type:str, dmg:int,rarity=1, goldvalue=1,crt=0) -> None:
        self.name = name
        self.type = type
        self.dmg = dmg
        self.goldvalue = goldvalue
        self.crt = crt
        
        self.assignRarity(rarity)

common = []
uncommon = []
rare = []
epic = []
legendary = []

ironSword = Weapon(name='Iron Sword',type='Sharp',dmg=3,crt=50,rarity=5)

shortBow = Weapon(name='Short Bow',type='Ranged',dmg=4)

fists = Weapon(name='Fists',type='Blunt',dmg=1,goldvalue=0,crt=0.0001)

claws = Weapon(name='Claws',type='Sharp',dmg=2,crt=10)

print(shortBow.rarname)