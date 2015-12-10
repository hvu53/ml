# (0) Retains the type provided by the SKU spreadsheet
# (1) Categorizes into Meat, Vegetarian or Seafood
# (2) Categorizes the price into low, med and high
# (3) Determines if microwaved
# (4) Determines if contains allergens
# Author: Kevin Xu (klx@andrew.cmu.edu)

# Thresholds for determining price category
high = 7.00 # $7.00+
med = 5.00 # $5.00-7.00

# Returns SKU,name,SKU type,meat type,price category,allergens,microwaved
def process_line(inp, meats, seafoods, vegetables):
    toks = inp.split(',')
    try:
        SKU = toks[1]
        SKU_type = toks[0]
        Name = toks[2]
        Price = float(toks[3].strip()[1:])
        Allerg = toks[len(toks)-2] # Beware commas separating ingred
        Micro = toks[len(toks)-1]
    except:
        return False
    SKU += ',' + Name + ',' + SKU_type + ','
    cat = False
    for word in inp.lower().replace(',', ' ').split(' '):
        if word in meats:
            SKU += 'meat'
            cat = True
            break
        elif word in seafoods:
            SKU += 'seafood'
            cat = True
            break
        elif word in vegetables:
            SKU += 'vegetable'
            cat = True
            break
    if not cat:
        SKU += 'unknown'
    SKU += ','
    if Price >= high:
        SKU += 'high'
    elif Price >= med:
        SKU += 'med'
    else:
        SKU += 'low'
    SKU += ','
    if Allerg == '':
        SKU += 'no'
    else:
        SKU += 'yes'
    SKU += ','
    SKU += Micro.lower()
    return SKU

#print process_line('Salad,1900,Asian Noodle Salad,$3.99,"Angel Hair Pasta, Chile Oil, Scallions, Cilantro, Toasted Almonds, Tamari",Nuts,No')
