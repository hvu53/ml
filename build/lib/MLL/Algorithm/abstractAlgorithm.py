__author__ = 'Zhiyu'
from abc import ABCMeta, abstractmethod

class abstractAlgorithm:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self): pass

    @abstractmethod
    #generate the best recommendation this algorithm thinks
    def generateRecommendation(self): pass