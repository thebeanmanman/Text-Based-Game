# Import Modules
from random import choices

# Import Objects
from system import syst

#Import Functions
from functions import text,chance
from colours import col

# Import Dictionaries
from dictionaries import iconDict,LevelDict

# Import Classes
from healthbar import HealthBar

class Entity():
    fists = None
    def __init__(self,maxhp, name='') -> None:
        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.weapon = Entity.fists
        self.poisonDur = 0
        self.poisonDmg = 0

    def takeDamage(self,dmg):
        self.hp -= dmg
        self.hp = max(self.hp,0)

    def heal(self,healAmount):
        self.hp += healAmount
        self.hp = min(self.hp,self.maxhp)

class Player(Entity):
    def __init__(self,DungLvl, maxhp=10) -> None:
        super().__init__(maxhp)
        self.defaultWeapon = Entity.fists
        self.room = None
        self.DungLvl = DungLvl
        self.icon = iconDict['Player']
        self.gold = 0
        self.lvl = 1
        self.xp = 0
        self.maxxp = 4
        self.maxlvl = 20
        self.healthbar = HealthBar(self,type='player')
    
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
            target.takeDamage(self.weapon.dmg*2)
            self.turn(target)
            print(f'You dealt {col.red(self.weapon.dmg*2)} damage using your {self.weapon.name}! {col.red("[Critial Hit!]")}')
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
        if self.weapon == self.defaultWeapon:
            text(f'Your current weapon is your fists.')
        else:
            text(f'Your current weapon is a {self.weapon.rarname}')
        self.weapon.showStats()

    def battle(self,enemy):
        self.battling = True
        syst.enterHint()
        syst.printStatus()
        enemy.healthbar.update()
        text(f'You have encountered a {enemy.name}!')
        text(f"The {enemy.name}'s Health:",end='')
        print(f' {enemy.healthbar.getBar()}')
        syst.enterHint()
        while self.battling:
            self.attack(enemy)
            if self.battling:
                syst.enterHint()
                enemy.attack(self)
                if self.battling:
                    syst.enterHint()
                    enemy.round(self)
                    self.round(enemy)
        self.levelCheck()

    def turn(self,enemy):
        syst.printStatus()
        enemy.healthbar.update()
        print(f'You have encountered a {enemy.name}!')
        print(f"The {enemy.name}'s Health: {enemy.healthbar.getBar()}")
        print()

    def round(self,enemy):
        if self.poisonDur:
            self.poisonDur -= 1
            self.takeDamage(self.poisonDmg)
            self.turn(enemy)
            print(f'You take {col.poison(self.poisonDmg)} poison damage.')
            syst.enterHint()

        if self.hp <= 0:
            self.battling = False
            self.death()

    def levelCheck(self):
        while self.xp >= self.maxxp and self.lvl < self.maxlvl:
            self.lvl += 1
            self.xp -= self.maxxp
            self.maxxp += 3
            if self.lvl <= self.maxlvl:
                gains = LevelDict[self.lvl]
                hpGain = gains[0]
                fistDmgGain = gains[1]
                fistCrtGain = gains[2]
                lvltext = f'You leveled up to level {self.lvl}! You gained:'
                if hpGain:
                    lvltext += f'\n{chr(8226)} +{hpGain} Max Health!'
                    self.maxhp += hpGain
                    self.heal(hpGain)

                if fistDmgGain:
                    lvltext += f'\n{chr(8226)} +{fistDmgGain} Fist Damage!'
                    self.fists.dmg += fistDmgGain

                if fistCrtGain:
                    lvltext += f'\n{chr(8226)} +{int(fistCrtGain*100)}% Fist Critical Chance!'
                    self.fists.crtch += fistCrtGain
                    
                if self.lvl == self.maxlvl:
                    lvltext += f'\n{col.heal("You have reached the max level!")}'

                syst.printStatus()
                text(lvltext)
                syst.enterHint()
                syst.printStatus()


    def death(self):
        text(col.red('You have died... Game Over'))

