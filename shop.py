from items import common,uncommon,rare,epic,legendary,itemDict,HealItem
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
        header = f'----- {self.name} -----'
        print(header)
        if self.sellWeapons:
            print('> Weapons <'.center(len(header)))
            for weaponnum,weapon in enumerate(self.weapons):
                print(f'{chr(8226)} {weapon.rarname}: {col.name("gold",f"{self.weaponPrices[weaponnum]} Gold")}')
            print()
        print('> Items <'.center(len(header)))
        for type in itemDict:
            for item in itemDict[type]:
                itemprice = itemDict[type][item]['price']
                print(f'{chr(8226)} {item.title()}: {col.name("gold",f"{itemprice} Gold")}')
            print()
        

    def enterShop(self,player):
        buying = True
        optionList = []
        priceList = []
        itemList = []
        if self.sellWeapons:
            optionList += self.weaponNames
            priceList += self.weaponPrices
        for type in itemDict:
            for item in itemDict[type]:
                optionList.append(item)
                itemList.append(item)
                priceList.append(itemDict[type][item]['price'])

        while buying:
            choice = syst.Option(Other=True,OtherList=optionList,Exit=True)
            if choice in optionList:
                index = optionList.index(choice)
                syst.printStatus()
                text(f"Are you sure you want to buy the {optionList[index]} for {col.name('gold',f'{priceList[index]} gold')}?")
                if choice in self.weaponNames:
                    item = self.weapons[index]
                elif choice in itemList:
                    if choice in itemDict['heal']:
                        item = HealItem(optionList[index], **itemDict['heal'][optionList[index]])
                item.showInfo()
                confirm = syst.Option(Yes=True,No=True,OtherList=optionDict['buy'])
                if confirm in optionDict['yes'] or confirm in optionDict['buy']:
                    if player.buy(priceList[index]):
                        if item.__class__.__name__ == 'PlayerWeapon':
                            player.weapon = item
                            syst.printStatus()
                            text(f'You have purchased and equipped the {self.weapons[index].name}!')
                            syst.enterHint(text='Press enter to return to the shop...')
                            syst.printStatus()
                            self.printItems()
                        elif item.__class__.__base__.__name__ == 'UsableItem':
                            player.items.append(item)
                            syst.printStatus()
                            text(f'You have purchased the {item.name}!')
                            player.printItems()
                            syst.enterHint(text='Press enter to return to the shop...',space=False)
                            syst.printStatus()
                            self.printItems()
                    else:
                        text('You do not have enough funds to buy this.')
                        syst.enterHint(text='Press enter to return to the shop...')
                        syst.printStatus()
                        self.printItems()
                elif confirm in optionDict['no']:
                    text('You decide not to buy this.')
                    syst.enterHint(text='Press enter to return to the shop...')
                    syst.printStatus()
                    self.printItems()

            elif choice in optionDict['exit shop']:
                buying = False