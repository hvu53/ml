# Buckets sell rate into how much was sold, and how much was wasted
# Author: Kevin Xu (klx@andrew.cmu.edu)

# Returns SKU,Sold category,Wasted category
def process_line(inp):
    toks = inp.strip().split(',') # A clean line has 14 tokens
    try:
        SKU = str(int(float(toks[0])))
        soldcount = int(float(toks[len(toks)-4]))
        wastecount = int(float(toks[len(toks)-3]))
        sold = float(toks[len(toks)-2]) * 100
        waste = float(toks[len(toks)-1]) * 100
        if sold > 101 or waste > 101:
            return False
    except:
        return False
    SKU += ','
    # Using continuous variables for now
    # Can discretize if needed
    SKU += str(soldcount) + ',' + str(wastecount) + ',' + str(sold) + ',' + str(waste)
    '''
    if sold == 100:
        SKU += str('100')
    elif sold >= 75:
        SKU += str('75')
    elif sold >= 50:
        SKU += str('50')
    elif sold >= 25:
        SKU += str('25')
    else:
        SKU += str('0')
    SKU += ','
    if waste == 100:
        SKU += str('100')
    elif waste >= 75:
        SKU += str('75')
    elif waste >= 50:
        SKU += str('50')
    elif waste >= 25:
        SKU += str('25')
    else:
        SKU += str('0')
    '''
    return SKU

#print process_line('1910,,,,,3,0,0,0,,3,0,100.00%,0.00%')

