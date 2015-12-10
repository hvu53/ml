from category import *
import re,string;

import jsonpickle as json

# a metaCategory is a combination of category having the same metacategory
# Example: price (high, mid, low) ; waste (100,50,0)

class metaCategory:
    def __init__(self, metaname=None, values=None):
        if metaname is None:
            metaname = 'undefined'
        self.metaName = metaname
        if values is None:
            values = {}
        self.values = values # category name as key, category itself as value

    def setCategory(self, name, value):
        if name is None:
            return
        if value is None:
            return
        self.values[name] = value

    def getCategory(self, name):
        if name is None:
            return None
        if name not in self.values:
            return None
        return self.values[name]

# A categoryCollection is a collection of metacategory.
# This class is served as a look-up table for categories.

class categoryCollection:
    def __init__(self,values = None):
        if values is None:
            values = {}  # metacategory name as key, metacategory itself as value
        self.values = values

    def getCleanString(self,str):
        pattern = re.compile('[\W_]+')
        return pattern.sub('', str)

    def setMeta(self,name,value):
        if name is None:
            return
        if value is None:
            return
        self.values[name] = value

    def getMeta(self,name):

        if (name is None) or (name not in self.values):
            return None
        return self.values[name]

    def getCategoryInMeta(self,_metaname,_categoryname):
        metaname = _metaname.lower()
        if "entr" in _categoryname.lower():
            _categoryname = "entree"
        categoryname = self.getCleanString(_categoryname.lower())

        if (metaname is None) or (categoryname is None):
            return None
        # if (metaname not in self.values) or (categoryname not in self.values[metaname]):
        #     return None
        try:
            return self.values[metaname].values[categoryname]
        except:
            print "get Category in meta failed finding "+metaname+" / "+categoryname
            return None


    def writeToFile(self,filename):
        open(filename,'wb').write(json.encode(self))

    def readFromFile(self,filename):
        temp = json.decode(open(filename,'rb').read())
        self.values = temp.values




