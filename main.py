#
# ! 
# TODO: Create a game class that handles running the game loop

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

def titleSelect():
    option = input('> ').lower()
    if option == 'play':
        startGame()
    elif option == 'help':
        helpMenu()
    elif option == 'quit':
        text('Thanks for playing!')
    else:
        text('Unknown command. Please try again')
        titleSelect()

def title_screen():
    os.system('cls')
    print(f'---Welcome to {gameName}!---')
    text('- Play')
    text('- Help')
    text('- Quit')
    titleSelect()

def helpMenu():
    os.system('cls')
    print(f'---Welcome to {gameName}!---')
    text('Type up, down, left and right to move')
    text('Press enter to return to the menu')
    input()
    title_screen()

def startGame():
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

title_screen()
