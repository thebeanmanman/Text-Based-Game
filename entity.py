# Import Modules
from random import choices

# Import Objects
from system import syst

#Import Functions
from functions import text,chance
from colours import col

# Import Dictionaries
from dictionaries import iconDict,LevelDict,optionDict

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
    def __init__(self, maxhp=10) -> None:
        super().__init__(maxhp)
        self.defaultWeapon = Entity.fists
        self.room = None
        self.icon = iconDict['Player']
        self.gold = 10
        self.lvl = 1
        self.xp = 0
        self.maxxp = 4
        self.maxlvl = 20
        self.healthbar = HealthBar(self,type='player')
        self.items = []
    
    def setName(self,name):
        self.name = name.title()

    def printItems(self):
        if self.items:
            itemDict = {}
            for item in self.items:
                itemDict[item.name] = itemDict.get(item.name, 0)+1

            text('Your items:')
            for item in itemDict:
                print(f'{chr(8226)} {item} x{itemDict[item]}')
            print()
        else:
            print('You currently have no items.')

    def chooseItems(self):
        if self.items:
            choosing = True
            print('Choose an item to use:')
            while choosing:
                choice = input('> ').lower()
                if choice in [item.name.lower() for item in self.items]:
                    choosing = False
                    for item in self.items:
                        if choice == item.name.lower():
                            self.items.remove(item)
                            item.use(self)
                            syst.enterHint(text='Press enter to return to your inventory.')
                            syst.printStatus()
                            self.printItems()
                            self.chooseItems()
                            break

                elif choice in optionDict['close inventory']:
                    choosing = False
                    print('You have closed your inventory.')
                    syst.enterHint(text='Press enter to return to the battle.')

                else:
                    print('Unknown item. Please try again.')
        else:
            syst.enterHint(text='Press enter to return to the battle.')
        
    def setDungeonFloor(self,dungeonFloor):
        self.dungeonFloor = dungeonFloor

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
            print(f'You dealt {col.name("red",self.weapon.dmg*2)} damage using your {self.weapon.name}! {col.name("red","[Critial Hit!]")}')
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

    def battleChoice(self, target):
        self.turn(target)
        print(col.name('hint','Press enter to attack, or type "items" to use your items'))
        choosing = True
        while choosing:
            choice = input('> ')
            if choice in optionDict['open inventory']:
                syst.printStatus()
                self.printItems()
                self.chooseItems()
                self.turn(target)
                print(col.name('hint','Press enter to attack, or type "items" to use your items'))

            elif choice == '' or 'attack' in choice or 'kill' in choice:
                choosing = False
                self.attack(target)

            else:
                print('Unknown action. Please try again')

    def currentWeaponStats(self):
        if self.weapon == self.defaultWeapon:
            text(f'Your current weapon is your fists.')
        else:
            text(f'Your current weapon is a {self.weapon.rarname}')
        self.weapon.showInfo()

    def battle(self,enemy):
        self.battling = True
        syst.enterHint()
        syst.printStatus()
        enemy.healthbar.update()
        text(f'You have encountered a {enemy.name}!')
        text(f"The {enemy.name}'s Health:",end='')
        print(f' {enemy.healthbar.getBar()}')
        while self.battling:
            self.battleChoice(enemy)
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
            print(f'You take {col.name("poison",self.poisonDmg)} poison damage.')
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
                    lvltext += f'\n{col.name("heal","You have reached the max level!")}'

                syst.printStatus()
                text(lvltext)
                syst.enterHint()
                syst.printStatus()

    def buy(self,gold):
        if self.gold >= gold:
            self.gold -= gold
            return True
        else:
            return False

    def death(self):
        syst.printStatus()
        text(col.name('red','You have died... Game Over'))
        syst.enterHint()

    def deathReset(self):
        self.hp = self.maxhp
        self.weapon = self.defaultWeapon
        self.poisonDur = 0


class Enemy(Entity):
    enemyList = []
    def __init__(self, name, maxhp,gold,xp,attacks,attacksch,desc='',spawnch=0) -> None:
        super().__init__(name=name, maxhp=maxhp)
        self.gold = gold
        self.xp = xp
        self.healthbar = HealthBar(self,type='enemy')
        self.attacks = attacks
        self.attacksch = attacksch
        self.spawnch = spawnch
        self.desc = desc

        # Adding the created enemy into the list of enemies
        self.enemyList.append(self)
    
    def death(self,player):
        syst.enterHint()
        player.gold += self.gold
        player.xp += self.xp
        syst.printStatus()
        text(f'You have slain the {self.name}. Gained {col.name("gold",f"+{self.gold} gold")} and +{self.xp} experience.')
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
                print(f'You took {col.name("red",attack.dmg*2)} damage. {col.name("red","[Critical Hit!]")}')
            else:
                player.takeDamage(attack.dmg)
                player.turn(self)
                print(f'You took {attack.dmg} damage.')

        if attack.steal:
            if chance(attack.stealch):
                if player.gold > 0:
                    player.gold = max(player.gold-attack.steal,0)
                    player.turn(self)
                    print(f'The {self.name} stole {col.name("gold",f"{attack.steal} gold")}!')
                else:
                    player.turn(self)
                    print(f'You had no gold for the {self.name} to steal.')
            else:
                player.turn(self)
                print('The attack missed.')

        if attack.poisonCh:
            if chance(attack.poisonCh):
                player.poisonDmg = attack.poisonDmg
                player.poisonDur += attack.poisonDur
                player.turn(self)
                print(col.name('poison',f'You have been poisoned for {attack.poisonDur} turns.'))
            else:
                player.turn(self)
                print('The attack missed.')

        if attack.heal:
            if chance(attack.healCh):
                self.heal(attack.heal)
                player.turn(self)
                print(col.name('heal',f'The {self.name} healed for {attack.heal} hp!'))
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
            print(f'The {self.name} takes {col.name("poison",self.poisonDmg)} poison damage.')
            syst.enterHint()
        
        if self.hp <= 0:
            self.battling = False
            self.death(player)