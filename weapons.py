class Weapon:
    def __init__(self, name:str, type:str, dmg:int, goldvalue=1, rarity=1,crt=0) -> None:
        self.name = name
        self.type = type
        self.dmg = dmg
        self.goldvalue = goldvalue
        self.rarity = rarity
        self.crt = crt

ironSword = Weapon(name='Iron Sword',type='Sharp',dmg=3,crt=50)

shortBow = Weapon(name='Short Bow',type='Ranged',dmg=4)

fists = Weapon(name='Fists',type='Blunt',dmg=1,goldvalue=0,crt=0.0001)

claws = Weapon(name='Claws',type='Sharp',dmg=2,crt=10)
