__author__ = 'Zhiyu'

from abstractAlgorithm import *
from MLL.DAO.dataLoader import *
from MLL.Algorithm.objectiveFunction import *
from MLL.Model.recommendation import *
import random

class individual:
    def __init__(self):
        self.itemList = [] # one item each
        self.objectiveFunctionValue = 0

    def getCopy(self):
        result = individual()
        for i in self.itemList:
            result.itemList.append(i)
        result.objectiveFunctionValue = self.objectiveFunctionValue
        return result

    def __str__(self):
        s = ""
        for i in self.itemList:
            assert isinstance(i, item)
            s += str(i.itemID)  + " "#+str(i.category)+"\n"
        return s


    def generateRecommendation(self):
        result = recommendation()
        for i in self.itemList:
            try:
                result.itemList[i] += 1
            except KeyError:
                result.itemList[i] = 1
        return result

    def getObjectiveFunctionValue(self):
        objF = objectiveFunction()
        objF.recommendation = self.generateRecommendation()
        self.objectiveFunctionValue = objF.assess()

class evolutionAlgorithm(abstractAlgorithm):

    def __init__(self):
        self.population = []
        self.result = recommendation()
        self.datasource = None
        self.itemsData = None
        self.salesData = None
        self.categoryData = None

        self.fridgeSize = 50
        self.populationsize = 100
        self.iteration = 200

        self.mutation_chance = 0.05
        self.crossover_chance = 0.5

        self.debugData = []
        
    def getData(self,dataloader):
        """

        :type dataloader: dataLoader
        """
        self.datasource = dataloader
        self.itemsData = self.datasource.itemData;
        self.salesData = self.datasource.salesData;
        self.categoryData = self.datasource.categoryData;


    #generate the best recommendation this algorithm thinks
    def generateRecommendation(self):
        random.seed()
        #print 'Evolutionary Algorithm: Starting'
        for i in range(self.populationsize):
            self.population.append(self.generateRandomInvididual());
        for i in range(self.iteration):
            #print "Iteration "+str(i)
            self.debugData.append(self.getBestIndividual().objectiveFunctionValue)
            #print "Best individual has fitness: "+str(self.getBestIndividual().objectiveFunctionValue)
            #print "It is:"+self.getBestIndividual().__str__()
            #if self.checkFinish(): break
            for ind in self.population:
                ind.getObjectiveFunctionValue()
            newpopulation = []
            totalOp = self.populationsize/2
            for j in range(totalOp):
                ind1 = self.rouletteIndividual()
                ind2 = self.rouletteIndividual()
                crossover_result = self.crossoverIndividual(ind1,ind2)
                newind1 = crossover_result[0]
                newind2 = crossover_result[1]
                mutate1 = self.mutateIndividual(newind1)
                mutate2 = self.mutateIndividual(newind2)
                newpopulation.append(mutate1)
                newpopulation.append(mutate2)
            self.population = newpopulation
        for ind in self.population:
            ind.getObjectiveFunctionValue()
        bestind = self.getBestIndividual()
        s = ''
        for i in self.debugData:
            s = s+str(int(i))+' '
        print s
        return bestind.generateRecommendation()

    def generateRandomInvididual(self):
        result = individual()
        for i in range(1,self.fridgeSize):
            result.itemList.append(self.getRandomItem())
        return result;

    def getRandomItem(self):
        itemIDList = self.itemsData.getIDList()
        itemID = random.choice(itemIDList);
        return self.itemsData.getItemByID(itemID)

    def mutateIndividual(self,individual):
        result = individual.getCopy()
        for i in result.itemList:
            if random.random() < self.mutation_chance:
                i = self.getRandomItem()
        return result

    def crossoverIndividual(self,individual1,individual2):
        result = []
        r1 = individual1.getCopy()
        r2 = individual2.getCopy()
        for index in range(len(r1.itemList)):
            if random.random() < self.crossover_chance:
                temp = r1.itemList[index]
                r1.itemList[index]=r2.itemList[index]
                r2.itemList[index]=temp
        result.append(r1)
        result.append(r2)
        return result

    def checkFinish(self):
        return 1

    def getBestIndividual(self):
        maxFitness = -1
        maxIndividual = None
        for ind in self.population:
            if ind.objectiveFunctionValue > maxFitness:
                maxFitness = ind.objectiveFunctionValue
                maxIndividual = ind
        return maxIndividual

    def rouletteIndividual(self):
        totalScore = 0
        for ind in self.population:
            totalScore += ind.objectiveFunctionValue
        roulettePointer = random.random() * totalScore
        for ind in self.population:
            roulettePointer -= ind.objectiveFunctionValue;
            if roulettePointer <= 0:
                return ind



