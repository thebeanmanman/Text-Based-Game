# Import Enemies
from entity import Goblin

# Import Functions
from functions import text,randItem,Option,wipe

# Import Dictionaries
from dictionaries import iconDict,moveDict

# Import Grammar
from grammar import orChoice

# Import Weapons
from weapons import common,uncommon,rare,epic,legendary

class Dungeon():
    def __init__(self,reqRooms:list,rooms:list,roomNum:int,startRoom,mapsize:int) -> None:
        self.reqRooms = reqRooms
        self.rooms = rooms
        self.roomNum = roomNum
        self.startRoom = startRoom

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
        while i <= self.roomNum and self.rooms and Generate:
            self.map[y][x] = currRoom
            currRoom.x = x
            currRoom.y = y
            currRoom.lvl = self
            dirList = self.mapDirCheck(x,y)
            if dirList:
                direction = randItem(dirList)
                nextRoom = randItem(self.rooms)
                i += 1
                x = direction[1]
                y = direction[0]
                if currRoom in self.rooms:
                    self.rooms.remove(currRoom)
                currRoom = nextRoom
            else:
                Generate = False
        self.createDispMap()

    def mapDirCheck(self,x,y,reverse=False):
        dirList = []
        if y-1 >= 0 and not self.map[y-1][x]:
            dirList.append([y-1,x,'north'])
        if y+1 < self.mapsize and not self.map[y+1][x]:
            dirList.append([y+1,x,'south'])
        if x-1 >= 0 and not self.map[y][x-1]:
            dirList.append([y,x-1,'west'])
        if x+1 < self.mapsize and not self.map[y][x+1]:
            dirList.append([y,x+1,'east'])

        if reverse: 
            reversedDir = list({'north','south','west','east'} - set([item[2] for item in dirList]))
            return reversedDir
        else:
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
    def __init__(self,desc:str,icon:str) -> None:
        self.desc = desc
        self.icon = icon
        self.x = 0
        self.y = 0
        self.lvl = None
        self.cleared = False

    #When the player enters the room
    def enter(self,player):
        wipe()
        self.lvl.dispMap[self.y][self.x] = player.icon
        text(self.desc)
        self.move(player)

    def move(self,player):
        options = self.lvl.mapDirCheck(self.x,self.y,reverse=True)
        text(f'You can move {orChoice(options)}')
        direction = Option(player=player,North='north' in options,South='south' in options,West='west' in options,East='east',Map=True)
        self.lvl.dispMap[self.y][self.x] = self.icon
        if direction in moveDict['north']:
            player.room = self.lvl.map[self.y-1][self.x]
            player.room.enter(player)
        if direction in moveDict['south']:
            player.room = self.lvl.map[self.y+1][self.x]
            player.room.enter(player)
        if direction in moveDict['west']:
            player.room = self.lvl.map[self.y][self.x-1]
            player.room.enter(player)
        if direction in moveDict['east']:
            player.room = self.lvl.map[self.y][self.x+1]
            player.room.enter(player)
        
    def clear(self):
        self.cleared = True
        text('You have cleared this room.')
    
class StartRoom(Room):
    def __init__(self, desc: str, icon=iconDict['Start Room']) -> None:
        super().__init__(desc, icon)
        self.cleared = True


class EnemyRoom(Room):
    def __init__(self, desc: str,enemies:list,icon=iconDict['Enemy Room']) -> None:
        super().__init__(desc,icon)
        self.enemies = enemies

    def enter(self,player):
        wipe()
        self.lvl.dispMap[self.y][self.x] = player.icon
        text(self.desc)
        if self.cleared:
            text('You have already cleared this room.')
        else:
            self.battling = True
            enemy = self.spawnEnemy()
            while self.battling:
                player.attack(enemy)
                enemy.attack(player)
                text(f'Your HP: {player.hp}')
                text(f'{enemy.name}s HP: {enemy.hp}')
                input()
                if player.hp <= 0:
                    self.battling = False
                    player.death()
                elif enemy.hp <= 0:
                    enemy.death(player)
                    self.enemies.pop(0)
                    enemy = self.spawnEnemy()
        self.move(player)
    
    def spawnEnemy(self):
        if self.enemies:
            enemy = self.enemies[0]
            text(f'You have encountered {enemy.name}!')
            input()
            return enemy
        else:
            self.battling = False
            self.clear()
    
class TreasureRoom(Room):
    def __init__(self, desc: str) -> None:
        super().__init__(desc)
        self.icon = iconDict['Treasure Room']
    
# Start Rooms
startRoom = StartRoom(desc='You enter the dungeon...')

# Enemy Rooms
goblinRoom = EnemyRoom(desc='You enter a dark room...',enemies=[Goblin()])
goblinRoom1 = EnemyRoom(desc='You enter a dim room...',enemies=[Goblin(),Goblin()])
goblinRoom2 = EnemyRoom(desc='You enter a small room...',enemies=[Goblin()])
goblinRoom3 = EnemyRoom(desc='You enter a room...',enemies=[Goblin(),Goblin()])
goblinRoom4 = EnemyRoom(desc='You enter a gloomy room...',enemies=[Goblin()])

# Treasure Room

Level1 = Dungeon(rooms=[goblinRoom,goblinRoom1,goblinRoom2,goblinRoom3,goblinRoom4,],roomNum=7,startRoom=startRoom,reqRooms=None,mapsize=9)