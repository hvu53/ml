__author__ = 'Jin Xi & Jialiang Tan'

import MLL.Model.recommendation
import MLL.Model.itemData

# type:meat,vegetarian,seafood,unknown (string)
# microwave:yes,no (string)
# allergens:yes,no (string)
# price:low,med,high (string)
# time:early,mid,late (string)
# skutype:Anytime,Breakfast,Entree,Salad,Sandwich,Wrap

# global metacategories
metaCategory = ['foodtype','microwave','allergens','price','time','skutype']

# global weight assignment for metacategories
weightCategory = {'foodtype':3.0,'microwave':2.0,'allergens':1.0,'price':3.0,'time':1.0,'skutype':2.0}

# global metacategory : [category] map
categoryMap = {'foodtype':['meat','vegetable','seafood','unknown'],
               'microwave':['yes','no'],
              'allergens':['yes','no'],
               'price':['low','med','high'],
               'time':['early','mid','late'],
               'skutype':['anytime','breakfast','entree','salad','sandwich','wrap']}

# represents importance of the category distribution
coefficientMetacategory = {'foodtype':1.0,'microwave':0.5,'allergens':0.5,'price':1.0,'time':0.5,'skutype':0.5}

# This is the expected fridge size.
expectedFridgeSize = 50

# This is the expected item varieties.
# Based on survey, we tried to setup a higher value compared to current pantry setup.
expectedItemVarieties = 12


class objectiveFunction:
    def __init__(self):
        self.recommendation = None

    def assess(self):
        return self.assess_main()
        # return self.assess_simple()

    # this function takes in a recommendation list and calculates the overall
    # objective score
    def assess_main(self):
        score = 0
        for item in self.recommendation.itemList:
            # print "Now score = " + str(score)
            score += 1.0 * self.get_score_of_item(item) * self.recommendation.itemList[item] / self.get_total_amount()
        # print "Coefficient = "+str(self.get_relation_coefficient())


        score = self.adjusted_score(score)
        #print "Before:"+str(score)
        score = score * self.get_relation_coefficient() * self.item_variety_adjustment()
        #print "After:"+str(score)
        return score

    def adjusted_score(self,orig):
        result = 0.0
        if orig < 4.5:
            result = orig / 10
        else:
            result = orig - 4.05
        result = result **5
        return result

    def item_variety_adjustment(self):
        total = 0.0
        result = 0.0
        for item in self.recommendation.itemList:
            total = total + 1
        if total == 0:
            #print "Error: empty itemset!"
            return 0
        if total > expectedItemVarieties:
            result = (expectedItemVarieties / total)**5
        else:
            result = (total/expectedItemVarieties)
        totalAmount = self.get_total_amount()
        if totalAmount > expectedFridgeSize:
            result = result * (1.0*expectedFridgeSize / totalAmount)**3
        else:
            result = result * 1.0*totalAmount / expectedFridgeSize

        return result


    # temporarily using this for testing purpose
    # def assess_simple(self):
    #     score = 0
    #     for item in self.recommendation.itemList:
    #         score += 1.0 * self.get_score_of_item(item) * self.recommendation.itemList[item] / self.get_total_amount()
    #     return score

    # this function calculates the total quantity of the items in the recommendation
    def get_total_amount(self):
        total = 0
        for item in self.recommendation.itemList:
            total = total + self.recommendation.itemList[item]
        return total

    # this function takes into an item and output this single item's objective
    # score
    def get_score_of_item(self, item):
        totalWeight = 0
        sum = 0
        for category in item.category:
            totalWeight += weightCategory[category.metaCategory]
            # different category has different weight
            sum = sum + weightCategory[category.metaCategory] * self.get_score_of_category(category)
        return sum/totalWeight

    # this function takes into a category and output this single category's
    # objective score
    # it is assumed that the value variable in category is a predefined score for this
    # category that is ready to use
    def get_score_of_category(self, category):
        # value is from 0 - 10, high value means positive feedback.
        # likelihood is from 0 - 1, high value means data is reliable.
        return category.value * category.likelihood

    # relation coefficient represents a coefficient score reflecting the degree of quantity distribution
    # in each metacategory.
    def get_relation_coefficient(self):
        quantityMap = {}
        for metaCategoryName in categoryMap:
            quantityMap[metaCategoryName] = {}
            for categoryName in categoryMap[metaCategoryName]:
                quantityMap[metaCategoryName][categoryName] = 0

        for item in self.recommendation.itemList:
            for category in item.category:
                quantityMap[category.metaCategory][category.name] += self.recommendation.itemList[item]

        relationScore = 0
        for metaCategoryName in categoryMap:
            list = []
            for key in quantityMap[metaCategoryName]:
                list.append(quantityMap[metaCategoryName][key])
            # zero stuff for missed items
            totalTypeInCategory = len(categoryMap[metaCategoryName])
            zeros = totalTypeInCategory - len(list)
            for i in range(0, zeros):
                list.append(0)
            
            relationScore += coefficientMetacategory[metaCategoryName] / (self.get_variance_of_cateogry(list) + 0.005)
            #relationScore += coefficientMetacategory[metaCategoryName] / (self.get_variance_of_cateogry(list) + 0.005)
        return relationScore

    # get the self defined variance for a metacategory
    def get_variance_of_cateogry(self, quantity):
        sum = 0.0
        ave = 0.0
        for q in quantity:
            sum = sum + q
        if sum == 0:
            return 1
        ave = sum / len(quantity)
        normalizedAve = ave / sum

        normalizedVariance = 0
        for q in quantity:
            normalizedQ = q / sum
            normalizedVariance += (normalizedQ - normalizedAve) * (normalizedQ - normalizedAve)
        return normalizedVariance


