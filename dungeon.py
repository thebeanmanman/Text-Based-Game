# Import external modules
from random import choices,randint
import copy

# Import System
from system import syst

# Import Enemies
from entity import Enemy

# Import Functions
from functions import text,randItem,chance

# Import Dictionaries
from dictionaries import iconDict,optionDict,roomDescDict

# Import Grammar
from grammar import orChoice

# Import Weapon Rarity Tiers
from items import common,uncommon,rare,epic,legendary,enemyDict,bossDict

class Dungeon():
    def __init__(self,roomTypes:list,roomAmts:list,mapsize:int,Floor:int) -> None:
        self.startRoom = StartRoom(Floor)
        self.Floor = Floor
        self.roomTypes = roomTypes
        self.roomAmts = roomAmts

        self.mapsize = mapsize
        self.map = []
        for i in range(mapsize):
            row = []
            for j in range(mapsize):
                row.append('')
            self.map.append(row)

        self.generateDungeon()

    def generateDungeon(self):
        instantiatedRooms = []
        for index,roomType in enumerate(self.roomTypes):
            for i in range(self.roomAmts[index]):
                room = roomType(self.Floor)
                instantiatedRooms.append(room)

        rooms = 1
        center = self.mapsize//2
        x = center
        y = center
        currRoom = self.startRoom
        while instantiatedRooms and rooms <= self.mapsize**2:
            self.map[y][x] = currRoom
            currRoom.x = x
            currRoom.y = y
            currRoom.floorObject = self
            rooms += 1
            if rooms <= self.mapsize**2:
                x,y = center,center
                while self.map[y][x]:
                    dirList = self.DirList(x,y)
                    if dirList:
                        direction = randItem(dirList)
                        x,y = direction[1],direction[0]
                    else:
                        x,y = center,center
                if currRoom.roomName != 'StartRoom':
                    instantiatedRooms.remove(currRoom)
                currRoom = randItem(instantiatedRooms)
        self.createDevmap()

    def DirList(self,x,y):
        dirList = []
        if y-1 >= 0:
            dirList.append([y-1,x])
        if y+1 < self.mapsize:
            dirList.append([y+1,x])
        if x-1 >= 0:
            dirList.append([y,x-1])
        if x+1 < self.mapsize:
            dirList.append([y,x+1])
        return dirList

    def mapNoDirCheck(self,x,y):
        dirList = []
        if y-1 >= 0 and not self.map[y-1][x]:
            dirList.append([y-1,x])
        if y+1 < self.mapsize and not self.map[y+1][x]:
            dirList.append([y+1,x])
        if x-1 >= 0 and not self.map[y][x-1]:
            dirList.append([y,x-1])
        if x+1 < self.mapsize and not self.map[y][x+1]:
            dirList.append([y,x+1])

        return dirList
    
    def mapDirCheck(self,x,y):
        dirList = []
        if y-1 >= 0 and self.map[y-1][x]:
            dirList.append(optionDict['north'])
        if y+1 < self.mapsize and self.map[y+1][x]:
            dirList.append(optionDict['south'])
        if x+1 < self.mapsize and self.map[y][x+1]:
            dirList.append(optionDict['east'])
        if x-1 >= 0 and self.map[y][x-1]:
            dirList.append(optionDict['west'])
        return dirList
    
    def mapRoomCheck(self,x,y):
        roomList = []
        if y-1 >= 0 and self.map[y-1][x]:
            roomList.append(self.map[y-1][x])
        if y+1 < self.mapsize and self.map[y+1][x]:
            roomList.append(self.map[y+1][x])
        if x+1 < self.mapsize and self.map[y][x+1]:
            roomList.append(self.map[y][x+1])
        if x-1 >= 0 and self.map[y][x-1]:
            roomList.append(self.map[y][x-1])
        return roomList
    
    def createDevmap(self):
        self.devmap = []
        for row in self.map:
            newrow = []
            for room in row:
                if room:
                    newrow.append(room.icon)
                else:
                    newrow.append(iconDict['Blank'])
            self.devmap.append(newrow)
        
    # Prints the Map 
    def printMap(self,map):
        print('')
        for row in map:
            print(''.join(row))
        print('')
        # print(f'Your Location: {iconDict["Player"]}')
        # print(f'Treasure Room: {iconDict["Treasure Room"]}')
        # print(f'Unknown Room: {iconDict["Unknown Room"]}')
        # print(f'Start Room: {iconDict["Start Room"]}')
        # print(f'Enemy Room: {iconDict["Enemy Room"]}')
        # print(f'Stair Room: {iconDict["Stair Room"]}')

    # Prints the map shown to the players
    def printPlayerMap(self,player):
        # Map Creation
        hiddenMap = []
        for row in self.map:
            newrow = []
            for room in row:
                if room:
                    if player.room == room:
                        newrow.append(player.icon)
                    else:
                        if room.cleared:
                            newrow.append(room.icon)
                        elif room.discovered:
                            newrow.append(iconDict['Unknown Room'])
                        else:
                            newrow.append(iconDict['Blank'])
                else:
                    newrow.append(iconDict['Blank'])
            hiddenMap.append(newrow)
        
        # Map Printing
        self.printMap(hiddenMap)

