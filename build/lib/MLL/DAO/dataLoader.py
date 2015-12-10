__author__ = 'Zhiyu'

from MLL.DAO.itemDataReader import *
from MLL.DAO.salesDataReader import *
from MLL.Model import *
from MLL.Utility.globalSettings import *
from traceback import *

class dataLoader:
    def __init__(self):
        self.categoryData = None
        self.itemData = None
        self.salesData = salesDataCollection()

    def initialize(self,path=None):
        try:
            ir = itemDataReader()
            if path is None:
                path = _project_entry_point_ + "/../preprocess/output/SKU_Master/SKU Master.csv"
            ir.loadFromFile(path,"SKU")
            self.itemData = ir.allItems
            self.categoryData = ir.categoryCollection
        except:
            print "Data Loader: Failed to initialize."
            print_exc()
        # print "Testing: Item Entry imported = "+str(ir.allItems.itemList.__len__())

    def loadSalesData(self,path,time,type):
        if path is None:
            return False
        try:
            sr = salesDataReader(self.categoryData,self.itemData)
            # sr.loadFromFile(_project_entry_point_ + "/../preprocess/output/Monthly_Sold_Waste/10 October_Week 3.csv","efficiency")
            sr.loadFromFile(path,"efficiency")
            # print "Testing: Sales Entry imported = "+str(sr.allSales.salesList.__len__())
            self.salesData.setSalesData(sr.allSales,time,type)
        except:
            print "Sales Loader: Failed to load file at "+path+" ."
            print_exc()

# if __name__ == '__main__':
#     dr = dataLoader()
#     dr.initialize()
#     dr.loadSalesData(_project_entry_point_ + "/../preprocess/output/Monthly_Sold_Waste/10 October_Week 3.csv","October Week 3","efficiency")
#     dr.loadSalesData(_project_entry_point_ + "/../preprocess/output/Monthly_Sold_Waste/10 October_Week 4.csv","October Week 4","efficiency")


