__author__ = 'Zhiyu'

from category import *


class item:
    def __init__(self):
        self.category = []
        self.itemName = ""
        self.itemID = -1


class itemData:
    def __init__(self):
        self.itemList = {}
        self.idToItem = {}

    def addItem(self,item):
        if item.itemName not in self.itemList:
            self.itemList[item.itemName] = item
            try:
                itemofid = self.idToItem[item.itemID]
                print "item has same id:"+str(item.itemID)
            except:
                pass
            self.idToItem[item.itemID] = item
        return self.itemList[item.itemName]

    def getItem(self,name):
        return self.itemList[name]

    def getItemByID(self,id):
        return self.idToItem[id]

    def removeItem(self,name):
        if self.itemList[name] is None:
            return
        id = self.itemList[name].itemID
        del self.idToItem[id]
        del self.itemList[name]

    def getIDList(self):
        return self.idToItem.keys()
