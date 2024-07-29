from colours import col

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
        if self.currvalue:
            if self.type == 'player':
                bar = f'{self.end}{col.name("heal",f"{remaining*self.remaininghp}")}{col.name("lightred",lost*self.losthp)}{self.end} {self.entity.hp}/{self.entity.maxhp}'
            elif self.type == 'enemy':
                bar = f'{self.end}{col.name("red",f"{remaining*self.remaininghp}")}{col.name("lightred",lost*self.losthp)}{self.end} {self.entity.hp}/{self.entity.maxhp}'
            else:
                bar = f'{self.end}{remaining*self.remaininghp}{lost*self.losthp}{self.end} {self.entity.hp}/{self.entity.maxhp}'
            
            if self.entity.poisonDur:
                bar += f' {col.name("poison",f"[Poisoned for {self.entity.poisonDur} turns]")}'

        else:
            bar = f'{self.end}{self.death*self.length}{self.end} {self.entity.hp}/{self.entity.maxhp}'

        return bar