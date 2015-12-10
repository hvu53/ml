# Reads the processed data from files into lists of dictionaries
# Each dictionary represents a row in the file
# Author: Kevin Xu (klx@andrew.cmu.edu)

# Output dictionary entries:
# SKUid: int
# Name: string
# SKUtype: string
# Foodtype: string
# Price: string
# Allergens: string
# Microwave: string
def parse_sku(fname):
    output = []
    with open(fname) as f:
        for line in f.readlines():
            toks = line.strip().split(',');
            d = {}
            d['SKUid'] = int(toks[0])
            d['Name'] = toks[1]
            d['SKUtype'] = toks[2]
            d['Foodtype'] = toks[3]
            d['Price'] = toks[4]
            d['Allergens'] = toks[5]
            d['Microwave'] = toks[6]
            output.append(d)
    return output

# Output dictionary entries:
# Name: string
# UID: int
# QSold: int
# Time: string
def parse_sales(fname):
    output = []
    with open(fname) as f:
        for line in f.readlines():
            toks = line.strip().split(',');
            d = {}
            d['Name'] = toks[0]
            d['UID'] = int(toks[1])
            d['QSold'] = int(toks[2])
            d['Time'] = toks[3]
            output.append(d)
    return output

# Output dictionary entries:
# SKUid: int
# QSold: int
# QWaste: int
# QSoldPct: float
# QWastePct: float
def parse_efficiency(fname):
    output = []
    with open(fname) as f:
        for line in f.readlines():
            toks = line.strip().split(',');
            d = {}
            d['SKUid'] = int(toks[0])
            d['QSold'] = int(toks[1])
            d['QWaste'] = int(toks[2])
            d['QSoldPct'] = float(toks[3])
            d['QWastePct'] = float(toks[4])
            output.append(d)
    return output

# Output dictionary entries (can also be found in attributes.txt):
# food_type:vegan,carnivore,vegetarian,(mix of others)
# allergies:yes,no (string)
# breakfast_freq:never,sometimes,always (string)
# lunch_freq:never,sometimes,always (string)
# dinner_freq:never,sometimes,always (string)
# variety_happiness:yes,no (string)
# quantity_happiness:under,fine,over (string)
# pay_price: (int)
# buy_if_added_options:yes,no,indifferent (string)
# sandwich_freq:never,sometimes,always (string)
# salad_freq:never,sometimes,always (string)
# soup_freq:never,sometimes,always (string)
# rice_freq:never,sometimes,always (string)
# noodle_freq:never,sometimes,always (string)
# pasta_freq:never,sometimes,always (string)
# desert_freq:never,sometimes,always (string)
def parse_survey(fname):
    output = []
    with open(fname) as f:
        for line in f.readlines():
            toks = line.strip().split(',');
            d = {}
            d['food_type'] = toks[0]
            d['allergies'] = toks[1]
            d['breakfast_freq'] = toks[2]
            d['lunch_freq'] = toks[3]
            d['dinner_freq'] = toks[4]
            d['variety_happiness'] = toks[5]
            d['quantity_happiness'] = toks[6]
            try:
                d['pay_price'] = int(toks[7])
            except:
                d['pay_price'] = ''
            d['buy_if_added_options'] = toks[8]
            d['sandwich_freq'] = toks[9]
            d['salad_freq'] = toks[10]
            d['soup_freq'] = toks[11]
            d['rice_freq'] = toks[12]
            d['noodle_freq'] = toks[13]
            d['pasta_freq'] = toks[14]
            d['desert_freq'] = toks[15]
            output.append(d)
    return output

def test_all():
    print parse_efficiency('../output/Monthly_Sold_Waste/10 October_Week 4.csv')
    print parse_sku('../output/SKU_Master/SKU Master.csv')
    print parse_sales('../output/Weekly_Sales_Records/CMU 9.1-9.9.csv')
    print parse_survey('../output/survey/ML for Lunch Survey.csv')

#test_all()
