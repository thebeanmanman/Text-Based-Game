# Import Modules
from random import choices

# Import Objects
from system import syst

#Import Functions
from functions import text,chance
from grammar import Plural

# Import Dictionaries
from dictionaries import LevelDict,optionDict

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
        self.defence = 0
        self.defenceDur = 0
        self.strength = 0
        self.strengthDur = 0

    def takeDamage(self,dmg):
        dmg = max(dmg,0)
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
        self.icon = f'[{syst.col("red","X")}]'
        self.gold = 20
        # Level Up Variables
        self.lvl = 1
        self.xp = 0
        self.maxxp = 4
        self.maxlvl = 20
        self.weaponDmg = 0
        self.weaponCrit = 0

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
            print('Choose an item to use or type "close" if you want to close your inventory:')
            while choosing:
                choice = input('> ').lower()
                if choice in [item.name.lower() for item in self.items]:
                    choosing = False
                    for item in self.items:
                        if choice == item.name.lower():
                            if item.dmg >= self.hp:
                                print()
                                text('This item will kill you if you use it.')
                                syst.enterHint('Press enter to choose a different item.')
                                syst.printStatus()
                                self.printItems()
                                self.chooseItems()
                                break
                            else:
                                self.items.remove(item)
                                item.use(self)
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

    def attack(self, target):
        if chance(self.weapon.crtch+self.weaponCrit):
            dmgDealt = max(2*(self.weapon.dmg+self.weaponDmg) +self.strength -target.defence,0)
            dmgMessage = f'You dealt {syst.col("red",dmgDealt)} damage using your {self.weapon.name}! {syst.col("red","[Critial Hit!]")}'
        else:
            dmgDealt = max(self.weapon.dmg+self.weaponDmg+self.strength-target.defence,0)
            dmgMessage = f'You dealt {dmgDealt} damage using your {self.weapon.name}!'

        if target.defence:
            dmgMessage += syst.col('defence',f'[-{target.defence}]')

        if self.strength:
            dmgMessage += syst.col('strength',f' [+{self.strength}]')

        if self.strengthDur:
            self.strengthDur -= 1
            if self.strengthDur == 0:
                self.strength = 0

        target.takeDamage(dmgDealt)
        self.turn(target)
        print(dmgMessage)

        if self.hp <= 0:
            self.battling = False
            self.death()
        elif target.hp <= 0:
            self.battling = False
            target.death(self)

    def battleChoice(self, target):
        self.turn(target)
        print(syst.col('hint','Press enter to attack, or type "items" to use your items'))
        choosing = True
        while choosing:
            choice = input('> ')
            if choice in optionDict['open inventory']:
                syst.printStatus()
                self.printItems()
                self.chooseItems()
                self.turn(target)
                print(syst.col('hint','Press enter to attack, or type "items" to use your items'))

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
            self.round(enemy)
            if self.battling:
                self.battleChoice(enemy)
                if self.battling:
                    syst.enterHint()
                    enemy.round(self)
                    if self.battling:
                        enemy.attack(self)
                        if self.battling:
                            syst.enterHint()
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
            self.takeDamage(1)
            self.turn(enemy)
            print(f'You take {syst.col("poison","1")} poison damage.')
            syst.enterHint()

        if self.defenceDur:
            self.defenceDur -= 1
            if self.defenceDur == 0:
                self.defence = 0

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
                weaponDmgGain = gains[1]
                weaponCrtGain = gains[2]
                lvltext = syst.col('heal',f'You leveled up to level {self.lvl}! You gained:')
                if hpGain:
                    lvltext += f'\n{chr(8226)} +{hpGain} Max Health!'
                    self.maxhp += hpGain
                    self.heal(hpGain)

                if weaponDmgGain:
                    lvltext += f'\n{chr(8226)} +{weaponDmgGain} Weapon Damage!'
                    self.weaponDmg += weaponDmgGain

                if weaponCrtGain:
                    lvltext += f'\n{chr(8226)} +{int(weaponCrtGain*100)}% Weapon Critical Chance!'
                    self.fists.crtch += weaponCrtGain
                    
                if self.lvl == self.maxlvl:
                    lvltext += f'\n{syst.col("heal","You have reached the max level!")}'

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
        text(syst.col('red','You have died... Game Over'))
        syst.enterHint()

    def deathReset(self):
        self.hp = self.maxhp
        self.weapon = self.defaultWeapon
        self.poisonDur = 0


