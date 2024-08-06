from colours import col
from functions import text
import os
from dictionaries import optionDict

class System():
    #Control Variables
    ClearTerminal = True
    Devmap = True
    Hints = True
    NarSpeed = 0.075

    def __init__(self):
        #Player Status Variables
        self.divChar = '-'
        self.sideDivLen = 5

    def setPlayer(self,player):
        self.player = player

    #Controls whether the terminal will be cleared or not. Also allows for compatibility between operating systems (Debugging)
    def wipe(self):
        if self.ClearTerminal:
            os.system('cls' if os.name=='nt' else 'clear')

    # Prints the players status
    def playerStatus(self):
        self.player.healthbar.update()
        topBanner = f"{self.divChar*self.sideDivLen} {self.player.name} Level {self.player.lvl} {self.divChar*self.sideDivLen}"
        print(topBanner)
        if self.player.lvl >= self.player.maxlvl:
            print(f'Experience: {col.name("heal","Max Level")}')
        elif self.player.xp >= self.player.maxxp:
            print(f'Experience: {col.name("heal",self.player.xp)}/{self.player.maxxp}')
        else:
            print(f'Experience: {self.player.xp}/{self.player.maxxp}')
        print(f'Gold: {col.name("gold",f"{self.player.gold}")}')
        print(f'Health: {self.player.healthbar.getBar()}')
        print(f'Weapon: {self.player.weapon.name}')
        print(f'Items: {len(self.player.items)}')
        self.fullDiv = self.divChar*len(topBanner)
        print(self.fullDiv)

    # Wipes the terminal and then prints the players status
    def printStatus(self):
        self.wipe()
        self.playerStatus()

    # Waits for the player to press enter, and then prints status
    def enterHint(self,text='Press enter to continue...',space=True):
        if self.Hints:
            if space:
                print()
            input(col.name('hint',text))
        else:
            input()

    #Returns a players choice from a list of options
    def Option(self,options,player=None,prompt='',Map=False,Drop=False,WeaponInfo=False):
        choosing = True
        if prompt:
            text(prompt)
        while choosing:
            choice = input('> ').lower()
            for option in options:
                if choice in option:
                    return choice

            # Constant Options
            if choice in optionDict['hintsoff']:
                self.Hints = False
                text('Hints have been turned off.\nType "hints on" anytime to turn them on.')
            elif choice in optionDict['hintson']:
                self.Hints = True
                text('Hints have been turned on.\nType "hints off" anytime to turn them off.')
            elif choice in optionDict['quit']:
                text('Thanks for playing!')
                quit()
            
            # Player Choices
            elif Map and choice in optionDict['map']:
                self.player.dungeonFloor.printPlayerMap(self.player)

            elif Drop and choice in optionDict['drop']:
                if self.player.weapon == self.player.defaultWeapon:
                    text("You can't drop your fists...")
                else:
                    text(f'Are you sure you want to drop your {self.player.weapon.name}?')
                    option = self.Option(options=[optionDict['drop'],optionDict['yes'],optionDict['no']])
                    if option in optionDict['yes'] or option in optionDict['drop']:
                        self.player.drop()
                        syst.enterHint()
                        syst.printStatus()
                        text(prompt)
                    elif option in optionDict['no']:
                        text(f"You choose to not drop your {self.player.weapon.name}.")

            elif WeaponInfo and choice in optionDict['weaponinfo']:
                self.player.currentWeaponStats()

            # Developer Tools
            elif self.Devmap and choice == 'devmap' and Map:
                self.player.dungeonFloor.printMap(self.player.dungeonFloor.devmap)
            else:
                print('Unknown action. Please try again')

syst = System()