__author__ = 'Zhiyu'

from MLL.Model.categoryCollection import *
from MLL.Utility.globalSettings import *

# foodtype:meat,vegetarian,seafood,unknown (string)
# microwave:yes,no (string)
# allergens:yes,no (string)
# price:low,med,high (string)
# time:early,mid,late (string)
# skutype:Anytime,Breakfast,Entree,Salad,Sandwich,Wrap

# USE LOWER CASE IN ALL OF THESE NAMES IN CATEGORY DEFINITION!!!

class categoryLoader:
    def __init__(self):
        self.categoryList = categoryCollection(None)

    def saveToFile(self,fname=_default_category_data_file_):
        pname = _project_entry_point_ + fname
        self.categoryList.writeToFile(pname)

    def loadFromFile(self,fname=_default_category_data_file_):
        pname = _project_entry_point_ + fname
        print "pname = "+_project_entry_point_
        self.categoryList.readFromFile(pname)


    def addCategoryToMeta(self,meta,category):
        name = category.name
        meta.setCategory(name,category)

    # creates a default category list, and write it to default location.
    # easy for debugging
    def createDefault(self):
        meta = metaCategory('foodtype',None)
        category_name = 'meat'
        cat = category(meta.metaName, category_name)
        cat.value = 4;
        self.addCategoryToMeta(meta,cat)
        category_name = 'vegetable'
        cat = category(meta.metaName, category_name)
        cat.value = 6;
        self.addCategoryToMeta(meta,cat)
        category_name = 'seafood'
        cat = category(meta.metaName, category_name)
        cat.value = 4;
        self.addCategoryToMeta(meta,cat)
        category_name = 'unknown'
        cat = category(meta.metaName, category_name)
        cat.value = 1;
        self.addCategoryToMeta(meta,cat)
        self.categoryList.setMeta(meta.metaName,meta)

        meta = metaCategory('microwave',None)
        category_name = 'yes'
        cat = category(meta.metaName, category_name)
        cat.value = 4;
        self.addCategoryToMeta(meta,cat)
        category_name = 'no'
        cat = category(meta.metaName, category_name)
        cat.value = 5;
        self.addCategoryToMeta(meta,cat)
        self.categoryList.setMeta(meta.metaName,meta)

        meta = metaCategory('allergens',None)
        category_name = 'yes'
        cat = category(meta.metaName, category_name)
        cat.value = 4;
        self.addCategoryToMeta(meta,cat)
        category_name = 'no'
        cat = category(meta.metaName, category_name)
        cat.value = 5;
        self.addCategoryToMeta(meta,cat)
        self.categoryList.setMeta(meta.metaName,meta)

        meta = metaCategory('price',None)
        category_name = 'low'
        cat = category(meta.metaName, category_name)
        cat.value = 10;
        self.addCategoryToMeta(meta,cat)
        category_name = 'med'
        cat = category(meta.metaName, category_name)
        cat.value = 7.5;
        self.addCategoryToMeta(meta,cat)
        category_name = 'high'
        cat = category(meta.metaName, category_name)
        cat.value = 3;
        self.addCategoryToMeta(meta,cat)
        self.categoryList.setMeta(meta.metaName,meta)

        meta = metaCategory('time',None)
        category_name = 'early'
        cat = category(meta.metaName, category_name)
        cat.value = 2;
        self.addCategoryToMeta(meta,cat)
        category_name = 'mid'
        cat = category(meta.metaName, category_name)
        cat.value = 5;
        self.addCategoryToMeta(meta,cat)
        category_name = 'late'
        cat = category(meta.metaName, category_name)
        cat.value = 3;
        self.addCategoryToMeta(meta,cat)
        self.categoryList.setMeta(meta.metaName,meta)

        meta = metaCategory('skutype',None)
        category_name = 'anytime'
        cat = category(meta.metaName, category_name)
        cat.value = 4.2;
        self.addCategoryToMeta(meta,cat)
        category_name = 'breakfast'
        cat = category(meta.metaName, category_name)
        cat.value = 5.7;
        self.addCategoryToMeta(meta,cat)
        category_name = 'entree'
        cat = category(meta.metaName, category_name)
        cat.value = 3.8;
        self.addCategoryToMeta(meta,cat)
        category_name = 'salad'
        cat = category(meta.metaName, category_name)
        cat.value = 4.5;
        self.addCategoryToMeta(meta,cat)
        category_name = 'sandwich'
        cat = category(meta.metaName, category_name)
        cat.value = 5.7;
        self.addCategoryToMeta(meta,cat)
        category_name = 'wrap'
        cat = category(meta.metaName, category_name)
        cat.value = 5.7;
        self.addCategoryToMeta(meta,cat)
        self.categoryList.setMeta(meta.metaName,meta)

        self.saveToFile()

if __name__ == '__main__':
    test = categoryLoader()
    test.createDefault()
