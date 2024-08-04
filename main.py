#Import Classes
from entity import Player
from shop import Shop

# Import Objects
from items import ironSword
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
    header = f'--- Welcome to {gameName}!---'
    syst.wipe()
    print(header)
    print()
    print('▸ Play ◂'.center(len(header)))
    print('▸ Help ◂'.center(len(header)))
    print('▸ Quit ◂'.center(len(header)))
    print()
    titleSelect()

def helpMenu():
    syst.wipe()
    print(f'--- Welcome to {gameName}!---')
    text('Type up, down, left and right to move')
    text('Press enter to return to the menu')
    input()
    title_screen()


def startGame():
    syst.playing = True
    rounds = 1
    while syst.playing:
        if rounds == 1:
            syst.wipe()
            # text(toprint=col.name('nar',"You awake in field of long flowing grass, gradually opening your eyes,\nThey slowly adjust to the warm sunlight splashing on your face,\nTaking in the electric blue of the sky above you,\nSlowly, your body begins to wake up and you summon enough strength to stand.\nYou feel a sense of confidence wash over you, wanting everyone to know the name of...\n \nHang on... What is your name?"),time=syst.NarSpeed)
            name = input('> ')
            player.setName(name),
            syst.wipe()
            # text(toprint=col.name('nar',f"Oh of course! I knew that...\nWell anyways as I was saying...\nYou feel a sense of confidence wash over you, wanting everyone to know the name of... {player.name}.\nHang on... I'm sorry is that your actual name?\nBecause it really doesn't roll off the tongue all that well...\nNarrating is a very difficult job as it is, and you choosing a name such as {player.name} really doesn't help."),time=syst.NarSpeed)
            # text(toprint=col.name)
            # # Add more later...

            # text(col.name('nar',f'You encounter a humble shopkeeper selling his wares in the village.'))
            shopEncounter()
        else:
            player.deathReset()
            syst.printStatus()
            text(col.name('nar',f'You encounter a humble shopkeeper selling his wares in the village.'))
            shopEncounter()
        rounds += 1

def shopEncounter():
    if player.gold > 0:
        text(f"Shopkeeper: {col.name('npc','Hello there young traveller, take a look at my fine wares.')}")
        shop = Shop(sellWeapons=True,name="Shopkeeper's Store")
        shop.printItems()
        shop.enterShop(player)
        enterDungeon()
    else:
        text(f"Shopkeeper: {col.name('npc','Hello there young traveller, please come back to my store when your pockets are full of gold.')}")
        enterDungeon()
    
def enterDungeon():
    Floor1 = Dungeon(rooms=[TreasureRoom,EnemyRoom],roomNum=13,reqRooms=None,mapsize=9,Floor=1,roomChances=[6,20])
    player.setDungeonFloor(Floor1)
    syst.wipe()
    player.room = Floor1.startRoom
    player.room.enter(player)

player = Player(maxhp=10)
syst.setPlayer(player)
title_screen()