class Enemy(Entity):
    def __init__(self, name, maxhp,gold,xp,attacks,attacksch,desc,spawnch=0) -> None:
        super().__init__(name=name, maxhp=maxhp)
        self.gold = gold
        self.xp = xp
        self.healthbar = HealthBar(self,type='enemy')
        self.attacks = attacks
        self.attacksch = attacksch
        self.spawnch = spawnch
        self.desc = desc
    
    def death(self,player):
        syst.enterHint()
        player.gold += self.gold
        player.xp += self.xp
        syst.printStatus()
        text(f'You have slain the {self.name}. Gained {syst.col("gold",f"+{self.gold} gold")} and +{self.xp} experience.')
        syst.enterHint()
        syst.printStatus()

    def attack(self, player) -> None:
        attack = choices(self.attacks,weights=self.attacksch,k=1)[0]
        player.turn(self)
        print(f'The {self.name} used {attack.name}!')
        syst.enterHint()
        if attack.dmg:
            if chance(attack.crtch):
                dmgDealt = max(2*(attack.dmg) +self.strength - player.defence,0)
                dmgMessage = (f'You took {syst.col("red",dmgDealt)} damage. {syst.col("red","[Critical Hit!]")}')
            else:
                dmgDealt = max(attack.dmg +self.strength - player.defence,0)
                dmgMessage = (f'You took {dmgDealt} damage.')

            if player.defence:
                dmgMessage += syst.col('defence',f' [-{player.defence}]')

            if self.strength:
                dmgMessage += syst.col('strength',f' [+{self.strength}]')

            player.takeDamage(max(dmgDealt,0))
            player.turn(self)
            print(dmgMessage)

        if attack.steal:
            if chance(attack.stealch):
                if player.gold > 0:
                    player.gold = max(player.gold-attack.steal,0)
                    player.turn(self)
                    print(f'The {self.name} stole {syst.col("gold",f"{attack.steal} gold")}!')
                else:
                    player.turn(self)
                    print(f'You had no gold for the {self.name} to steal.')
            else:
                player.turn(self)
                print('The attack failed.')

        if attack.poisonCh:
            if chance(attack.poisonCh):
                player.poisonDur += attack.poisonDur
                player.turn(self)
                print(syst.col('poison',f'You have been poisoned for {attack.poisonDur} {Plural(attack.poisonDur, "turn")}.'))
            else:
                player.turn(self)
                print('The attack failed.')

        if attack.heal:
            if chance(attack.healCh):
                self.heal(attack.heal)
                player.turn(self)
                print(syst.col('heal',f'The {self.name} healed for {attack.heal} hp!'))
            else:
                player.turn(self)
                print(f"The {self.name} didn't heal.")

        if attack.defencech:
            if chance(attack.defencech):
                self.defence = attack.defence
                self.defenceDur = attack.defenceDur
                player.turn(self)
                print(syst.col('defence',f'The {self.name} gained +{attack.defence} defence for {attack.defenceDur} {Plural(attack.defenceDur,"turn")}.'))
            else:
                player.turn(self)
                print('The attack failed.')
            
        if self.strengthDur:
            self.strengthDur -= 1
            if self.strengthDur == 0:
                self.strength = 0

        if attack.strengthch:
            if chance(attack.strengthch):
                self.strength = attack.strength
                self.strengthDur = attack.strengthDur
                player.turn(self)
                print(syst.col('strength',f'The {self.name} gained +{attack.strength} strength for {attack.strengthDur} {Plural(attack.strengthDur,"turn")}.'))
            else:
                player.turn(self)
                print('The attack failed.')

        if player.hp <= 0:
                player.battling = False
                syst.enterHint()
                player.death()

        elif self.hp <= 0:
            player.battling = False
            self.death(player)

    def round(self,player):

        if self.defenceDur:
            self.defenceDur -= 1
            if self.defenceDur == 0:
                self.defence = 0

        if self.poisonDur:
            self.poisonDur -= 1
            self.takeDamage(1)
            player.turn(self)
            print(f'The {self.name} takes {syst.col("poison","1")} poison damage.')
            syst.enterHint()
        
        if self.hp <= 0:
            self.battling = False
            self.death(player)