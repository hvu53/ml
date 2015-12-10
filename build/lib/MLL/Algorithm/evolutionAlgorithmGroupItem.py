__author__ = 'Zhiyu'

from abstractAlgorithm import *
from MLL.DAO.dataLoader import *
from MLL.Algorithm.objectiveFunction import *
from MLL.Model.recommendation import *
import random,math

class individual:
    def __init__(self):
        self.itemList = {} # key is item, value is amount
        self.objectiveFunctionValue = 0
        self.minimumGroupSize = 2

    def getCopy(self):
        result = individual()
        for i in self.itemList:
            result.itemList[i] = self.itemList[i]
        result.objectiveFunctionValue = self.objectiveFunctionValue
        return result

    def __str__(self):
        s = ""
        for i in self.itemList:
            assert isinstance(i, item)
            s += str(i.itemName)  + "x"+str(self.itemList[i])+" "
        return s

    def generateRecommendation(self):
        result = recommendation()
        for i in self.itemList:
            if self.itemList[i] > self.minimumGroupSize:
                result.itemList[i] = self.itemList[i]
        return result

    def getObjectiveFunctionValue(self):
        objF = objectiveFunction()
        objF.recommendation = self.generateRecommendation()
        self.objectiveFunctionValue = objF.assess()

class evolutionAlgorithmGroupItem(abstractAlgorithm):

    def __init__(self):
        self.population = []
        self.result = recommendation()
        self.datasource = None
        self.itemsData = None
        self.salesData = None
        self.categoryData = None

        self.fridgeSize = 15
        self.populationsize = 100
        self.iteration = 200

        self.mutation_chance = 0.1
        self.crossover_chance = 0.3

        self.maximumGroupSize = 10

        self.debugData = []

    def dynamicChance(self,iteration):
        self.mutation_chance = self.mutation_chance * 0.98
        if self.mutation_chance<0.03: self.mutation_chance = 0.03
        self.crossover_chance = self.crossover_chance * 0.98
        if self.crossover_chance<0.1: self.crossover_chance = 0.1

        
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
        for ind in self.population:
            ind.getObjectiveFunctionValue()
        bestind = None
        bestindScore = -1.0
        for i in range(self.iteration):
            self.dynamicChance(i)
            #if self.checkFinish(): break
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
            #print "Iteration "+str(i)
            bestindThisitr = self.getBestIndividual()
            bestScoreThisitr = bestindThisitr.objectiveFunctionValue
            self.debugData.append(self.getBestIndividual().objectiveFunctionValue)
            if bestScoreThisitr > bestindScore:
                bestind = bestindThisitr
                bestindScore = bestScoreThisitr
                #print "New record:"+str(bestScoreThisitr)
                #print "It is:"+str(bestind)
            #print "Best individual has fitness: "+str(self.getBestIndividual().objectiveFunctionValue)

            #print "It is:"+self.getBestIndividual().__str__()
        # s = ''
        # for i in self.debugData:
        #     s = s+str(int(i))+' '
        # print s
        return bestind.generateRecommendation()

    def generateRandomInvididual(self):
        result = individual()
        for i in range(1,self.fridgeSize):
            result.itemList[self.getRandomItem()] = random.randint(1,self.maximumGroupSize)
        result = self.keepIndividualAtFixedSize(result)
        return result

    # This function is to keep that all individuals are the same size
    def keepIndividualAtFixedSize(self,ind):
        """

        :type ind: individual
        """
        #print "INPUT SIZE:"+str(ind.itemList.__len__())
        result = ind.getCopy()
        for key in result.itemList.keys():
            if result.itemList[key] == 0:
                del result.itemList[key]
            elif result.itemList[key] > self.maximumGroupSize:
                result.itemList[key] = self.maximumGroupSize
        #print "RESULT SIZE:"+str(result.itemList.__len__())
        while len(result.itemList)<self.fridgeSize:
            theItem = self.getRandomItem()
            if theItem not in result.itemList:
                result.itemList[theItem] = 1
        #print "RESULT SIZE:"+str(result.itemList.__len__())
        return result        


    def getRandomItem(self):
        itemIDList = self.itemsData.getIDList()
        itemID = random.choice(itemIDList);
        return self.itemsData.getItemByID(itemID)

    #only have item count mutated
    def mutateIndividual(self,individual):
        result = individual.getCopy()
        for i in result.itemList.keys():
            if random.random() < self.mutation_chance:
                #result.itemList[i] = random.randint(1,self.maximumGroupSize)
                newitem = self.getRandomItem()
                if newitem in result.itemList:
                    # do amount mutation instead
                    result.itemList[i] = random.randint(1,self.maximumGroupSize)
                else:
                    del result.itemList[i]
                    result.itemList[newitem] = random.randint(1,self.maximumGroupSize)
        return result

    def crossoverIndividual(self,individual1,individual2):

        result = []
        r1 = individual1.getCopy()
        r2 = individual2.getCopy()
        allItems1 = []
        allItems2 = []
        for index in r1.itemList:
            allItems1.append(index)
        for index in r2.itemList:
            allItems2.append(index)
        for index in range(allItems1.__len__()):
            if random.random() < self.crossover_chance:
                try:
                    item1 = allItems1[index]
                    item2 = allItems2[index]
                except:
                    print "Out of index! index = "+str(allItems1.__len__())+" vs "+str(allItems2.__len__())

                if item1 in allItems2:
                    r2.itemList[item1] += r1.itemList[item1]
                    r1.itemList[item1] = 0
                else:
                    r2.itemList[item1] = r1.itemList[item1]
                    r1.itemList[item1] = 0
                if item2 in allItems1:
                    r1.itemList[item2] += r2.itemList[item2]
                    r2.itemList[item2] = 0
                else:
                    r1.itemList[item2] = r2.itemList[item2]
                    r2.itemList[item2] = 0
        # print "LENGTH:"+len(individual1.itemList).__str__()+" "+len(individual2.itemList).__str__()+"/"+len(r1.itemList).__str__()+" "+len(r2.itemList).__str__()+" "
        r1=self.keepIndividualAtFixedSize(r1)
        r2=self.keepIndividualAtFixedSize(r2)
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



