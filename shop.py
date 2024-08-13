from items import common,uncommon,rare,epic,legendary,itemDict,UsableItem
from functions import randItem,text
from colours import col
from system import syst
from dictionaries import optionDict

class Shop():
    weaponList = [common,uncommon,rare,epic,legendary]
    def __init__(self,sellWeapons:bool,itemNumber,dialogue='',weaponPrices=[5,10,15,20,25],name='Store') -> None:
        self.weapons = []
        self.weaponNames = []
        self.weaponPrices = weaponPrices
        self.sellWeapons = sellWeapons
        self.name = name
        self.itemNumber = itemNumber
        self.dialogue = dialogue
        self.rerollPrice = 2
        self.rerollIncr = 1

    def rollWeapons(self):
        self.weapons = []
        self.weaponNames = []
        for rarity in self.weaponList:
            self.weapons.append(randItem(rarity))
        for weapon in self.weapons:
            self.weaponNames.append(weapon.rawname)

    def rollItems(self):
        allItems = list(itemDict)
        self.items = []
        for i in range(self.itemNumber):
            item = randItem(allItems)
            self.items.append(item)
            allItems.remove(item)

    def printItems(self):
        if self.dialogue:
            text(self.dialogue)
            syst.hint('Type the name of any item to purchase it and type "leave" to exit the store.')
            print()
        header = f'----- {self.name} -----'
        print(header)
        print()
        if self.sellWeapons:
            print('> Weapons <'.center(len(header)))
            for weaponnum,weapon in enumerate(self.weapons):
                print(f'{chr(8226)} {weapon.rarname}: {col.name("gold",f"{self.weaponPrices[weaponnum]} Gold")}')
            print()
        print('> Items <'.center(len(header)))
        for item in self.items:
            itemprice = itemDict[item]['price']
            print(f'{chr(8226)} {item.title()}: {col.name("gold",f"{itemprice} Gold")}')
        print()
        print(f'Reroll the shop: {col.name("gold",f"{self.rerollPrice} Gold")}')
        
    def rollAllItems(self):
        self.rollItems()
        if self.sellWeapons:
            self.rollWeapons()
        self.optionList = []
        self.priceList = []
        self.itemList = []
        if self.sellWeapons:
            self.optionList += self.weaponNames
            self.priceList += self.weaponPrices

        for item in self.items:
            self.optionList.append(item)
            self.itemList.append(item)
            self.priceList.append(itemDict[item]['price'])


    def enterShop(self,player):
        self.rollAllItems()
        buying = True
        while buying:
            syst.printStatus()
            self.printItems()
            choice = syst.Option(options=[self.optionList,optionDict['exit shop'],optionDict['reroll items']])
            if choice in self.optionList:
                index = self.optionList.index(choice)
                syst.printStatus()
                text(f"Do you want to buy the {self.optionList[index]} for {col.name('gold',f'{self.priceList[index]} gold')}?")
                if choice in self.weaponNames:
                    item = self.weapons[index]
                elif choice in self.itemList:
                    item = UsableItem(self.optionList[index], **itemDict[self.optionList[index]])
                item.showInfo()
                confirm = syst.Option(options=[optionDict['buy'],optionDict['yes'],optionDict['no']])
                if confirm in optionDict['yes'] or confirm in optionDict['buy']:
                    if player.buy(self.priceList[index]):
                        if item.__class__.__name__ == 'PlayerWeapon':
                            player.weapon = item
                            text(f'You have purchased and equipped the {self.weapons[index].name}!')
                            syst.enterHint(text='Press enter to return to the shop...')
                        elif item.__class__.__name__ == 'UsableItem':
                            player.items.append(item)
                            text(f'You have purchased the {item.name}!')
                            player.printItems()
                            syst.enterHint(text='Press enter to return to the shop...',space=False)
                    else:
                        text('You do not have enough gold to buy this.')
                        syst.enterHint(text='Press enter to return to the shop...')
                elif confirm in optionDict['no']:
                    text('You decide not to buy this.')
                    syst.enterHint(text='Press enter to return to the shop...')
            elif choice in optionDict['reroll items']:
                if player.buy(self.rerollPrice):
                    text('Rerolling items...')
                    self.rerollPrice += self.rerollIncr
                    self.rollAllItems()
                    syst.enterHint(text='Press enter to see the new items.')
                else:
                    text('You do not have enough gold to reroll the shop')
                    syst.enterHint()
            elif choice in optionDict['exit shop']:
                buying = False