from colours import col
from functions import text,wipe
from time import sleep

class System():
    def __init__(self):
        self.locationDesc = ''
        self.stateDesc = ''

        #Battle Menu Variables
        self.divChar = '-'
        self.sideDivLen = 5

    def setPlayer(self,player):
        self.player = player

    def playerStatus(self):
        topBanner = f"{self.divChar*self.sideDivLen} {self.player.name} Level {self.player.lvl} {self.divChar*self.sideDivLen}"
        print(topBanner)
        print(f'XP: {self.player.xp}/20')
        print(f'Gold: {col.gold(f"{self.player.gold}")}')
        print(f'Health: {self.player.hp}/{self.player.maxhp}')
        print(f'Weapon: {self.player.weapon.name}')
        self.fullDiv = self.divChar*len(topBanner)
        print(self.fullDiv)

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