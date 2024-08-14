from functions import text
import os
from dictionaries import optionDict

class System():
    #Control Variables
    ClearTerminal = True
    Devmap = True
    NarSpeed = 0.075

    # Settings Variables
    settingsDict = {
        'Hints' : True,
        'Text Colours' : True
    }
    def __init__(self):
        #Player Status Variables
        self.divChar = '─'
        self.sideDivLen = 5

        # Colour Variables
        self.colourDict = {
            # Regular Colours
            'red': (255,0,0),
            'lightred': (250,95,85),
            'gold': (255,255,0),
            'nar' : (0,191,255),
            'npc' : (210,180,140),
            'hint': (255,255,255),

            # Status Effects
            'poison' : (0,128,0),
            'heal' : (60,245,113),
            'defence' : (137,207,240),
            'strength' : (178,34,34),

            # Rarity Colours
            'common' : (128,128,128),
            'uncommon' : (50,185,50),
            'rare' : (30,144,255),
            'epic' : (148,0,211),
            'leg' : (239,204,0)
        }
        self.commont = '[Common]'
        self.uncommont = '[Uncommon]'
        self.raret = '[Rare]'
        self.epict = '[Epic]'
        self.legt = '[Legendary]'

    # Sets the targeted player for the system, allowing the system to print the players status
    def setPlayer(self,player):
        self.player = player

    #Controls whether the terminal will be cleared or not. Also allows for compatibility between operating systems (Debugging)
    def wipe(self):
        if self.ClearTerminal:
            os.system('cls' if os.name=='nt' else 'clear')

    def col(self,colour,text):
        if self.settingsDict['Text Colours']:
            rgb = self.colourDict[colour]
            return f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{text}\033[0m" 
        else:
            return text

    # Prints the players status
    def playerStatus(self):
        self.player.healthbar.update()
        topBanner = f"{self.divChar*self.sideDivLen} {self.player.name} Level {self.player.lvl} {self.divChar*self.sideDivLen}"
        print(topBanner)
        if self.player.lvl >= self.player.maxlvl:
            print(f'Experience: {self.col("heal","Max Level")}')
        elif self.player.xp >= self.player.maxxp:
            print(f'Experience: {self.col("heal",self.player.xp)}/{self.player.maxxp}')
        else:
            print(f'Experience: {self.player.xp}/{self.player.maxxp}')
        print(f'Gold: {self.col("gold",f"{self.player.gold}")}')
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
        if self.settingsDict['Hints']:
            if space:
                print()
            input(self.col('hint',text))
        else:
            input()

    def hint(self,text):
        if self.settingsDict['Hints']:
            print(self.col('hint',text))

    def printSettings(self):
        settingChoice = True
        while settingChoice:
            self.wipe()
            header = '--- Your Current Settings ---'
            print(header)
            for setting in self.settingsDict:
                print(f'{setting}: {"On" if self.settingsDict[setting] else "Off"}'.center(len(header)))
            print()
            print(f'Colour Test: {self.col("heal","█"*10)}')
            print('If the bar above is grey while text colours are enabled, please turn off text colours to ensure you have the best experience.')
            print()
            print(self.col('hint','Type a specific setting with "off" or "on" at the end to turn a setting on or off.\nPress enter to return back to the main menu.'))
            choice = self.Option(options=[optionDict['hintsoff'],optionDict['hintson'],optionDict['coloursoff'],optionDict['colourson'],['','back','main menu','menu','leave']],errorMsg='Unknown setting. Please try again')

            if choice in optionDict['hintsoff']:
                self.settingsDict['Hints'] = False
                text('Hints have been turned off.\nType "hints on" to turn them back on.')
            elif choice in optionDict['hintson']:
                self.settingsDict['Hints'] = True
                text('Hints have been turned on.\nType "hints off" to turn them back off.')

            elif choice in optionDict['coloursoff']:
                self.settingsDict['Text Colours'] = False
                text('Text colours have been turned off.\nType "colours on" to turn them back on.')
            elif choice in optionDict['colourson']:
                self.settingsDict['Text Colours'] = True
                text('Text colours have been turned on.\nType "colours off" to turn them back off.')
            
            else:
                settingChoice = False

    #Returns a players choice from a list of options
    def Option(self,options,Map=False,WeaponInfo=False,errorMsg='Unknown action. Please try again'):
        choosing = True
        while choosing:
            choice = input('> ').lower().strip()
            for option in options:
                if choice in option:
                    return choice

            # Constant Options
            if choice in optionDict['quit']:
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
                print(errorMsg)

syst = System()