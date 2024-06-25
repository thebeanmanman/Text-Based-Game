class Colour():
    @staticmethod
    def rgb(r, g, b, text):
        return f"\033[38;2;{r};{g};{b}m{text}\033[0m"
    
    # Regular Colours
    @staticmethod
    def red(text):
        return f"\033[38;2;{255};{0};{0}m{text}\033[0m"    
    
    # Rarity Colours
    @staticmethod
    def common():
        return f"\033[38;2;{5};{5};{5}m{'[Common]'}\033[0m"
    
    @staticmethod
    def uncommon():
        return f"\033[38;2;{0};{185};{0}m{'[Uncommon]'}\033[0m"
    
    @staticmethod
    def rare():
        return f"\033[38;2;{0};{0};{255}m{'[Rare]'}\033[0m"
    
    @staticmethod
    def epic():
        return f"\033[38;2;{150};{0};{255}m{'[Epic]'}\033[0m"
    
    @staticmethod
    def leg():
        return f"\033[38;2;{239};{204};{0}m{'[Legendary]'}\033[0m"    

col = Colour() #? Change this to a class instead
print(col.common())