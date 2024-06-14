from weapons import fists

#Import Functions
from functions import text,chance

class Entity():
    def __init__(self, name:str, maxhp=1) -> None:
        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.weapon = fists
    
    def attack(self, target) -> None:
        if chance(self.weapon.crt):
            target.hp -= self.weapon.dmg*3
            text(f'{self.name} dealt {self.weapon.dmg*3} damage using {self.weapon.name} Critial Hit!')
        else:
            target.hp -= self.weapon.dmg
            text(f'{self.name} dealt {self.weapon.dmg} damage using {self.weapon.name}!')

class Player(Entity):
    def __init__(self, name: str, maxhp=1) -> None:
        super().__init__(name, maxhp)

        self.defaultWeapon = self.weapon

    def equip(self, weapon) -> None:
        self.weapon = weapon
        text(f'{self.name} equipped a {self.weapon.name}!')

    def drop(self) -> None:
        text(f'{self.name} dropped the {self.weapon.name}!')
        self.weapon = self.defaultWeapon

class Enemy(Entity):
    def __init__(self, name: str,weapon, maxhp=1) -> None:
        super().__init__(name, maxhp)
        self.weapon = weapon