from random import choices,randint

# Import Enemies
from entity import Goblin,Mimic,Spider

# Import Functions
from functions import text,randItem,Option,wipe,chance

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

        self.GenerateMap()

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
            dirList.append('north')
        if y+1 < self.mapsize and self.map[y+1][x]:
            dirList.append('south')
        if x-1 >= 0 and self.map[y][x-1]:
            dirList.append('west')
        if x+1 < self.mapsize and self.map[y][x+1]:
            dirList.append('east')
        return dirList
    
    def createDispMap(self):
        self.dispMap = []
        for row in self.map:
            newrow = []
            for room in row:
                if room:
                    newrow.append(room.icon)
                else:
                    newrow.append(' . ')
            self.dispMap.append(newrow)
        
    def printMap(self):
        print('')
        for row in self.dispMap:
            print(''.join(row))
        print('')
        print(f'Your Location: {iconDict["Player"]}')
        print(f'Treasure Room: {iconDict["Treasure Room"]}')
        print(f'Start Room: {iconDict["Start Room"]}')
        print(f'Enemy Room: {iconDict["Enemy Room"]}')

class Room():
    def __init__(self,Level) -> None:
        self.x = 0
        self.y = 0
        self.Level = Level
        self.lvl = None
        self.cleared = False

    #When the player enters the room
    def enter(self,player):
        wipe()
        self.lvl.dispMap[self.y][self.x] = player.icon
        text(self.desc)
        self.move(player)

    def move(self,player):
        options = self.lvl.mapDirCheck(self.x,self.y)
        text(f'You can move {orChoice(options)}')
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
        self.cleared = True

        if Level == 1:
            self.desc = 'You enter the dungeon...'


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


    def enter(self,player):
        wipe()
        self.lvl.dispMap[self.y][self.x] = player.icon
        text(self.desc)
        if self.cleared:
            text('You have already cleared this room.')
        else:
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
            text(f'You have encountered {enemy.name}!')
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
        self.mimicChance = 0.1
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

    def enter(self,player):
        wipe()
        self.lvl.dispMap[self.y][self.x] = player.icon
        text(self.desc)
        if self.cleared:
            text('You have already cleared this room.')
            self.move(player)
        else:
            text('Open the chest?')
            answer = Option(Yes=True,No=True)
            if answer in optionDict['yes']:
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
            text(f'You have encountered a {col.red("Mimic!")}')
            player.battle(self.Mimic)
            if player.hp > 0:
                self.clear()
                self.move(player)
        else:
            text('You find an item lying in the bottom of the chest.')
            text(f'You have found a {self.treasure.rarname}!')
            self.treasure.showStats()
            text('Would you like to equip it?')
            answer = Option(Yes=True,No=True)
            if answer in optionDict['yes']:
                player.equip(self.treasure)
                self.clear()
                self.move(player)
            elif answer in optionDict['no']:
                text('You leave the item in the chest and move on.')
                self.clear()
                self.move(player)

# Start Rooms
# startRoom = StartRoom()

# # Enemy Rooms
# goblinRoom = EnemyRoom(desc='You enter a dark room...',enemies=[Goblin()])
# goblinRoom1 = EnemyRoom(desc='You enter a dim room...',enemies=[Goblin(),Goblin()])
# goblinRoom2 = EnemyRoom(desc='You enter a small room...',enemies=[Goblin()])
# goblinRoom3 = EnemyRoom(desc='You enter a room...',enemies=[Goblin(),Goblin()])
# goblinRoom4 = EnemyRoom(desc='You enter a gloomy room...',enemies=[Goblin()])

# # Treasure Rooms
# treasureRoom = TreasureRoom(desc='You enter a room with a large treasure chest inside.')
# treasureRoom2 = TreasureRoom(desc='dnja')

Level1 = Dungeon(rooms=[TreasureRoom,EnemyRoom],roomNum=7,reqRooms=None,mapsize=9,Level=1,roomChances=[5,20])