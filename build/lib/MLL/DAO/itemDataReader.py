__author__ = 'Zhiyu'
from MLL.Model.itemData import *
from MLL.Model.categoryCollection import *
from MLL.DAO.categoryLoader import *
from preprocess.components.retrieve_dicts import *
from MLL.Utility.globalSettings import *

import os

type = ['SKU']

class itemDataReader:
    def __init__(self,categoryCollection=None):
        self.allItems = itemData()
        if categoryCollection is None:
            loader = categoryLoader()
            loader.loadFromFile()
            self.categoryCollection = loader.categoryList
        self.initialize()


    #remove all entries
    def initialize(self):
        self.allItems = itemData()

    def loadFromFile(self,filename,type):
        self.initialize()
        if type == "SKU":
            dict = parse_sku(filename)
            self.loadSKU(dict)
            return True
        else:
            return False



    def loadSKU(self,arr):
        for entry in arr:
            tempItem = self.generateSingleItemFromSKU(entry)
            self.allItems.addItem(tempItem)

    def generateSingleItemFromSKU(self,dict):
        theitem = item()
        for key in dict:
            keyunified = key.lower()
            value = dict[key]
            # special check
            if value == "entr\xe9e":
                value = "entree"
            if keyunified == "skuid":
                theitem.itemID = int(value)
            elif keyunified == "name":
                theitem.itemName = value
            else:
                meta = key
                cat = value
                theitem.category.append(self.categoryCollection.getCategoryInMeta(meta,cat))
        return theitem


if __name__ == '__main__':
    ir = itemDataReader()
    ir.loadFromFile(_project_entry_point_ + "/../preprocess/output/SKU_Master/SKU Master.csv","SKU")
    print "Testing: Entry imported = "+str(ir.allItems.itemList.__len__())
