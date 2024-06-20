#Import Modules
from random import randint
import os

#Import Classes
from entity import Player,Enemy
from weapons import shortBow,ironSword

#Import Functions
from functions import text

#Import Names
from names import Goblinlist

#Global Variables
gameName = 'Dungeon Runner'

def titleselect():
    select = True
    while select:
        option = input('> ').lower()
        if option == 'play':
            select = False
            # startgame()
        elif option == 'help':
            select = False
            help_menu()
        elif option == 'quit':
            text('Thanks for playing!')
            select = False
        else:
            text('Unknown command. Please try again')

def title_screen():
    os.system('cls')
    print(f'---Welcome to {gameName}!---')
    text('- Play')
    text('- Help')
    text('- Quit')
    titleselect()

def help_menu():
    os.system('cls')
    print(f'---Welcome to {gameName}!---')
    text('Type up, down, left and right to move')
    text('Press enter to return to the menu')
    input()
    title_screen()

title_screen()
'''

hero = Player(name='The Main Character', maxhp=100)
hero.equip(ironSword)
goblin = Enemy(name=Goblinlist[randint(0,len(Goblinlist))], maxhp=20, weapon=shortBow)
# hero.drop()
while True:
    #Create a use function for weapons that handle crits and stuff
    hero.attack(goblin)
    goblin.attack(hero)

    text(f'HP of {hero.name}: {hero.hp}')
    text(f'HP of {goblin.name}: {goblin.hp}')

    input()
'''