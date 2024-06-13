#Import Modules
from random import randint
from time import sleep
import os

#Import Classes
from entity import Player,Enemy
from weapons import shortBow,ironSword

#Import Functions
from loop import text

#Import Names
from names import GOBBYLIST

os.system('cls')
hero = Player(name='The Main Character', maxhp=100)
hero.equip(ironSword)
goblin = Enemy(name=GOBBYLIST[randint(0,len(GOBBYLIST))], maxhp=20, weapon=shortBow)
hero.drop()
while True:
    hero.attack(goblin)
    goblin.attack(hero)

    text(f'HP of {hero.name}: {hero.hp}')
    text(f'HP of {goblin.name}: {goblin.hp}')

    input()
'''
Gobby = Goblin()
text(Gobby.pos)
Start = True
while Start:
    Start = False
Play = True
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
    Gobby.turn(Player1)
'''