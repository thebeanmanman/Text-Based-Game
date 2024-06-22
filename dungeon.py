# Import Modules
from random import randint
import os

# Import Enemies
from entity import Goblin

# Import Functions
from functions import text,randItem,option


class Dungeon():
    def __init__(self,reqRooms:list,rooms:list,roomNum:int,startRoom) -> None:
        self.reqRooms = reqRooms
        self.rooms = rooms
        self.roomNum = roomNum
        self.startRoom = startRoom

        self.Generate()
    
    def Generate(self):
        i = 0
        currRoom = self.startRoom
        while i <= self.roomNum and self.rooms:
            dirList = currRoom.nodirCheck()
            direction = randItem(dirList)
            nextRoom = randItem(self.rooms)
            print(f'Current: {currRoom}. Next: {nextRoom}, Direction: {direction}')
            currRoom.createBranch(direction,nextRoom)
            i += 1
            if currRoom in self.rooms:
                self.rooms.remove(currRoom)
            currRoom = nextRoom


class Room():
    def __init__(self,desc:str) -> None:
        self.desc = desc
        self.north = None
        self.south = None
        self.west = None
        self.east = None
        self.cleared = False

    #When the player enters the room
    def enter(self,player):
        os.system('cls')
        text(self.desc)
        self.move(player)

    def move(self,player):
        options = self.dirCheck()
        text(f'You can move {", ".join(options)}')
        direction = option(options)
        if direction == 'north':
            player.room = self.north
            player.room.enter(player)
        if direction == 'south':
            player.room = self.south
            player.room.enter(player)
        if direction == 'west':
            player.room = self.west
            player.room.enter(player)
        if direction == 'east':
            player.room = self.east
            player.room.enter(player)

    #Creates a branch f
    def createBranch(self,dir,room):
        if dir == 'north':
            self.north = room
            room.south = self
        elif dir == 'south':
            self.south = room
            room.north = self
        elif dir == 'west':
            self.west = room
            room.east = self
        elif dir == 'east':
            self.east = room
            room.west = self
        else:
            print('No direction stated for room gen')
    
    #Returns a list of directions that don't already have a room
    def nodirCheck(self):
        dirList = []
        if not self.north:
            dirList.append('north')
        if not self.south:
            dirList.append('south')
        if not self.west:
            dirList.append('west')
        if not self.east:
            dirList.append('east')
        return dirList
    
    #Returns a list of directions that do already have a room
    def dirCheck(self):
        dirList = []
        if self.north:
            dirList.append('north')
        if self.south:
            dirList.append('south')
        if self.west:
            dirList.append('west')
        if self.east:
            dirList.append('east')
        return dirList
    
    def clear(self):
        self.cleared = True
        text('You have cleared this room.')
    

class EnemyRoom(Room):
    def __init__(self, desc: str,enemies:list,) -> None:
        super().__init__(desc)
        self.enemies = enemies

    def enter(self,player):
        os.system('cls')
        if self.cleared:
            text('You have already cleared this room.')
        text(self.desc)
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

startRoom = Room(desc='You enter the dungeon...')

goblinRoom = EnemyRoom(desc='You enter a dark room...',enemies=[Goblin()])
goblinRoom1 = EnemyRoom(desc='You enter a dim room...',enemies=[Goblin(),Goblin()])
goblinRoom2 = EnemyRoom(desc='You enter a dank room...',enemies=[Goblin()])
goblinRoom3 = EnemyRoom(desc='You enter a smelly room...',enemies=[Goblin(),Goblin()])
goblinRoom4 = EnemyRoom(desc='You enter a horrid room...',enemies=[Goblin()])

Level1 = Dungeon(rooms=[goblinRoom,goblinRoom1,goblinRoom2,goblinRoom3,goblinRoom4,],roomNum=5,startRoom=startRoom,reqRooms=None)