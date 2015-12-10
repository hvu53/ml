__author__ = 'Zhiyu'
from MLL.Model.itemData import *
from MLL.DAO.itemDataReader import *
from MLL.Model.salesData import *
from MLL.DAO.categoryLoader import *
from MLL.Model.categoryCollection import *
from preprocess.components.retrieve_dicts import *
from MLL.Utility.globalSettings import *

class salesDataReader:
    def __init__(self,categoryCollection=None,itemList=None):
        """

        :type itemList: itemData
        :type categoryCollection: categoryCollection
        """
        self.allItems = itemList
        self.allSales = None
        if categoryCollection is None:
            loader = categoryLoader()
            loader.loadFromFile()
            self.categoryCollection = loader.categoryList
        if itemList is None:
            print "No item list present!"
        self.initialize()


    #remove all entries
    def initialize(self):
        self.allSales = salesData()

    def loadFromFile(self,filename,type):
        self.initialize()
        if type == "efficiency":
            dict = parse_efficiency(filename)
            self.loadEfficiency(dict)
            return True
        else:
            return False



    def loadEfficiency(self,arr):
        for entry in arr:
            tempsales = self.generateSingleItemFromEfficiency(entry)
            self.allSales.addSales(tempsales)

    def generateSingleItemFromEfficiency(self,dict):
        thesales = sales()
        for key in dict:
            keyunified = key.lower()
            value = dict[key]
            if keyunified == "skuid":
                try:
                    thesales.item = self.allItems.getItemByID(int(value))
                except:
                    print "Efficiency Loader: No such item with SKU ID:"+str(value)+". Entry ignored."
                    return None
            elif keyunified == "qsold":
                thesales.sold = int(value)
            elif keyunified == "qwaste":
                thesales.wasted = int(value)
        return thesales