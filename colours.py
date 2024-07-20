class Colour():
    def __init__(self) -> None:
        self.commont = self.common('[Common]')
        self.uncommont = self.uncommon('[Uncommon]')
        self.raret = self.rare('[Rare]')
        self.epict = self.epic('[Epic]')
        self.legt = self.leg('[Legendary]')

    @staticmethod
    def rgb(r, g, b, text):
        return f"\033[38;2;{r};{g};{b}m{text}\033[0m"
    
    # Regular Colours
    @staticmethod
    def red(text):
        return f"\033[38;2;{255};{0};{0}m{text}\033[0m"
    
    @staticmethod
    def lightred(text):
        return f"\033[38;2;{250};{95};{85}m{text}\033[0m"
    
    @staticmethod
    def gold(text):
        return f"\033[38;2;{255};{255};{0}m{text}\033[0m"    

    @staticmethod # Narrator Text
    def nar(text):
        return f"\033[38;2;{0};{191};{255}m{text}\033[0m"
    
    @staticmethod # NPC Text
    def npc(text):
        return f"\033[38;2;{210};{180};{140}m{text}\033[0m"
    
    @staticmethod # Hint Text
    def hint(text):
        return f"\033[38;2;{255};{255};{255}m{text}\033[0m"
    
    ### Status Effect Colours
    @staticmethod
    def poison(text):
        return f"\033[38;2;{0};{128};{0}m{text}\033[0m"
    
    @staticmethod
    def heal(text):
        return f"\033[38;2;{60};{245};{113}m{text}\033[0m"
    # Rarity Colours
    @staticmethod
    def common(text):
        return f"\033[38;2;{128};{128};{128}m{text}\033[0m"
    
    @staticmethod
    def uncommon(text):
        return f"\033[38;2;{50};{185};{50}m{text}\033[0m"
    
    @staticmethod
    def rare(text):
        return f"\033[38;2;{30};{144};{255}m{text}\033[0m"
    
    @staticmethod
    def epic(text):
        return f"\033[38;2;{148};{0};{211}m{text}\033[0m"
    
    @staticmethod
    def leg(text):
        return f"\033[38;2;{239};{204};{0}m{text}\033[0m"    

col = Colour() #? Change this to a class instead