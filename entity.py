# Import Objects
from system import syst
from weapons import fists,goblinDagger,mimicJaws,spiderFangs

#Import Functions
from functions import text,chance
from colours import col

# Import Dictionaries
from dictionaries import iconDict

class Entity():
    def __init__(self,maxhp, name='' ) -> None:
        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.weapon = fists
    
    def attack(self, target) -> None:
        if chance(self.weapon.crt):
            target.hp -= self.weapon.dmg*3
            target.hp = max(target.hp,0)
            target.turn(self)
            print(f'The {self.name} dealt {col.red(self.weapon.dmg*3)} damage using their {self.weapon.name}! {col.red("[Critial Hit!]")}')
        else:
            target.hp -= self.weapon.dmg
            target.hp = max(target.hp,0)
            target.turn(self)
            print(f'The {self.name} dealt {self.weapon.dmg} damage using their {self.weapon.name}!')
        if target.hp <= 0:
                target.battling = False
                input()
                target.death()
        elif self.hp <= 0:
            target.battling = False
            self.death(target)

class Player(Entity):
    def __init__(self,DungLvl, maxhp=10) -> None:
        super().__init__(maxhp)
        self.defaultWeapon = self.weapon
        self.room = None
        self.DungLvl = DungLvl
        self.icon = iconDict['Player']
        self.gold = 0
        self.lvl = 1
        self.xp = 0
    
    def setName(self,name):
        self.name = name.title()

    def equip(self, weapon) -> None:
        self.weapon = weapon
        syst.printStatus()
        text(f'You have equipped the {self.weapon.name}!')

    def drop(self) -> None:
        text(f'You dropped the {self.weapon.name}!')
        self.weapon = self.defaultWeapon

    def attack(self, target):
        if chance(self.weapon.crt):
            target.hp -= self.weapon.dmg*3
            self.turn(target)
            print(f'You dealt {col.red(self.weapon.dmg*3)} damage using your {self.weapon.name}! {col.red("[Critial Hit!]")}')
        else:
            target.hp -= self.weapon.dmg
            self.turn(target)
            print(f'You dealt {self.weapon.dmg} damage using your {self.weapon.name}!')
        target.hp = max(target.hp,0)
        if self.hp <= 0:
            self.battling = False
            self.death()
        elif target.hp <= 0:
            self.battling = False
            target.death(self)

    def currentWeaponStats(self):
        if self.weapon == fists:
            text(f'Your current weapon is your fists.')
        else:
            text(f'Your current weapon is a {self.weapon.rarname}')
        self.weapon.showStats()

    def battle(self,enemy):
        self.battling = True
        input()
        syst.printStatus()
        text(f'You have encountered a {enemy.name}!')
        text(f"The {enemy.name}'s HP: {enemy.hp}")
        input()
        while self.battling:
            self.attack(enemy)
            if self.battling:
                input()
                enemy.attack(self)
                if self.battling:
                    input()

    def turn(self,enemy):
        syst.printStatus()
        print(f'You have encountered a {enemy.name}!')
        print(f"The {enemy.name}'s HP: {enemy.hp}")
        print()

    def death(self):
        text(col.red('You have died... Game Over'))

class Enemy(Entity):
    def __init__(self, name='',weapon=None, maxhp=1,gold=1,xp=1) -> None:
        super().__init__(name=name, maxhp=maxhp)
        self.weapon = weapon
        self.gold = gold
        self.xp = xp
    
    def death(self,player):
        input()
        player.gold += self.gold
        player.xp += self.xp
        syst.printStatus()
        text(f'You have slain the {self.name}. Gained {col.gold(f"+{self.gold} gold")} and +{self.xp} xp')

class Goblin(Enemy):
    def __init__(self, weapon=goblinDagger,hp=4,) -> None:
        super().__init__(maxhp=hp)
        self.name = 'Goblin'
        self.weapon = weapon
        self.maxhp = hp
        self.hp = hp
        self.gold = 2

class Mimic(Enemy):
    def __init__(self,hp=10) -> None:
        super().__init__(maxhp=hp)
        self.name = 'Mimic'
        self.weapon = mimicJaws
        self.maxhp = hp
        self.hp = hp
        self.gold = 5

class Spider(Enemy):
    def __init__(self,hp=3):
        super().__init__(maxhp=hp)
        self.name = 'Spider'
        self.weapon = spiderFangs
        self.gold = 1