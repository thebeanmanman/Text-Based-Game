class Weapon:
    def __init__(self, name:str, type:str, dmg:int, goldvalue=1, rarity=1) -> None:
        self.name = name
        self.type = type
        self.dmg = dmg
        self.goldvalue = goldvalue
        self.rarity = rarity

ironSword = Weapon(name='Iron Sword',type='Sharp',dmg=2)

shortBow = Weapon(name='Short Bow',type='Ranged',dmg=4)

fists = Weapon(name='Fists',type='Blunt',dmg=1,goldvalue=0)
