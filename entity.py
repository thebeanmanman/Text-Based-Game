# Import Modules
from random import choices

# Import Objects
from system import syst

#Import Functions
from functions import text,chance
from colours import col

# Import Dictionaries
from dictionaries import iconDict

class Entity():
    fists = None
    def __init__(self,maxhp, name='' ) -> None:
        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.weapon = Entity.fists
        self.poisonDur = 0
        self.poisonDmg = 0

    def takeDamage(self,dmg):
        self.hp -= dmg
        self.hp = max(self.hp,0)

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
        if chance(self.weapon.crtch):
            target.takeDamage(self.weapon.dmg*3)
            self.turn(target)
            print(f'You dealt {col.red(self.weapon.dmg*3)} damage using your {self.weapon.name}! {col.red("[Critial Hit!]")}')
        else:
            target.takeDamage(self.weapon.dmg)
            self.turn(target)
            print(f'You dealt {self.weapon.dmg} damage using your {self.weapon.name}!')
        if self.hp <= 0:
            self.battling = False
            self.death()
        elif target.hp <= 0:
            self.battling = False
            target.death(self)

    def currentWeaponStats(self):
        if self.weapon == Entity.fists:
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
                    self.round(enemy)
                    enemy.round(self)

    def turn(self,enemy):
        syst.printStatus()
        print(f'You have encountered a {enemy.name}!')
        print(f"The {enemy.name}'s HP: {enemy.hp}")
        print()

    def round(self,enemy):
        if self.poisonDur:
            self.poisonDur -= 1
            self.takeDamage(self.poisonDmg)
            self.turn(enemy)
            print(f'You take {col.poison(self.poisonDmg)} poison damage.')
            input()


    def death(self):
        text(col.red('You have died... Game Over'))

class Enemy(Entity):
    def __init__(self, name, maxhp,gold,xp) -> None:
        super().__init__(name=name, maxhp=maxhp)
        self.gold = gold
        self.xp = xp
    
    def death(self,player):
        input()
        player.gold += self.gold
        player.xp += self.xp
        syst.printStatus()
        text(f'You have slain the {self.name}. Gained {col.gold(f"+{self.gold} gold")} and +{self.xp} xp')

    def attack(self, player) -> None:
        attack = choices(self.attacks,weights=self.attacksch,k=1)[0]
        player.turn(self)
        print(f'The {self.name} used {attack.name}!')
        input()
        if attack.dmg:
            if chance(attack.crtch):
                player.takeDamage(attack.dmg*3)
                player.turn(self)
                print(f'You took {col.red(attack.dmg*3)} damage. {col.red("[Critical Hit!]")}')
            else:
                player.takeDamage(attack.dmg)
                player.turn(self)
                print(f'You took {attack.dmg} damage.')

        if attack.steal:
            if chance(attack.stealch):
                player.gold = max(player.gold-attack.steal,0)
                player.turn(self)
                print(f'The {self.name} stole {col.gold(attack.steal)} gold!')
            else:
                print('The attack missed.')

        if attack.poisonCh:
            if chance(attack.poisonCh):
                player.poisonDmg = attack.poisonDmg
                player.poisonDur = attack.poisonDur
                print(f'You have been poisoned for {col.poison(attack.poisonDur)} turns.')
            else:
                print('The attack missed.')
            
        if player.hp <= 0:
                player.battling = False
                input()
                player.death()
        elif self.hp <= 0:
            player.battling = False
            self.death(player)

    def round(self,player):
        if self.poisonDur:
            self.poisonDur -= 1
            self.takeDamage(self.poisonDmg)
            player.turn(self)
            print(f'The {self.name} takes {col.poison(self.poisonDmg)} poison damage.')
            input()

class Goblin(Enemy):
    attacks = []
    attacksch = []
    def __init__(self,
                 hp=4,
                 name='Goblin',
                 gold=2,
                 xp=1) -> None:
        super().__init__(name=name,maxhp=hp,gold=gold,xp=xp)

class Mimic(Enemy):
    attacks = []
    attacksch = []
    def __init__(self,
                 hp=10,
                 name='Mimic',
                 gold=10,
                 xp=4) -> None:
        super().__init__(name=name,maxhp=hp,gold=gold,xp=xp)

class Spider(Enemy):
    attacks = []
    attacksch = []
    def __init__(self,
                 hp=3,
                 name = 'Spider',
                 gold=1,
                 xp=1
                 ):
        super().__init__(name=name,maxhp=hp,gold=gold,xp=xp)

class Idk(Enemy):
    attacks = []
    attacksch = []
    def __init__(self,
                 hp=2,
                 name='',
                 gold=1,
                 xp=1
                 ):
        super().__init__(name=name,maxhp=hp,gold=gold,xp=xp)
