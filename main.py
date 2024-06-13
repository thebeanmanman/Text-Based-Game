from random import randint
from time import sleep
GOBBYLIST = ['Grizzletongue', 'Grumbletoad', 'Rumblebelly', 'Rumblestomp', 'Noggleblight', 'Goblintide', 'Glimmergob', 'Wretchwhisker', 'Fangsnarl', 'Snagglewort', 'Sludgegrip', 'Snickersnatch', 'Gloomclaw', 'Sliverfang', 'Wartnose', 'Muckspindle', 'Thistleknob', 'Moldfinger', 'Gnarltooth', 'Slimefoot', 'Grumblegrim', 'Snickergrin', 'Fizzlefingers', 'Bogbelch', 'Slurgtail', 'Sludgeclaw', 'Miregaze', 'Grumblegut', 'Wretchling', 'Nibblesnatch', 'Slithergrub', 'Snaggleclaw', 'Sludgefist', 'Slurpblight', 'Grizzleknob', 'Wartbelly', 'Sludgejaw', 'Nogglegrin', 'Moldywhisk', 'Rumblemuck', 'Fazefoot', 'Glimmerwart', 'Snaktongue', 'Gnarlbelly', 'Thistlefang', 'Wobblewart', 'Snikernose', 'Goblintooth', 'Nettlegrin', 'Gloomshadow', 'Sludgejaw', 'Snickerwart', 'Rumblefoot', 'Gobsmudge', 'Sludgebelle', 'Golintid', 'Nogglebelly', 'Mosswhisk', 'Grizzletooth', 'Wartnibble', 'Wretchfang', 'Slitherclaw', 'Grumbleclaw', 'Grumblethorn', 'Wobblethumb', 'Snaggletoad', 'Thistlenose', 'Sludgebelch', 'Fizzlefoot', 'Sliverclaw', 'Nibblesnarl', 'Glimmerbelly', 'Snagglenose', 'Slurpgrub', 'Slimegob', 'Wretchwhisk', 'Thistlejaw', 'Snickersnarl', 'Sludgepaw', 'Gobblefist', 'Grizzlegrin', 'Bogbelch', 'Slitherjaw', 'Slurpnose', 'Gnarlclaw', 'Wartbelly', 'Thistletide', 'Slurptongue', 'Moldywhisk', 'Gontongue', 'Glimmergrim', 'Snickergaze', 'Grumblefoot', 'Fizzlegob', 'Rumblenose', 'Grumblegaze'] 
def text(toprint):
    texttime = 0.03
    toprint = str(toprint)
    for char in toprint:
        print(char,flush=True,end='')
        if char == '.':
            sleep(texttime*20)
        else:
            sleep(texttime)
    print('\n',end='')
class Goblin():
    def __init__(self):
        self.pos = [randint(-3,3),randint(-3,3)]
        self.health = randint(1,3)
        self.damage = randint(1,2)
        self.name = GOBBYLIST[randint(0,len(GOBBYLIST))]
    def turn(self):
        if self.pos == Player.pos:
            self.battle()
    def battle(self):
        Player.health -= self.damage
        text(f'Hit! You take {self.damage} damage from {self.name} The Goblin')
class Player():
    pos = [0,0]
    health = 10
    def move(self,x,y):
        self.pos[0] += x
        self.pos[1] += y
    
class Item():
    def __init__(self,name,x,y):
        self.pos = [x,y]
        self.name = name


Player1 = Player()
Gobby = Goblin()
text(Gobby.pos)
Start = True
while Start:
    Start = False
Play = True
while Play:
    text(f"Pos: {Player1.pos}")
    Direction = input('Enter Direction: ')
    if Direction == 'w':
        Player1.move(0,1)
    elif Direction == 'a':
        Player1.move(-1,0)
    elif Direction == 's':
        Player1.move(0,-1)
    elif Direction == 'd':
        Player1.move(1,0)
    Gobby.turn(Player1)