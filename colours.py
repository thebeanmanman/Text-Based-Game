class Colour():
    def __init__(self) -> None:
        self.colourDict = {
            # Regular Colours
            'red': (255,0,0),
            'lightred': (250,95,85),
            'gold': (255,255,0),
            'nar' : (0,191,255),
            'npc' : (210,180,140),
            'hint': (255,255,255),

            # Status Effects
            'poison' : (0,128,0),
            'heal' : (60,245,113),
            'defence' : (137,207,240),

            # Rarity Colours
            'common' : (128,128,128),
            'uncommon' : (50,185,50),
            'rare' : (30,144,255),
            'epic' : (148,0,211),
            'leg' : (239,204,0)
        }
        self.commont = self.name('common','[Common]')
        self.uncommont = self.name('uncommon','[Uncommon]')
        self.raret = self.name('rare','[Rare]')
        self.epict = self.name('epic','[Epic]')
        self.legt = self.name('leg','[Legendary]')

    @staticmethod
    def rgb(r, g, b, text):
        return f"\033[38;2;{r};{g};{b}m{text}\033[0m"
    
    def name(self,colour,text):
        rgb = self.colourDict[colour]
        return f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{text}\033[0m" 

col = Colour() #? Change this to a class instead