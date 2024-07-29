from weapons import common,uncommon,rare,epic,legendary
from functions import randItem,text
from colours import col
from system import syst
from dictionaries import optionDict

class Shop():
    weaponList = [common,uncommon,rare,epic,legendary]
    def __init__(self,sellWeapons:bool,weaponPrices=[5,10,15,20,25],name='Store') -> None:
        self.weapons = []
        self.weaponNames = []
        self.weaponPrices = weaponPrices
        self.sellWeapons = sellWeapons
        self.name = name
        if sellWeapons:
            self.rollWeapons()

    def rollWeapons(self):
        for rarity in self.weaponList:
            self.weapons.append(randItem(rarity))
        for weapon in self.weapons:
            self.weaponNames.append(weapon.rawname)

    def printItems(self):
        print(f'----- {self.name} -----')
        if self.sellWeapons:
            print('> Weapons <')
            for weaponnum,weapon in enumerate(self.weapons):
                print(f'{chr(8226)} {weapon.rarname}: {col.name("gold",f"{self.weaponPrices[weaponnum]} Gold")}')
            print()

    def enterShop(self,player):
        buying = True
        optionList = []
        if self.sellWeapons:
            optionList += self.weaponNames

        while buying:
            choice = syst.Option(Other=True,OtherList=optionList,Exit=True)
            if choice in self.weaponNames:
                index = self.weaponNames.index(choice)
                text(f"Are you sure you want to buy a {self.weapons[index].name} for {col.name('gold',f'{self.weaponPrices[index]} gold')}?")
                self.weapons[index].showStats()
                confirm = syst.Option(Yes=True,No=True,OtherList=optionDict['buy'])
                if confirm in optionDict['yes'] or confirm in optionDict['buy']:
                    if player.buy(self.weaponPrices[index]):
                        player.weapon = self.weapons[index]
                        syst.printStatus()
                        text(f'You have purchased and equipped a {self.weapons[index].name}!')
                        syst.enterHint(text='Press enter to return to the shop...')
                        syst.printStatus()
                        self.printItems()
                    else:
                        text('You do not have enough funds to buy this.')
                elif confirm in optionDict['no']:
                    text('You decide not to buy this.')

            elif choice in optionDict['exit']:
                buying = False