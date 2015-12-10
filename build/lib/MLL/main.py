__author__ = 'Zhiyu'

from MLL.Algorithm.abstractAlgorithm import *
from MLL.Algorithm.evolutionAlgorithmGroupItem import *
from MLL.Algorithm.evolutionAlgorithm import *
import MLL.Utility.globalSettings as gs
from MLL.DAO.dataLoader import *
from MLL.Algorithm.objectiveFunction import *
import os,sys

if __name__ == '__main__':

    # set entry point for other packages.
    # other packages use this to determine file locations.
    # gs._project_entry_point_ = os.getcwd()
    # print 'Entry point has been set to '+gs._project_entry_point_

    # initialize data loader
    dr = dataLoader()
    dr.initialize()

    # load some data. Will change to batch work later
    dr.loadSalesData(gs._project_entry_point_ + "/../preprocess/output/Monthly_Sold_Waste/10 October_Week 3.csv","October Week 3","efficiency")
    dr.loadSalesData(gs._project_entry_point_ + "/../preprocess/output/Monthly_Sold_Waste/10 October_Week 4.csv","October Week 4","efficiency")

    # create your algorithm prototype here
    for i in range(1):
        sys.stdout.write(str(i)+' ')
        evolutionAlgorithmController = evolutionAlgorithmGroupItem()
        #evolutionAlgorithmController = evolutionAlgorithm()
    # get data from data loader
        evolutionAlgorithmController.getData(dr)
        resultForEvolutionAlgorithm = evolutionAlgorithmController.generateRecommendation()


    # calculate the objective function value
    objectiveFunctionObj = objectiveFunction()
    objectiveFunctionObj.recommendation = resultForEvolutionAlgorithm
    score = objectiveFunctionObj.assess()

    print "Final result:"

    for item in resultForEvolutionAlgorithm.itemList:
        print str(item.itemName)+"x"+str(resultForEvolutionAlgorithm.itemList[item])

    # do comparison and output the best (when we have more than 1)
    print "Test: score = "+str(score)
    print('Under Construction')

