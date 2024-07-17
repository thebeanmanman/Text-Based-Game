#Import Classes
from entity import Player

# Import Objects
from weapons import ironSword
from dungeon import *
from system import syst
from colours import col

#Import Functions
from functions import text

#Global Variables
gameName = 'Dungeon Runner'

def titleSelect():
    choice = syst.Option(Other=True,OtherList=['play','help','quit'])
    if choice == 'play':
        startGame()
    elif choice == 'help':
        helpMenu()
    elif choice == 'quit':
        text('Thanks for playing!')
        quit()

def title_screen():
    syst.wipe()
    print(f'--- Welcome to {gameName}!---')
    text('- Play')
    text('- Help')
    text('- Quit')
    titleSelect()

def helpMenu():
    syst.wipe()
    print(f'--- Welcome to {gameName}!---')
    text('Type up, down, left and right to move')
    text('Press enter to return to the menu')
    input()
    title_screen()

def startGame():
    Level1 = Dungeon(rooms=[TreasureRoom,EnemyRoom],roomNum=13,reqRooms=None,mapsize=9,Level=1,roomChances=[6,20])
    hero = Player(maxhp=10, DungLvl=Level1)
    syst.setPlayer(hero)
    syst.wipe()
    text('What is your name?')
    hero.setName('Jimmy')
    # text(col.nar(randItem(['What a strange name.\nYou are definitley going to be bullied for that.'])))
    # hero.equip(ironSword)
    hero.room = Level1.startRoom
    hero.room.enter(hero)

title_screen()