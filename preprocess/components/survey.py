# Output Attributes (in order):
# (0) Food type (vegan, carnivore, vegetarian, or a mix)
# (1) Has allergies (yes, no)
# (2) Breakfast likelihood (never, sometimes, always)
# (3) Lunch likelihood (never, sometimes, always)
# (4) Dinner likelihood (never, sometimes, always)
# (5) Satisfaction with variety (yes, no)
# (6) Satisfaction with quantity (under, fine, over)
# (x) Qualities for choosing selection (raw data) # REDACTED
# (7) Price willing to pay (int)
# (8) Willing to buy if added food options (yes, no, indifferent)
# (9) Frequency of Sandwich Purchase (never, sometimes, always)
# (10) Frequency of Salad Purchase (never, sometimes, always)
# (11) Frequency of Soup Purchase (never, sometimes, always)
# (12) Frequency of Rice entree Purchase (never, sometimes, always)
# (13) Frequency of Noodle Purchase (never, sometimes, always)
# (14) Frequency of Pasta Purchase (never, sometimes, always)
# (15) Frequency of Desert Purchase (never, sometimes, always)
# Author: Kevin Xu (klx@andrew.cmu.edu)

# Removes the commas that are not indicative of column change
def convert_commas(inp):
    toks = inp.split('"')
    out = ""
    for i in xrange(len(toks)):
        if i % 2 == 1:
            out += toks[i].replace(',', '+')
        else:
            out += toks[i]
    return out

def process_entry(tok):
    if 'all the time' in tok:
        return 'always'
    if 'specific time' in tok or 'would like to try' in tok:
        return 'sometimes'
    if 'Never' in tok:
        return 'never'
    return ''

def process_line(inp):
    inp = convert_commas(inp)
    toks = inp.split(',')
    try:
        food_type = toks[1]
        allergy = toks[2]
        breakfast = toks[3]
        lunch = toks[4]
        dinner = toks[5]
        variety = toks[6]
        quantity = toks[8]
        price = toks[12]
        buy = toks[15]
        sandwich = toks[10]
        salad = toks[16]
        soup = toks[17]
        rice = toks[18]
        noodle = toks[19]
        pasta = toks[20]
        desert = toks[21]
    except:
        return False
    out = ""
    if 'vegan' in food_type:
        out += 'vegan+'
    if 'vegetarian' in food_type:
        out += 'vegetarian+'
    if 'carnivore' in food_type:
        out += 'carnivore+'
    if 'omnivore' in food_type:
        out += 'carnivore+vegetarian+'
    if out:
        out = out[:-1] # remove trailing +
    out += ','
    if 'no' in allergy or 'No' in allergy:
        out += 'no'
    elif allergy:
        out += 'yes'
    out += ','
    if 'Never' in breakfast:
        out += 'never'
    elif 'Sometimes' in breakfast:
        out += 'sometimes'
    elif 'Majority' in breakfast:
        out += 'always'
    out += ','
    if 'Never' in lunch:
        out += 'never'
    elif 'Sometimes' in lunch:
        out += 'sometimes'
    elif 'Majority' in lunch:
        out += 'always'
    out += ','
    if 'Never' in dinner:
        out += 'never'
    elif 'Sometimes' in dinner:
        out += 'sometimes'
    elif 'Majority' in dinner:
        out += 'always'
    out += ','
    if 'ok' in variety:
        out += 'yes'
    elif 'not happy' in variety:
        out += 'no'
    out += ','
    if 'little' in quantity:
        out += 'under'
    elif 'about right' in quantity:
        out += 'fine'
    elif 'much' in quantity:
        out += 'over'
    out += ','
    try:
        out += str(int(price))
    except:
        pass
    out += ','
    if 'Yes' in buy:
        out += 'yes'
    elif 'No' in buy:
        out += 'no'
    else:
        out += 'indifferent'
    out += ','
    out += process_entry(sandwich) + ','
    out += process_entry(salad) + ','
    out += process_entry(soup) + ','
    out += process_entry(rice) + ','
    out += process_entry(noodle) + ','
    out += process_entry(pasta) + ','
    out += process_entry(desert)
    return out

sample = '11/10/2015 10:04:03,"omnivore (I eat everything, including meat and             vegetables), Calories watcher, Nutrition watcher",,Majority of the time,,,It is ok as it is,,Too little,"Affordable, Healthy Options, Great Taste","My favorite only at a specific time (breakfast, lunch or dinner)",,10,,,Yes,,,,My favorite  all the time,My favorite all the time,,,,,,,,^M'
print process_line(sample)

