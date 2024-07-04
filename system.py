from colours import col
from functions import text,wipe
from time import sleep

class System():
    def __init__(self):
        self.locationDesc = ''
        self.stateDesc = ''

        #Battle Menu Variables
        self.divChar = '-'
        self.sideDivLen = 4

    def setPlayer(self,player):
        self.player = player

    def setLocation(self,desc):
        text(desc)
        self.locationDesc = desc

    def addLocation(self,desc):
        self.playerStatus()
        print(self.locationDesc)
        text(desc)
        self.locationDesc += '\n'+desc

    def setState(self,desc):
        self.playerStatus()
        if self.locationDesc:
            print(self.locationDesc)
            print(self.fullDiv)
        text(desc)
        self.stateDesc = desc

    def addState(self,desc):
        text(desc)
        self.stateDesc += '\n'+desc

    def playerStatus(self):
        topBanner = f"{self.divChar*self.sideDivLen} {self.player.name} Level {self.player.lvl} {self.divChar*self.sideDivLen}"
        print(topBanner)
        print(f'XP: {self.player.xp}/20')
        print(f'Gold: {col.gold(f"{self.player.gold}")}')
        print(f'Health: {self.player.hp}/{self.player.maxhp}')
        print(f'Weapon: {self.player.weapon.name}')
        self.fullDiv = self.divChar*len(topBanner)
        print(self.fullDiv)

    def div(self):
        print(self.fullDiv)
        sleep(0.5)

    def printStatus(self):
        wipe()
        self.playerStatus()
        if self.locationDesc:
            print(self.locationDesc)
            print(self.fullDiv)
        if self.stateDesc:
            print(self.stateDesc)
            print(self.fullDiv)

syst = System()