class Room():
    def __init__(self,Floor) -> None:
        self.x = 0
        self.y = 0
        self.Floor = Floor
        self.floorObject = None
        self.cleared = False
        self.discovered = False
        self.roomName = self.__class__.__name__
        self.desc = roomDescDict[self.Floor][self.roomName]
        self.icon = iconDict['Default']

    # Default enter method always called when the player enters the room  (Unless overwritten)
    # This then runs subclass specific onEnter methods
    def enter(self,player):
        self.floorObject.devmap[self.y][self.x] = player.icon
        syst.printStatus()
        if self.cleared:
            text('You have already cleared this room.')
            self.move(player)
        else:
            text(self.desc)
            self.onEnter(player)

    # Allows the player to move between rooms
    def move(self,player):
        directions = self.floorObject.mapDirCheck(self.x,self.y)

        roomList = self.floorObject.mapRoomCheck(self.x,self.y)
        for Adjroom in roomList:
            Adjroom.discovered = True
        syst.enterHint()
        syst.printStatus()
        text(f'You can move {orChoice([direction[0] for direction in directions])}.')
        syst.hint('You can type "map" to see where you have already travelled.')
        direction = syst.Option(options=directions,Map=True,WeaponInfo=True)
        if direction in optionDict['north']:
            chosenRoom = self.floorObject.map[self.y-1][self.x]
        elif direction in optionDict['south']:
            chosenRoom = self.floorObject.map[self.y+1][self.x]
        elif direction in optionDict['west']:
            chosenRoom = self.floorObject.map[self.y][self.x-1]
        elif direction in optionDict['east']:
            chosenRoom = self.floorObject.map[self.y][self.x+1]

        if chosenRoom.__class__.__name__ == 'BossRoom' and not chosenRoom.cleared:
            text('You feel an ominous presence coming from that direction...\nAre you sure you want to continue?')
            confirm = syst.Option(options=[optionDict['yes'],optionDict['no']])
            if confirm in optionDict['no']:
                text('You decide not to go in that direction...')
                self.move(player)
                return

        self.floorObject.devmap[self.y][self.x] = self.icon
        player.room = chosenRoom
        player.room.enter(player)

    def clear(self):
        self.cleared = True
        text('You have cleared this room.')
    
class StartRoom(Room):
    def __init__(self, Floor) -> None:
        super().__init__(Floor)
        self.icon = iconDict[self.roomName]
        self.reEnter = roomDescDict[self.Floor]['ReEnterStartRoom']
    
    def enter(self, player):
        self.floorObject.devmap[self.y][self.x] = player.icon
        syst.printStatus()
        if self.cleared:
            text(self.reEnter)
        else:
            self.cleared = True
            text(self.desc)
        self.move(player)

class BossRoom(Room):
    def __init__(self, Floor) -> None:
        super().__init__(Floor)
        bossName = list(bossDict[self.Floor])[0]
        self.boss = Enemy(bossName, **bossDict[self.Floor][bossName])
        self.icon = iconDict[self.roomName]

    def enter(self,player):
        self.floorObject.devmap[self.y][self.x] = player.icon
        syst.printStatus()
        text(self.desc)
        if not self.cleared:
            player.battle(self.boss)
            if player.hp > 0:
                self.cleared = True
                text("A mysterious portal appears before you, seemingly out of thin air.\nThe portals shimmering texture intrigues you, almost inviting you step into it.")
                self.portalChoice(player)
        else:
            text('The portal still remains, inviting you to step inside it...')
            self.portalChoice(player)

    def portalChoice(self,player):
        text('Do you want to enter the portal?')
        choice = syst.Option(options=[optionDict['yes'],optionDict['no']])
        if choice in optionDict['yes']:
            text('You decide to step into the portal...')
            syst.enterHint()
            syst.wipe()
            player.setDungeonFloor(floorDict[self.Floor+1])
            player.room = floorDict[self.Floor+1].startRoom
            player.room.enter(player)
        elif choice in optionDict['no']:
            text('You decide not to step into the portal...')
            self.move(player)

