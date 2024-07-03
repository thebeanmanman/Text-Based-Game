from colours import col

class System():
    def __init__(self,player):
        self.player = player

        #Battle Menu Variables
        self.divChar = '-'
        self.sideDivLen = 4

    def playerStatus(self):
        topBanner = f"{self.divChar*self.sideDivLen} {self.player.name} Level {self.player.lvl} {self.divChar*self.sideDivLen}"
        print(topBanner)
        print(f'XP: {self.player.xp}/20')
        print(f'Gold: {col.gold(f"{self.player.gold}")}')
        print(f'Health: {self.player.hp}/{self.player.maxhp}')
        print(self.divChar*len(topBanner))

    def setLocation(self,desc):
        self.locationDesc = desc