class Enemy(Entity):
    def __init__(self, name, maxhp,gold,xp) -> None:
        super().__init__(name=name, maxhp=maxhp)
        self.gold = gold
        self.xp = xp
        self.healthbar = HealthBar(self,type='enemy')
    
    def death(self,player):
        syst.enterHint()
        player.gold += self.gold
        player.xp += self.xp
        syst.printStatus()
        text(f'You have slain the {self.name}. Gained {col.gold(f"+{self.gold} gold")} and +{self.xp} experience.')
        syst.enterHint()
        syst.printStatus()

    def attack(self, player) -> None:
        attack = choices(self.attacks,weights=self.attacksch,k=1)[0]
        player.turn(self)
        print(f'The {self.name} used {attack.name}!')
        syst.enterHint()
        if attack.dmg:
            if chance(attack.crtch):
                player.takeDamage(attack.dmg*2)
                player.turn(self)
                print(f'You took {col.red(attack.dmg*2)} damage. {col.red("[Critical Hit!]")}')
            else:
                player.takeDamage(attack.dmg)
                player.turn(self)
                print(f'You took {attack.dmg} damage.')

        if attack.steal:
            if chance(attack.stealch):
                if player.gold > 0:
                    player.gold = max(player.gold-attack.steal,0)
                    player.turn(self)
                    print(f'The {self.name} stole {col.gold(f"{attack.steal} gold")}!')
                else:
                    player.turn(self)
                    print(f'You had no gold for the {self.name} to steal.')
            else:
                player.turn(self)
                print('The attack missed.')

        if attack.poisonCh:
            if chance(attack.poisonCh):
                player.poisonDmg = attack.poisonDmg
                player.poisonDur = attack.poisonDur
                player.turn(self)
                print(col.poison(f'You have been poisoned for {attack.poisonDur} turns.'))
            else:
                player.turn(self)
                print('The attack missed.')

        if attack.heal:
            if chance(attack.healCh):
                self.heal(attack.heal)
                player.turn(self)
                print(col.heal(f'The {self.name} healed for {attack.heal} hp!'))
            else:
                player.turn(self)
                print(f"The {self.name} didn't heal.")
            
        if player.hp <= 0:
                player.battling = False
                syst.enterHint()
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
            syst.enterHint()
        
        if self.hp <= 0:
            self.battling = False
            self.death(player)

class Goblin(Enemy):
    attacks = []
    attacksch = []
    Levels = [1]
    Chances = [1]
    Descs = ['You hear a mischievous snicker from behind you.\nYou quickly turn around to see a small green creature brandishing a crudely crafted knife staring intensly at your gold pouch.']
    def __init__(self,
                 hp=4,
                 name='Goblin',
                 gold=2,
                 xp=1) -> None:
        super().__init__(name=name,maxhp=hp,gold=gold,xp=xp)

class Mimic(Enemy):
    attacks = []
    attacksch = []
    Levels = []
    def __init__(self,
                 hp=10,
                 name='Mimic',
                 gold=10,
                 xp=4) -> None:
        super().__init__(name=name,maxhp=hp,gold=gold,xp=xp)

class BabySpider(Enemy):
    attacks = []
    attacksch = []
    Levels = [1]
    Chances = [1]
    Descs = ['You suddenly run into a thick spider web, which blocks your vision.\nAs you hastily remove it, you see a spider the size of a wolf standing before you.']
    def __init__(self,
                 hp=3,
                 name = 'Baby Spider',
                 gold=1,
                 xp=1
                 ):
        super().__init__(name=name,maxhp=hp,gold=gold,xp=xp)

class Slime(Enemy):
    attacks = []
    attacksch = []
    Levels = [1]
    Chances = [1]
    Descs = ["Standing before you, there is a green gelatinous blob.\nThrough its translucent skin, you can see partially digested bones floating in what seems to be it's stomach."]
    def __init__(self,
                 hp=4,
                 name='Slime',
                 gold=1,
                 xp=2
                 ):
        super().__init__(name=name,maxhp=hp,gold=gold,xp=xp)