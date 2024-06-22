#
# ! 
# TODO: Create a game class that handles running the game loop

#Import Modules
from random import randint
import os

#Import Classes
from entity import Player,Enemy
from weapons import shortBow,ironSword
from dungeon import Level1

#Import Functions
from functions import text,option,wipe

#Import Names
from names import Goblinlist

#Global Variables
gameName = 'Dungeon Runner'

def titleSelect():
    choice = option(['play','help','quit'])
    if choice == 'play':
        startGame()
    elif choice == 'help':
        helpMenu()
    elif choice == 'quit':
        text('Thanks for playing!')

def title_screen():
    wipe()
    print(f'---Welcome to {gameName}!---')
    text('- Play')
    text('- Help')
    text('- Quit')
    titleSelect()

def helpMenu():
    wipe()
    print(f'---Welcome to {gameName}!---')
    text('Type up, down, left and right to move')
    text('Press enter to return to the menu')
    input()
    title_screen()

def startGame():
    hero = Player(name='The Main Character', maxhp=100, DungLvl=Level1)
    hero.equip(ironSword)
    hero.room = Level1.startRoom
    hero.room.enter(hero)

title_screen()