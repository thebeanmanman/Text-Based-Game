from entity import Enemy
from functions import text


class Dungeon():
    def __init__(self,reqRooms:list,rooms:list,roomNum:int,startRoom) -> None:
        self.reqRooms = reqRooms
        self.rooms = rooms
        self.roomNum = roomNum
        self.startRoom = startRoom

        self.Generate()
    
    def Generate(self):
        self.startRoom.createBranch('up',self.rooms[0])
        print(self.startRoom.up)


class Room():
    def __init__(self,desc:str) -> None:
        self.desc = desc
        self.up = None
        self.down = None
        self.left = None
        self.right = None

    def enter(self):
        text(self.desc)

    def createBranch(self,dir,room):
        if dir == 'up':
            self.up = room
            room.down = self
        if dir == 'down':
            self.down = room
            room.up = self
        if dir == 'left':
            self.left = room
            room.right = self
        if dir == 'right':
            self.right = room
            room.left = self

class EnemyRoom(Room):
    def __init__(self, desc: str,enemies:list,) -> None:
        super().__init__(desc)
        self.enemies = enemies
    def enter(self):
        text(self.desc)

startRoom = Room(desc='You enter the dungeon...')

goblinRoom = EnemyRoom(desc='You enter a dark room...',enemies=[Goblin])

Level1 = Dungeon(rooms=[goblinRoom],roomNum=2,startRoom=startRoom,reqRooms=None)