__author__ = 'Zhiyu'

from MLL.Algorithm.abstractAlgorithm import *
from MLL.Algorithm.evolutionAlgorithmGroupItem import *
from MLL.Algorithm.evolutionAlgorithm import *
import MLL.Utility.globalSettings as gs
from MLL.DAO.dataLoader import *
from MLL.Algorithm.objectiveFunction import *
import os,sys

class APIHead:
    def __init__(self):
        self.dr = dataLoader()

    def loadData(self):

        # Load item data
        self.dr.initialize()

        # Load sales data
        self.dr.loadSalesData(gs._project_entry_point_ + "/../preprocess/output/Monthly_Sold_Waste/10 October_Week 3.csv","October Week 3","efficiency")
        self.dr.loadSalesData(gs._project_entry_point_ + "/../preprocess/output/Monthly_Sold_Waste/10 October_Week 4.csv","October Week 4","efficiency")

    def loadExtraSalesData(self,path):
        self.dr.loadSalesData(gs._project_entry_point_ + path,"efficiency")

    def callEvolutionaryAlgorithm(self):
        evolutionAlgorithmController = evolutionAlgorithmGroupItem()
        evolutionAlgorithmController.getData(self.dr)
        resultForEvolutionAlgorithm = evolutionAlgorithmController.generateRecommendation()
        return resultForEvolutionAlgorithm


if __name__ == '__main__':

    tester = APIHead()
    tester.loadData()
    resultForEvolutionAlgorithm = tester.callEvolutionaryAlgorithm()

    # calculate the objective function value
    objectiveFunctionObj = objectiveFunction()
    objectiveFunctionObj.recommendation = resultForEvolutionAlgorithm
    score = objectiveFunctionObj.assess()

    print "Final result:"

    for item in resultForEvolutionAlgorithm.itemList:
        print str(item.itemName)+"x"+str(resultForEvolutionAlgorithm.itemList[item])

    # do comparison and output the best (when we have more than 1)
    print "Test: score = "+str(score)

    print('API Test Done')