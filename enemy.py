class Enemy():
    def __init__(self,x,y,maxhealth,damage):
        self.pos = [x,y]
        self.maxhealth = maxhealth
        self.damage = damage
        self.name = GOBBYLIST[randint(0,len(GOBBYLIST))]
    def turn(self):
        if self.pos == Player.pos:
            self.battle()
    def battle(self):
        Player.health -= self.damage
        text(f'Hit! You take {self.damage} damage from {self.name} The Goblin')