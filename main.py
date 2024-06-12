from random import randint
from time import sleep
def text(toprint):
    texttime = 0.75/len(toprint)
    toprint = str(toprint)
    for char in toprint:
        print(char,flush=True,end='')
        if char == '.':
            sleep(texttime*20)
        else:
            sleep(texttime)
    print('\n',end='')
class Goblin():
    pos = [randint(-3,3),randint(-3,3)]
    health = randint(1,3)
    damage = randint(1,2)
    def turn(self):
        if self.pos == Player.pos:
            self.battle()
    def battle(self):
        Player.health -= self.damage
        text(f'Hit! You take {self.damage} damage from {self}')
class Player():
    pos = [0,0]
    health = 10
    def move(self,x,y):
        self.pos[0] += x
        self.pos[1] += y
class Item():
    def __init__(self,name,x,y):
        self.pos = [x,y]
        self.name = name
        

Play = True
Player1 = Player()
Gobby = Goblin()
text(Gobby.pos)
while Play:
    text(f"Pos: {Player1.pos}")
    Direction = input('Enter Direction: ')
    if Direction == 'w':
        Player1.move(0,1)
    elif Direction == 'a':
        Player1.move(-1,0)
    elif Direction == 's':
        Player1.move(0,-1)
    elif Direction == 'd':
        Player1.move(1,0)
    Gobby.turn()