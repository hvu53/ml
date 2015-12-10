__author__ = 'Hoa Vu'

from abstractAlgorithm import *
from MLL.DAO.dataLoader import *
from MLL.Algorithm.objectiveFunction import *
from MLL.Model.recommendation import *
import math
import random

class Node:
    def __init__(self, prob, children):
        self.children = children
        self.prob = prob

class individual:
    def __init__(self):
        self.tree = self.initTree() # one item each
        self.objectiveFunctionValue = 0

    def buildTimeNode(self):
        return Node(prob=0, children = None)

    def buildPriceNode(self):
        root = Node(prob=0, children=[])
        for i in xrange(3):
            node = self.buildTimeNode()
            root.children.append(node)
        a = random.random()
        b = random.random()
        c = random.random()
        p1 = a / (a + b + c)
        p2 = b / (a + b + c)
        p3 = 1 - p1 - p2
        root.children[0].prob = p1
        root.children[1].prob = p2
        root.children[2].prob = p3
        return root

    def buildFoodTypeNode(self):
        root = Node(prob=0, children=[])
        for i in xrange(3):
            node = self.buildPriceNode()
            root.children.append(node)
        a = random.random()
        b = random.random()
        c = random.random()
        p1 = a / (a + b + c)
        p2 = b / (a + b + c)
        p3 = 1 - p1 - p2
        root.children[0].prob = p1
        root.children[1].prob = p2
        root.children[2].prob = p3
        return root

    def buildRoot(self):
        root = Node(prob=1, children=[])
        for i in xrange(3):
            node = self.buildFoodTypeNode()
            root.children.append(node)
        a = random.random()
        b = random.random()
        c = random.random()
        p1 = a / (a + b + c)
        p2 = b / (a + b + c)
        p3 = 1 - p1 - p2
        root.children[0].prob = p1
        root.children[1].prob = p2
        root.children[2].prob = p3
        return root

    def initTree(self):
        return buildRoot()    

    def getCopy(self):
        result = individual()
        for i in self.itemList:
            result.itemList.append(i)
        result.objectiveFunctionValue = self.objectiveFunctionValue
        return result

    def mapping(self):
        
        
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

class evolutionAlgorithm2(abstractAlgorithm):

    def __init__(self):
        self.population = []
        self.result = recommendation()
        self.datasource = None
        self.itemsData = None
        self.salesData = None
        self.categoryData = None

        self.fridgeSize = 30
        self.populationsize = 100
        self.iteration = 50

        self.mutation_chance = 0.05
        self.crossover_chance = 0.2

        
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
        print 'Evolutionary Algorithm2: Starting'
        for i in range(self.populationsize):
            self.population.append(self.generateRandomInvididual());
        for i in range(self.iteration):
            #print "Iteration "+str(i)
            #print "Best individual has fitness: "+str(self.getBestIndividual().objectiveFunctionValue)
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



