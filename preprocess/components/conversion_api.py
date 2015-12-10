# Takes in .csv files or .xlsx files as raw input
# Converts them, and keeps the intermediate outputs
# And ultimately outputs a dictionary of entries

import retrieve_dicts
from main import monthly_file, weekly_file, sku_file, convert_file, survey_file

def efficiency(fname):
    converted = convert_file(fname)
    weekly = []
    for convertedname in converted:
        processed = monthly_file(convertedname)
        weekly.append(retrieve_dicts.parse_efficiency(processed))
    return weekly

def sales(fname):
    processed = weekly_file(fname)
    return retrieve_dicts.parse_sales(processed)

def sku(fname):
    processed = sku_file(fname)
    return retrieve_dicts.parse_sku(processed)

def survey(fname):
    processed = survey_file(fname)
    return retrieve_dicts.parse_survey(processed)

def test():
    print sku('SKU Master.csv')
    print sales('CMU 9.1-9.9.csv')
    print efficiency('09 September.xlsx')
    print survey('ML for Lunch Survey.csv')


test()
