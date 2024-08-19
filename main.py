#Import Classes
from entity import Player
from shop import Shop

# Import Objects
from system import syst

# Import dictionaries
from dungeon import Dungeon,floorStatDict,floorDict
from dictionaries import optionDict

#Global Variables
gameName = 'Dungeon Runner'

# Allows the player to choose an option from the title screen
def titleSelect():
    choice = syst.Option(options=[['play'],['quit'],['settings']])
    if choice == 'play':
        startGame()
    elif choice == 'quit':
        syst.text('Thanks for playing!')
        quit()
    elif choice == 'settings':
        settingsMenu()
# Main Menu
def title_screen():
    header = f'--- Welcome to {gameName}!---'
    syst.wipe()
    print(header)
    print()
    print('▸ Play ◂'.center(len(header)))
    print('▸ Settings ◂'.center(len(header)))
    print('▸ Quit ◂'.center(len(header)))
    print()
    titleSelect()

# Shows the player the current settings
def settingsMenu():
    syst.wipe()
    syst.printSettings()
    title_screen()

# Starts the game
def startGame():
    syst.playing = True
    rounds = 1
    while syst.playing:
        if rounds == 1:
            syst.printStatus()
            syst.nar("You awake in field of tall, flowing, green, grass.\nGradually, you open your eyes.\nThey gently adjust to the warm sunlight splashing on your face, taking in the electric blue of the sky above you.")
            syst.nar("Slowly, your body begins to wake up and you summon enough strength to stand.\nYou feel a sense of confidence wash over you, wanting everyone to know the name of...\n \nHang on... What is your name?",enterHint=False,clear=False)
            nameSelect = True
            while nameSelect:
                name = input('> ')
                if len(name) > 20:
                    syst.nar('Do you expect me to say that every single time?!\nPlease pick a shorter name.',enterHint=False,clear=False)
                elif not name:
                    syst.nar("That isn't a name...\nPlease at least come up with something.",enterHint=False,clear=False)
                else:
                    nameSelect = False
            player.setName(name),
            syst.printStatus()
            syst.nar(f'''{player.name}... Is that your actual name?\nBecause it really doesn't roll off the tongue all that well...\nNarrating is a very difficult job as it is, and you choosing a name such as "{player.name}" really doesn't help...\nSigh... I guess I'll let it slide.\nAnyways what was I saying?\nOh yeah that's right...''')
            syst.nar(f'''"{player.name}", in their somewhat weakened state, spotted that just past the rolling fields of grass, there was a village.\nIntrigued by what they may find at the village, {player.name} set off to satiate their curiosity.''')
            syst.nar('''After what felt like countless hours of travelling through the rolling grassy fields,\nYou stumble upon a dirt path leading to the village.\nFrom here, you could already smell the warm aroma of freshly baked bread. Eager to explore, you hastily make your way into the village square.''')
            syst.nar('''Cottages line the street, they are simple, yet sturdy, each one telling a story of the generations that have lived there.\nYou notice many residents of the village wandering about, yet something seems off.\nThe villagers friendly smiles waver just slightly when they catch your gaze, and their conversations grow quieter as you pass by.\nIt's as if they know something, something unsaid, their eyes potraying a hint of worry and fear.''')
            syst.nar('''Suddenly, you hear someone call out to you. It seems to be a humble merchant who is selling his wares from a small stall.''')
            syst.npc('Shopkeeper','Hello there young traveller, comes take a look at my wares...')
            syst.npc("Shopkeeper","Oh? What's that? You have no gold? Well... I do have a solution for you.")
            syst.npc("Shopkeeper","You see, in the outskirts of this town there lies a dungeon, And within it there is much treasure... Yet much danger...")
            syst.npc("Shopkeeper","Here is a map that leads you to the dungeon. I wish you the best of luck in your travels.")
            syst.nar('''And so, with a renewed sense of purpose, you decide to set off towards the dungeon...''')
            syst.nar('''Eventually, you find yourself standing at the entrance of the dungeon.\nLarge grandiose doors tower above you, daring you to step inside.''')
            syst.nar('''You cautiously push them open, and through them you find a small room with a lever to the side.''')
            syst.nar('''You push the lever, and the wooden platform beneath your feet begins to descend...''')
            enterDungeon()
        elif rounds == 2:
            player.deathReset()
            syst.printStatus()
            syst.nar('''You wake up startled...\n"Shouldn't I be dead?" You ask yourself.\nThen you begin to notice that you are in the same grassy field that you started in.''')
            syst.nar('''Incredibly confused, you decide to head back to the village.\nOnce you get there, you encounter the shopkeeper once again.''')
            shopEncounter()
        else:
            player.deathReset()
            syst.printStatus()
            syst.nar('''You wake up in that same grassy field...\nWould you like to head to the shop or go straight to the dungeon?''',clear=False,enterHint=False)
            choice = syst.Option([optionDict['market'],optionDict['dungeon']])
            if choice in optionDict['market']:
                syst.nar('You decide to go visit the shopkeeper...')
                shopEncounter()
            elif choice in optionDict['dungeon']:
                syst.nar('You decide to head straight to the dungeon...')
                syst.nar('Once you arrive, you enter and flick the lever, and the platform begins to descend once again.')
                enterDungeon()
        rounds += 1

# Run the allow the player to open the shop
def shopEncounter():
    shop = Shop(sellWeapons=True,itemNumber=3,dialogue=f"Shopkeeper: {syst.col('npc','Hello again young traveller, please take a look at my fine wares.')}",name="Shopkeeper's Store")
    shop.enterShop(player)
    syst.printStatus()
    syst.nar('''You decide to leave the shop and you make your way back to the dungeon to make sense of things...\nOnce you arrive, you enter and flick the lever, and the platform begins to descend once again.''')
    enterDungeon()

# Regenerates dungeon floors
def generateFloors():
    for floornum,floor in enumerate(floorStatDict,start=1):
        floorDict[floornum] = Dungeon(**floorStatDict[floor],Floor=floornum)
    
# Run to allow the player to enter the dungeon
def enterDungeon():
    generateFloors()
    player.setDungeonFloor(floorDict[1])
    syst.wipe()
    player.room = floorDict[1].startRoom
    player.room.enter(player)

player = Player(maxhp=10)
syst.setPlayer(player)
print('Notes from the developer:\n- Before you begin your journey, please ensure you have checked the setting menu and adjusted your colour settings.\n- Please play this game in fullscreen for the best experience.\n- Most importanly, have fun.')
syst.enterHint('Press enter to continue to the game.')
title_screen()

startGame()