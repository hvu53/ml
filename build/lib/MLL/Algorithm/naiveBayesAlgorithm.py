__author__ = 'Hoavu'

from abstractAlgorithm import *
from MLL.DAO.dataLoader import *
from MLL.Algorithm.objectiveFunction import *
from MLL.Model.recommendation import *
import random

class naiveBayesAlgorithm(abstractAlgorithm):

    def __init__(self):
        self.features_train = None
        self.features_test = None

    def getData(self,dataloader):
        """

        :type dataloader: dataLoader
        """
        self.datasource = dataloader
        self.itemsData = self.datasource.itemData;
        self.salesData = self.datasource.salesData;
        self.categoryData = self.datasource.categoryData;

    def getRandomItem(self):
        itemIDList = self.itemsData.getIDList()
        itemID = random.choice(itemIDList);
        return self.itemsData.getItemByID(itemID)

    def splitData(dataset, splitRatio):
      trainSize = int(len(dataset) * splitRatio)
      trainSet = []
      copy = list(dataset)
      while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
      return [trainSet, copy]


    def classify(features_train, labels_train):
      from sklearn.naive_bayes import GaussianNB
      clf = GaussianNB()
      clf = clf.fit(features_train, labels_train)
      return clf

    def prediction(clf,features_test):
      pred = clf.predict(features_test)
      return pred
    

    #generate the best recommendation this algorithm thinks
    def generateRecommendation(self):
      random.seed()
      print 'Naive Bayes Algorithm: Starting'
      return 'Not implemented'



print dataLoader
print 'items Data'