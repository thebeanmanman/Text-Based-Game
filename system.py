from time import sleep
import os
from dictionaries import optionDict

class System():
    #Control Variables
    ClearTerminal = True
    Devmap = False
    NarSpeed = 0.05

    # Settings Variables
    settingsDict = {
        'Hints' : True,
        'Text Colours' : True,
        'Text Animations' : True
    }
    def __init__(self):
        self.playing = False

        #Player Status Variables
        self.divChar = '─'
        self.sideDivLen = 5

        # Player Stats
        self.deaths = 0
        self.enemiesDefeated = 0
        self.chestsOpened = 0
        self.itemsUsed = 0

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
            'legendary' : (239,204,0)
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

    #Creates a smooth text animation
    def text(self,toprint,end='\n',time=0) -> None:
        if self.settingsDict['Text Animations']:
            for line in str(toprint).split('\n'):
                avoidValues = []
                i = 0
                while i < len(line):
                    if line[i] == '\033':
                        End = line.find('m',i)
                        for j in range(i,End+1):
                            avoidValues.append(j)
                        i = End+1
                    else:
                        i+=1
                if not time:
                    totalLen = len(line)-len(avoidValues)
                    if totalLen > 20:
                        texttime = 1.85/totalLen
                    else:
                        texttime = 1/totalLen
                else:
                    texttime = time
                for charNum,char in enumerate(line):
                    print(char,flush=True,end='')
                    if char == '.':
                        sleep(0.4)
                    elif char == '?':
                        sleep(0.8)
                    else:
                        if charNum not in avoidValues:
                            sleep(texttime)
                print(end,end='')
        else:
            print(toprint)

    # A method which allows for the addition of Narrartor dialogue much quicker and easier
    def nar(self,text,enterHint=True,clear=True):
        self.text(toprint=self.col('nar',text),time=self.NarSpeed)
        if enterHint:
            self.enterHint()
        if clear:
            self.printStatus()

    # A method to allow for the implementation of dialogue from npc's a lot easier
    def npc(self,name,text,enterHint=True,clear=True):
        print(f'{name}: ',end='')
        self.text(self.col('npc',text))
        if enterHint:
            self.enterHint()
        if clear:
            self.printStatus()

    # Colours the provided text, if colours are on
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
            print(self.col('hint',text))
            input()
        else:
            input()

    # Creates a hint that is only displayed when hints are on
    def hint(self,text):
        if self.settingsDict['Hints']:
            print(self.col('hint',text))

    # Prints the current settings, allowing the player to modify them
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
            choice = self.Option(options=[optionDict['hintsoff'],optionDict['hintson'],optionDict['coloursoff'],optionDict['colourson'],optionDict['animationsoff'],optionDict['animationson'],['','back','main menu','menu','leave']],errorMsg='Unknown setting. Please try again')

            if choice in optionDict['hintsoff']:
                self.settingsDict['Hints'] = False
                self.text('Hints have been turned off.\nType "hints on" to turn them back on.')
            elif choice in optionDict['hintson']:
                self.settingsDict['Hints'] = True
                self.text('Hints have been turned on.\nType "hints off" to turn them back off.')

            elif choice in optionDict['coloursoff']:
                self.settingsDict['Text Colours'] = False
                self.text('Text colours have been turned off.\nType "colours on" to turn them back on.')
            elif choice in optionDict['colourson']:
                self.settingsDict['Text Colours'] = True
                self.text('Text colours have been turned on.\nType "colours off" to turn them back off.')

            elif choice in optionDict['animationsoff']:
                self.settingsDict['Text Animations'] = False
                self.text('Text animations have been turned off.\nType "animations on" to turn them back on.')
            elif choice in optionDict['animationson']:
                self.settingsDict['Text Animations'] = True
                self.text('Text animations have been turned on.\nType "animations off" to turn them back off.') 
            
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
                self.text('Thanks for playing!')
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

    # Run at the end of the game
    def endGame(self):
        self.playing = False
        self.nar('You enter a white room, that seemingly goes on forever...\nYou see that there is a man standing in the middle of the room.\nAs it would seem, he is the one who is talking to you right now.\nI am the narrator of your story, I am glad to finally talk to you face to face.\nYou have passed all of my tests with apparent ease...\nBut I wonder whether you can do it any quicker?',clear=False,enterHint=False)
        self.enterHint()
        self.wipe()
        print('-- The End --')
        sleep(1)
        print('Your Stats:')
        sleep(1)
        print(f'Deaths: {self.deaths}')
        sleep(1)
        print(f'Enemies Defeated: {self.enemiesDefeated}')
        sleep(1)
        print(f'Treasure Chests Opened: {self.chestsOpened}')
        sleep(1)
        print(f'Items Used: {self.itemsUsed}')
        sleep(1)
        print()
        input('Press enter to quit the game')
        quit()

syst = System()