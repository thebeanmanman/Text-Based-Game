from colours import col

class Item():
    def __init__(self,rarity:int,name:str,desc:str,playerItem=True) -> None:
        self.name = name
        self.desc = desc
        self.playerItem = playerItem
        self.assignRarity(rarity)

    def assignRarity(self, rarity):
        if self.playerItem:
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
    def __init__(self, name:str, type:str, dmg:int,desc='',rarity=1, goldvalue=1,crt=0,playerItem=True) -> None:
        super().__init__(name=name,desc=desc,rarity=rarity,playerItem=playerItem)
        self.type = type
        self.dmg = dmg
        self.goldvalue = goldvalue
        self.crt = crt

common = []
uncommon = []
rare = []
epic = []
legendary = []

# rarityList = [common,uncommon,rare,epic,legendary]

woodenSword = Weapon(name='Wooden Sword',type='Sharp',dmg=3,crt=0.01,rarity=1,desc='A sword made of wood.')
ironSword = Weapon(name='Iron Sword',type='Sharp',dmg=3,crt=0.5,rarity=3,desc='A sword made of iron.')
diamondSword = Weapon(name='Diamond Sword',type='Sharp',dmg=3,crt=0.01,rarity=5,desc='A sword made of diamonds.')

greatSword = Weapon(name='Great Sword',type='Sharp',dmg=9,crt=0.05,rarity=4,desc='A great sword.')

shortBow = Weapon(name='Short Bow',type='Ranged',dmg=4,desc='A short bow',rarity=2)

fists = Weapon(name='Fists',type='Blunt',dmg=1,goldvalue=0,crt=0.0001,desc='Punchy Punchy',playerItem=False)

claws = Weapon(name='Claws',type='Sharp',dmg=2,crt=0.1,playerItem=False)