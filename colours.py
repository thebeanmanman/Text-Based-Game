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
    
    # Rarity Colours
    @staticmethod
    def common(text):
        return f"\033[38;2;{5};{5};{5}m{text}\033[0m"
    
    @staticmethod
    def uncommon(text):
        return f"\033[38;2;{0};{185};{0}m{text}\033[0m"
    
    @staticmethod
    def rare(text):
        return f"\033[38;2;{0};{0};{255}m{text}\033[0m"
    
    @staticmethod
    def epic(text):
        return f"\033[38;2;{150};{0};{255}m{text}\033[0m"
    
    @staticmethod
    def leg(text):
        return f"\033[38;2;{239};{204};{0}m{text}\033[0m"    

col = Colour() #? Change this to a class instead