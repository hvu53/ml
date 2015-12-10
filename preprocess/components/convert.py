# Converts the raw .xls files to readable .csv files
# Uses xlrd, install it using:
# pip install xlrd
# Author: Kevin Xu (klx@andrew.cmu.edu)
import xlrd

input_dir = '../data/raw_xlsx/'
output_dir = '../data/Monthly_csv_converted/'

def parse_cell(inp):
    try:
        return str(inp.value)
    except:
        return "Encoding error!"

def save_sheet(sheet):
    lines = range(sheet.nrows)
    rows = map(lambda i: sheet.row(i), lines)
    out = map(lambda row: (map(parse_cell, row)), rows)
    return map(lambda vals: ','.join(vals), out)

def convert_xls_to_csv(fname):
    full_name = input_dir + fname
    book = xlrd.open_workbook(full_name)
    out_names = []
    for sheetname in book.sheet_names():
        try:
            newname = fname[:-5] + '_' + sheetname + '.csv'
        except:
            newname = sheetname + '.csv'
        output = output_dir + newname
        sheet = book.sheet_by_name(sheetname)
        csv = save_sheet(sheet)
        out = open(output, 'w+')
        for line in csv:
            out.write('%s\n' % line)
        out_names.append(output)
    return out_names

#convert_xls_to_csv('09 September.xlsx')

