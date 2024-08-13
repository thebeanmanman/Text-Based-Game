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

    def hint(self,text):
        if self.Hints:
            print(col.name('hint',text))

    #Returns a players choice from a list of options
    def Option(self,options,Map=False,WeaponInfo=False):
        choosing = True
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

            elif WeaponInfo and choice in optionDict['weaponinfo']:
                self.player.currentWeaponStats()

            # Developer Tools
            elif self.Devmap and choice == 'devmap' and Map:
                self.player.dungeonFloor.printMap(self.player.dungeonFloor.devmap)
            else:
                print('Unknown action. Please try again')

syst = System()