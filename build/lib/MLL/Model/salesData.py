__author__ = 'Zhiyu'

import itemData

# A single record of sale.
# Can be either a single entry or an aggregated weekly one.

class sales:
    def __init__(self):
        self.item = None
        self.time = None
        self.sold = 0
        self.wasted = 0

# Sales in a given time.
# For example, weekly sales data aggregated.
class salesData:
    def __init__(self):
        self.salesList = []
        self.containsDetailedEntry = False
        self.containsAggregatedEntry = False
        self.timePeriod = None

    def addSales(self,sales):
        if sales is not None:
            self.salesList.append(sales)

class salesDataCollection:
    # Possible types of sales data. Aggregated for weekly report.
    # Detailed for small data set like data.
    # Mixed for unknown data (reserved)
    TYPES = ["detailed","efficiency","mixed"]

    def __init__(self):
        self.allSales = {} # key is timePeriod, value is salesData

    def getInternalName(self,time,type):
        return time+'@'+type

    # No checks for whether salesData is salesData!
    def setSalesData(self,salesData,time,type):
        if type in self.TYPES:
            self.allSales[self.getInternalName(time,type)] = salesData
            return True
        else:
            return False

    # Use this function to get inner elements and change it.
    # Do not use setSalesData unless you have a new copy.
    def getSalesData(self,time,type):
        if type in self.TYPES:
            try:
                return self.allSales[self.getInternalName(time,type)]
            except KeyError:
                return None
        else:
            return None