class EnemyRoom(Room):
    def __init__(self,Floor) -> None:
        super().__init__(Floor)
        self.enemies = []
        self.icon = iconDict[self.roomName]
        
        self.rollEnemy()

    def rollEnemy(self):
        enemyNum  = randint(1,3)
        enemyTypes = list(enemyDict[self.Floor])
        enemyChances = [enemyDict[self.Floor][enemy]['spawnch'] for enemy in enemyTypes]
        for i in range(enemyNum):
            enemyName = choices(enemyTypes,weights=enemyChances,k=1)[0]
            InstantiatedEnemy = Enemy(enemyName,**enemyDict[self.Floor][enemyName])
            self.enemies.append(InstantiatedEnemy)

    def onEnter(self,player):
        self.battling = True
        enemy = self.spawnEnemy()
        while self.battling:
            player.battle(enemy)
            if player.hp <= 0:
                self.battling = False
            elif enemy.hp <= 0:
                self.enemies.pop(0)
                # text(f'There {AreIs(len(self.enemies))} {len(self.enemies)} {Plural(len(self.enemies),"enemy")} left.')
                enemy = self.spawnEnemy()
        if player.hp > 0:
            self.move(player)

    def spawnEnemy(self):
        if self.enemies:
            enemy = self.enemies[0]
            text(enemy.desc)
            return enemy
        else:
            self.battling = False
            self.clear()
    
class TreasureRoom(Room):
    def __init__(self,Floor):
        super().__init__(Floor)

        # Visual Variables:
        self.icon = iconDict[self.roomName]

        # Chances for each rarity tier
        self.commonCh = 37
        self.uncommonCh = 28
        self.rareCh = 19
        self.epicCh = 13
        self.legCh = 3

        # Mimic variables
        self.mimicChance = 0.1
        self.IsMimic = False
        self.Mimic = Enemy('Mimic',**enemyDict['misc']['Mimic'])

        # Rolls for loot and mimic chances
        self.rollTreasure()
        self.rollMimic()
    
    def rollTreasure(self):
        rarityLvl = choices([common,uncommon,rare,epic,legendary], weights=(self.commonCh,self.uncommonCh,self.rareCh,self.epicCh,self.legCh), k=1)[0]
        self.treasure = randItem(rarityLvl)
    
    def rollMimic(self):
        if chance(self.mimicChance):
            self.IsMimic = True        

    def onEnter(self,player):
        text('Open the chest?')
        answer = syst.Option(options=[optionDict['yes'],optionDict['open'],optionDict['no']])
        syst.printStatus()
        if answer in optionDict['yes'] or answer in optionDict['open']:
            text('Your curiousity is tempted by the chest and you approach it...')
            self.open(player)
        elif answer in optionDict['no']:
            text('You supress the desire to see what treasure awaits you and you move on.')
            self.clear()
            self.move(player)
        
    def open(self,player):
        text('Your hands swiftly unlock the chest, awaiting your reward...')
        if self.IsMimic:
            text(f'{syst.col("red","Only to find rows upon rows of gnashing teeth.")}') 
            player.battle(self.Mimic)
            if player.hp > 0:
                self.clear()
                self.move(player)
        else:
            text('You find an item lying in the bottom of the chest.')
            syst.enterHint()
            syst.printStatus()
            text(f'You have found a {self.treasure.rarname}!')
            self.treasure.showInfo()
            print()
            player.currentWeaponStats()
            print()
            text(f'Would you like to equip the {self.treasure.rarname}?')
            answer = syst.Option(options=[optionDict['no'],optionDict['yes']])
            if answer in optionDict['yes']:
                player.equip(self.treasure)
                self.clear()
                self.move(player)
            elif answer in optionDict['no']:
                text('You leave the item in the chest and move on.')
                self.clear()
                self.move(player)


# Specifies the attributes of each floor
floorStatDict = {
    'Floor 1' : {'roomTypes':[TreasureRoom,EnemyRoom,BossRoom],'roomAmts':[2,7,1],'mapsize':5},
    'Floor 2' : {'roomTypes':[TreasureRoom,EnemyRoom],'roomAmts':[2,10],'mapsize':7}
}

# Contains instantianted objects of each floor
floorDict = {}