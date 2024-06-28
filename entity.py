from weapons import fists,goblinDagger,mimicJaws,spiderFangs
from names import Goblinlist

#Import Functions
from functions import text,chance,randItem
from colours import col

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
    def __init__(self, name: str,DungLvl, maxhp=10, ) -> None:
        super().__init__(name, maxhp)
        self.defaultWeapon = self.weapon
        self.room = None
        self.DungLvl = DungLvl
        self.icon = iconDict['Player']

    def equip(self, weapon) -> None:
        self.weapon = weapon
        text(f'You have equipped the {self.weapon.name}!')

    def drop(self) -> None:
        text(f'You dropped the {self.weapon.name}!')
        self.weapon = self.defaultWeapon

    def battle(self,enemy):
        self.battling = True
        while self.battling:
            self.attack(enemy)
            enemy.attack(self)
            text(f'Your HP: {self.hp}')
            text(f'{enemy.name}s HP: {enemy.hp}')
            input()
            if self.hp <= 0:
                self.battling = False
                self.death()
            elif enemy.hp <= 0:
                self.battling = False
                enemy.death(self)

    def death(self):
        text(col.red('You have died... Game Over'))

class Enemy(Entity):
    def __init__(self, name: str,weapon, maxhp=1) -> None:
        super().__init__(name, maxhp)
        self.weapon = weapon
    
    def death(self,player):
        text(f'You have slain {self.name}. Gained ____')

class Goblin(Enemy):
    def __init__(self, weapon=goblinDagger,hp=4,) -> None:
        self.name = f'{randItem(Goblinlist)} The Goblin'
        self.weapon = weapon
        self.maxhp = hp
        self.hp = hp

class Mimic(Enemy):
    def __init__(self,hp=10) -> None:
        self.name = 'The Mimic'
        self.weapon = mimicJaws
        self.maxhp = hp
        self.hp = hp

class Spider(Enemy):
    def __init__(self,hp=3):
        self.name = 'The Spider'
        self.weapon = spiderFangs
        self.maxhp = hp
        self.hp = hp