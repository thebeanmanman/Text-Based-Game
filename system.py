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
    def Option(self,player=None,North=False,South=False,West=False,East=False,Map=False,Other=False,OtherList=[],Yes=False,No=False,Open=False,Exit=False,prompt=''):
        choosing = True
        if prompt:
            text(prompt)
        while choosing:
            choice = input('> ').lower()
            if North and choice in optionDict['north']:
                return choice
            elif South and choice in optionDict['south']:
                return choice
            elif West and choice in optionDict['west']:
                return choice
            elif East and choice in optionDict['east']:
                return choice
            elif Other and choice in OtherList:
                return choice
            elif Exit and choice in optionDict['exit']:
                return choice
            elif Map and choice in optionDict['map']:
                player.dungeonFloor.printPlayerMap(player)
            elif Yes and choice in optionDict['yes']:
                return choice
            elif No and choice in optionDict['no']:
                return choice
            elif Open and choice in optionDict['open']:
                return choice
            # Constant Options
            elif choice in optionDict['hintsoff']:
                self.Hints = False
                text('Hints have been turned off.\nType "hints on" anytime to turn them on.')
            elif choice in optionDict['hintson']:
                self.Hints = True
                text('Hints have been turned on.\nType "hints off" anytime to turn them off.')
            elif choice in optionDict['quit']:
                text('Thanks for playing!')
                quit()
            
            # Player Choices
            elif player and choice in optionDict['drop']:
                if player.weapon == player.defaultWeapon:
                    text("You can't drop your fists...")
                else:
                    text(f'Are you sure you want to drop your {player.weapon.name}?')
                    option = self.Option(Yes=True,No=True,Other=True,OtherList=optionDict['drop'])
                    if option in optionDict['yes'] or option in optionDict['drop']:
                        player.drop()
                        syst.enterHint()
                        syst.printStatus()
                        text(prompt)
                    elif option in optionDict['no']:
                        text(f"You choose to not drop your {player.weapon.name}.")

            elif player and choice in optionDict['weaponinfo']:
                player.currentWeaponStats()

            # Developer Tools
            elif self.Devmap and choice == 'devmap' and Map:
                player.dungeonFloor.printMap(player.dungeonFloor.dispMap)
            else:
                print('Unknown action. Please try again')

syst = System()