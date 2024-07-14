from colours import col
class HealthBar():
    remaininghp = '█'
    losthp = '─'
    end = '│'

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

    def getBar(self):
        remaining = round(self.currvalue/self.maxvalue*self.length)
        lost = self.length - remaining
        if self.type == 'player':
            return f'{self.end}{col.heal(f"{remaining*self.remaininghp}")}{lost*self.losthp}{self.end} {self.entity.hp}/{self.entity.maxhp}'
        elif self.type == 'enemy':
            return f'{self.end}{col.red(f"{remaining*self.remaininghp}")}{lost*self.losthp}{self.end} {self.entity.hp}/{self.entity.maxhp}'
        else:
            return f'{self.end}{remaining*self.remaininghp}{lost*self.losthp}{self.end} {self.entity.hp}/{self.entity.maxhp}'