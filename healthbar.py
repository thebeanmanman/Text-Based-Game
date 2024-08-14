from grammar import Plural
from system import syst

class HealthBar():
    remaininghp = '█'
    losthp = '█'
    end = '│'
    death = '─'

    def __init__(self,
                 entity,
                 length = 10,
                 type = ''
                 ) -> None:
        self.entity = entity
        self.length = length
        self.maxvalue = entity.maxhp
        self.currvalue = entity.hp
        self.type = type

    def update(self):
        self.currvalue = self.entity.hp
        self.maxvalue = self.entity.maxhp

    def getBar(self):
        remaining = round(self.currvalue/self.maxvalue*self.length)
        lost = self.length - remaining

        if syst.settingsDict['Text Colours']:
            lostChar = self.losthp
        else:
            lostChar = self.death

        if self.currvalue:
            if self.type == 'player':
                bar = f'{self.end}{syst.col("heal",f"{remaining*self.remaininghp}")}{syst.col("lightred",lost*lostChar)}{self.end} {self.entity.hp}/{self.entity.maxhp}'
            elif self.type == 'enemy':
                bar = f'{self.end}{syst.col("red",f"{remaining*self.remaininghp}")}{syst.col("lightred",lost*lostChar)}{self.end} {self.entity.hp}/{self.entity.maxhp}'
            else:
                bar = f'{self.end}{remaining*self.remaininghp}{lost*lostChar}{self.end} {self.entity.hp}/{self.entity.maxhp}'
            
            if self.entity.poisonDur:
                bar += f""" {syst.col("poison",f"[Poisoned for {self.entity.poisonDur} {Plural(self.entity.poisonDur, 'turn')}]")}"""
            
            if self.entity.defenceDur:
                bar += f""" {syst.col("defence",f"[+{self.entity.defence} defence for {self.entity.defenceDur} {Plural(self.entity.defenceDur,'turn')}]")} """
            if self.entity.strengthDur:
                bar += f""" {syst.col("strength",f"[+{self.entity.strength} strength for {self.entity.strengthDur} {Plural(self.entity.strengthDur,'turn')}]")} """

        else:
            bar = f'{self.end}{self.death*self.length}{self.end} {self.entity.hp}/{self.entity.maxhp}'

        return bar