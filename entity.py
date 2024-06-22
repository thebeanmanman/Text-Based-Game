from weapons import fists,claws
from names import Goblinlist
from random import randint

#Import Functions
from functions import text,chance,randItem,col

# Import Dictionaries
from dictionaries import iconDict

class Entity():
    def __init__(self, name:str, maxhp=1) -> None:
        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.weapon = fists
    
    def attack(self, target) -> None:
        if chance(self.weapon.crt):
            target.hp -= self.weapon.dmg*3
            text(f'{self.name} dealt {col.rgb(255,0,0,self.weapon.dmg*3)} damage using their {self.weapon.name} {col.red("[Critial Hit!]")}')
        else:
            target.hp -= self.weapon.dmg
            text(f'{self.name} dealt {self.weapon.dmg} damage using their {self.weapon.name}!')
        target.hp = max(target.hp,0)
class Player(Entity):
    def __init__(self, name: str,DungLvl, maxhp=1, ) -> None:
        super().__init__(name, maxhp)
        self.defaultWeapon = self.weapon
        self.room = None
        self.DungLvl = DungLvl
        self.icon = iconDict['Player']

    def equip(self, weapon) -> None:
        self.weapon = weapon
        text(f'{self.name} equipped a {self.weapon.name}!')

    def drop(self) -> None:
        text(f'{self.name} dropped the {self.weapon.name}!')
        self.weapon = self.defaultWeapon

    def death(self):
        text(col.red('You have died... Game Over'))

class Enemy(Entity):
    def __init__(self, name: str,weapon, maxhp=1) -> None:
        super().__init__(name, maxhp)
        self.weapon = weapon
    
    def death(self,player):
        text(f'You have slain {self.name}. Gained ____')

class Goblin(Enemy):
    def __init__(self, weapon=claws,hp=4,) -> None:
        self.name = f'{randItem(Goblinlist)} The Goblin'
        self.weapon = weapon
        self.maxhp = hp
        self.hp = hp