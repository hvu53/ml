import efficiency, sales, products, survey
import convert
import os, sys
# Keywords for splits stored in meats, seafoods, vegetables
# This accuracy depends on the keywords being split on
# We'll split on meat first, then seafood, then vegetarian

Monthly_dir = '../data/Monthly_csv_converted/'
Weekly_dir = '../data/Weekly_Sales_Records/'
SKU_dir = '../data/SKU_Master/'
Monthly_out_dir = '../output/Monthly_Sold_Waste/'
Weekly_out_dir = '../output/Weekly_Sales_Records/'
SKU_out_dir = '../output/SKU_Master/'
raw_dir = '../data/raw_xlsx/'
convert_outdir = '../data/Monthly_csv_converted/'
survey_dir = '../data/survey/'
survey_out_dir = '../output/survey/'

def process_file(process_fun, file_name, out_file, meats=False, seafoods=False, vegetables=False):
    with open(file_name) as f:
        inputs = f.readlines()
    if meats:
        outputs = map(lambda s : process_fun(s.strip(), meats, seafoods, vegetables), inputs)
    else:
        outputs = map(process_fun, inputs)
    outputs = filter(lambda s : s, outputs)
    out = open(out_file, 'w+')
    for line in outputs:
        out.write("%s\n" % line)

# A simple test case for each file type
def test():
    with open('keywords/meats') as f:
        meats = map(lambda s : s.strip(), f.readlines())
    with open('keywords/seafoods') as f:
        seafoods = map(lambda s : s.strip(), f.readlines())
    with open('keywords/vegetables') as f:
        vegetables = map(lambda s : s.strip(), f.readlines())
    try:
        efficiency.process_line('1910,,,,,3,0,0,0,,3,0,100.00%,0.00%')
        sales.process_line('Chinese Chicken Salad Wrap,238908,1,null,$5.75 ,$5.75 ,$0.00 ,Y,9/9/2015 19:42,CMU-1')
        products.process_line('Sandwich,1823,B&B Grilled Steak Sandwich,$7.25,"Herb Marinated Grilled Skirt Steak, Bacon, Butter Lettuce, Blue Cheese Spread, Whole Grain Mustard, Sliced Sourdough Bread",Dairy/ Gluten,Yes', meats, seafoods, vegetables)
        products.process_line('Sandwich,1804,Classic Tuna Sandwich,$7.25,"Classic Tuna Salad, Swiss Cheese,    Lettuce, Tomato, Sliced Red Onion, Croissant",Dairy/ Gluten,Yes', meats, seafoods, vegetables)
    except:
        print "Test failed!"
        return False
    return True

def monthly_file(fname):
    if not os.path.exists(Monthly_out_dir):
        os.makedirs(Monthly_out_dir)
        print "Created Monthly output directory..."
    fullname = Monthly_dir + fname
    outname = Monthly_out_dir + fname
    process_file(efficiency.process_line, fullname, outname)
    return outname

def weekly_file(fname):
    if not os.path.exists(Weekly_out_dir):
        os.makedirs(Weekly_out_dir)
        print "Created Weekly output directory..."
    fullname = Weekly_dir + fname
    outname = Weekly_out_dir + fname
    process_file(sales.process_line, fullname, outname)
    return outname

def survey_file(fname):
    if not os.path.exists(survey_out_dir):
        os.makedirs(survey_out_dir)
        print "Created Survey output directory..."
    fullname = survey_dir + fname
    outname = survey_out_dir + fname
    process_file(survey.process_line, fullname, outname)
    return outname

def sku_file(fname):
    if not os.path.exists(SKU_out_dir):
        os.makedirs(SKU_out_dir)
        print "Created SKU output directory..."
    fullname = SKU_dir + fname
    outname = SKU_out_dir + fname
    with open('keywords/meats') as f:
        meats = map(lambda s : s.strip(), f.readlines())
    with open('keywords/seafoods') as f:
        seafoods = map(lambda s : s.strip(), f.readlines())
    with open('keywords/vegetables') as f:
        vegetables = map(lambda s : s.strip(), f.readlines())
    process_file(products.process_line, fullname, outname, meats, seafoods, vegetables)
    return outname

def convert_file(fname):
    if not os.path.exists(convert_outdir):
        print "Making output directory"
        os.makedirs(convert_outdir)
    converted = convert.convert_xls_to_csv(fname)
    return map(lambda s: s.split('/')[-1], converted)

def main():
    if not test():
        print "Preliminary tests did not pass!"
        print "Check that the keyword files and components are all present"
        return
    args = sys.argv
    if len(args) <= 1 or 'all' in args:
        print "Converting and Processing all directories"
        args = ['m', 'w', 'sku', 'c', 's']
    if 'h' in args or 'help' in args:
        print "Usage: h for help"
        print "c or convert for converting xlsx to csv files"
        print "m to process monthly directory"
        print "w to process weekly directory"
        print "sku to process SKU master"
        print "Default: nothing for all 3 directories\n"
    if 'c' in args or 'convert' in args:
        print "Converting xlsx files to .csv"
        for fname in os.listdir(raw_dir):
            convert_file(fname)
            print "Finished converting files to csv"
        if len(args) != 4:
            return
    else:
        args = args[1:]
    if 'm' in args:
        print "Processing Monthly directory now..."
        for fname in os.listdir(Monthly_dir):
            monthly_file(fname)
        print "Monthly Processing Done.\n"
    if 'w' in args:
        print "Processing Weekly directory now"
        for fname in os.listdir(Weekly_dir):
            weekly_file(fname)
        print "Weekly Processing Done.\n"
    if 'sku' in args:
        print "Processing SKU Master directory now"
        for fname in os.listdir(SKU_dir):
            sku_file(fname)
        print "SKU Processing Done.\n"
    if 's' in args:
        print "Processing Survey directory now"
        for fname in os.listdir(survey_dir):
            sku_file(fname)
        print "Survey Processing Done.\n"
#main()
