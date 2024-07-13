# Import external modules
from random import choices,randint

# Import System
from system import syst

# Import Enemies
from entity import Mimic,Goblin,Spider

# Import Functions
from functions import text,randItem,Option,chance

# Import Dictionaries
from dictionaries import iconDict,optionDict

# Import Grammar
from grammar import orChoice,AreIs,Plural

# Import Weapons
from weapons import common,uncommon,rare,epic,legendary

#Import Colours
from colours import col

class Dungeon():
    def __init__(self,reqRooms:list,rooms:list,roomNum:int,mapsize:int,Level:int,roomChances:list) -> None:
        self.reqRooms = reqRooms
        self.rooms = rooms
        self.roomNum = roomNum
        self.startRoom = StartRoom(Level)
        self.Level = Level
        self.roomChances = roomChances

        self.mapsize = mapsize
        self.map = []
        for i in range(mapsize):
            row = []
            for j in range(mapsize):
                row.append('')
            self.map.append(row)

        self.NewGen()

    def NewGen(self):
        Generate = True
        center = self.mapsize//2
        x = center
        y = center
        currRoom = self.startRoom
        i = 0
        while i <= self.roomNum or self.reqRooms:
            self.map[y][x] = currRoom
            currRoom.x = x
            currRoom.y = y
            currRoom.lvl = self
            x,y = center,center
            while self.map[y][x]:
                dirList = self.NewDirList(x,y)
                if dirList:
                    direction = randItem(dirList)
                    x,y = direction[1],direction[0]
                else:
                    x,y = center,center
            if i <= self.roomNum:
                currRoom = self.rollRooms()
                i += 1
            else:
                currRoom = randItem(self.reqRooms)
                self.reqRooms.remove(currRoom)

        self.createDispMap()

    def NewDirList(self,x,y):
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

    def GenerateMap(self):
        Generate = True
        x = (self.mapsize//2)
        y = x
        currRoom = self.startRoom
        i = 0
        while i <= self.roomNum and Generate:
            self.map[y][x] = currRoom
            currRoom.x = x
            currRoom.y = y
            currRoom.lvl = self
            dirList = self.mapNoDirCheck(x,y)
            if dirList:
                direction = randItem(dirList)
                nextRoom = self.rollRooms()
                x = direction[1]
                y = direction[0]
                currRoom = nextRoom
                i += 1
            else:
                Generate = False
        self.createDispMap()

    def rollRooms(self):
        room = choices(self.rooms,weights=self.roomChances,k=1)[0]
        return room(self.Level)

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
            dirList.append(['north',self.map[y-1][x]])
        if y+1 < self.mapsize and self.map[y+1][x]:
            dirList.append(['south',self.map[y+1][x]])
        if x+1 < self.mapsize and self.map[y][x+1]:
            dirList.append(['east',self.map[y][x+1]])
        if x-1 >= 0 and self.map[y][x-1]:
            dirList.append(['west',self.map[y][x-1]])
        return dirList
    
    def createDispMap(self):
        self.dispMap = []
        for row in self.map:
            newrow = []
            for room in row:
                if room:
                    newrow.append(room.icon)
                else:
                    newrow.append(iconDict['Blank'])
            self.dispMap.append(newrow)
        
    # Prints the Developer Map
    def printMap(self,map):
        print('')
        for row in map:
            print(''.join(row))
        print('')
        print(f'Your Location: {iconDict["Player"]}')
        print(f'Treasure Room: {iconDict["Treasure Room"]}')
        print(f'Unknown Room: {iconDict["Unknown Room"]}')
        print(f'Start Room: {iconDict["Start Room"]}')
        print(f'Enemy Room: {iconDict["Enemy Room"]}')
        print(f'Stair Room: {iconDict["Stair Room"]}')

    # Prints the map shown to the players
    def printHiddenMap(self,player):
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
    def __init__(self,Level) -> None:
        self.x = 0
        self.y = 0
        self.Level = Level
        self.lvl = None
        self.cleared = False
        self.discovered = False

    # Default enter method always called when the player enters the room  (Unless overwritten)
    # This then runs subclass specific onEnter methods
    def enter(self,player):
        self.lvl.dispMap[self.y][self.x] = player.icon
        syst.printStatus()
        text(self.desc)
        if self.cleared:
            text('You have already cleared this room.')
            self.move(player)
        else:
            self.onEnter(player)

    # Allows the player to move between rooms
    def move(self,player):
        dirCheck = self.lvl.mapDirCheck(self.x,self.y)
        options = [direction[0] for direction in dirCheck]
        for Adjroom in [room[1] for room in dirCheck]:
            Adjroom.discovered = True 
        input()
        syst.printStatus()
        text(f'You can move {orChoice(options)}.')
        direction = Option(player=player,North='north' in options,South='south' in options,West='west' in options,East='east',Map=True)
        self.lvl.dispMap[self.y][self.x] = self.icon
        if direction in optionDict['north']:
            player.room = self.lvl.map[self.y-1][self.x]
            player.room.enter(player)
        if direction in optionDict['south']:
            player.room = self.lvl.map[self.y+1][self.x]
            player.room.enter(player)
        if direction in optionDict['west']:
            player.room = self.lvl.map[self.y][self.x-1]
            player.room.enter(player)
        if direction in optionDict['east']:
            player.room = self.lvl.map[self.y][self.x+1]
            player.room.enter(player)
        
    def clear(self):
        self.cleared = True
        text('You have cleared this room.')
    
class StartRoom(Room):
    def __init__(self, Level) -> None:
        super().__init__(Level)
        self.icon = iconDict['Start Room']

        if Level == 1:
            self.desc = 'You enter the dungeon...'
            self.reEnter = 'You enter the room that you started in.\nAre you sure your not lost?'
    
    def enter(self, player):
        self.lvl.dispMap[self.y][self.x] = player.icon
        syst.printStatus()
        if self.cleared:
            text(self.reEnter)
        else:
            self.cleared = True
            text(self.desc)
        self.move(player)

class Level1Exit(Room):
    def __init__(self, Level) -> None:
        super().__init__(Level)
        self.icon = iconDict['Stair Room']
        self.desc = 'You enter the dungeon...'
        self.reEnter = 'You enter the room that you started in.\nAre you sure your not lost?'
    
    def enter(self, player):
        self.lvl.dispMap[self.y][self.x] = player.icon
        syst.printStatus()
        if self.cleared:
            text(self.reEnter)
        else:
            self.cleared = True
            text(self.desc)
        self.move(player)


class EnemyRoom(Room):
    def __init__(self,Level) -> None:
        super().__init__(Level)
        self.desc = 'You enter a dimly lit room.' 
        self.icon = iconDict['Enemy Room']
        self.enemies = []
        if self.Level == 1:
            self.EnemyTypes = [Goblin,Spider]
        
        self.rollEnemy()

    def rollEnemy(self):
        enemyNum  = randint(1,3)
        for i in range(enemyNum):
            enemyType = randItem(self.EnemyTypes)
            InstantiatedEnemy = enemyType()
            self.enemies.append(InstantiatedEnemy)


    def onEnter(self,player):
        text('It is filled with enemies!')
        self.battling = True
        enemy = self.spawnEnemy()
        while self.battling:
            player.battle(enemy)
            if player.hp <= 0:
                self.battling = False
            elif enemy.hp <= 0:
                self.enemies.pop(0)
                text(f'There {AreIs(len(self.enemies))} {len(self.enemies)} {Plural(len(self.enemies),"enemy")} left.')
                enemy = self.spawnEnemy()
        if player.hp > 0:
            self.move(player)
    
    def spawnEnemy(self):
        if self.enemies:
            enemy = self.enemies[0]
            return enemy
        else:
            self.battling = False
            self.clear()
    
class TreasureRoom(Room):
    def __init__(self,Level):
        super().__init__(Level)

        # Visual Variables:
        self.desc = 'You enter a room with a large treasure chest inside.'
        self.icon = iconDict['Treasure Room']

        # Chances for each rarity tier
        self.commonCh = 37
        self.uncommonCh = 28
        self.rareCh = 19
        self.epicCh = 13
        self.legCh = 3

        # Mimic variables
        self.mimicChance = 0.15
        self.IsMimic = False
        self.Mimic = Mimic()

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
        answer = Option(Yes=True,No=True,Open=True)
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
            text(f'{col.red("Only to find rows upon rows of gnashing teeth.")}')
            player.battle(self.Mimic)
            if player.hp > 0:
                self.clear()
                self.move(player)
        else:
            text('You find an item lying in the bottom of the chest.')
            input()
            syst.printStatus()
            text(f'You have found a {self.treasure.rarname}!')
            self.treasure.showStats()
            print()
            player.currentWeaponStats()
            print()
            text(f'Would you like to equip the {self.treasure.rarname}?')
            answer = Option(Yes=True,No=True)
            if answer in optionDict['yes']:
                player.equip(self.treasure)
                self.clear()
                self.move(player)
            elif answer in optionDict['no']:
                text('You leave the item in the chest and move on.')
                self.clear()
                self.move(player)