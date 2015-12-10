Preprocessing of datasets (Cleaning and Categorizations)
Author: Kevin Xu (klx@andrew.cmu.edu)

The datasets for the master SKU spreadsheet and sales records are great and well defined, but the weekly spreadsheets (like 09 September.csv) are not.

It's rather difficult to categorize the weekly sheets since they are only sold in units like 2-3, so it's often times either 100% sold, or 100% wasted, not usually in between.

For now, we should use the sales records like 'CMU 9.1-9.9.csv' and unit details like 'SKU Master' to ML.

Further details of the column categories are as follows:

CMU 9.1-9.9 proc.csv:
Unit name,Unit ID (not SKU!),Quantity sold,Time of day sold

SKU Master proc.csv:
SKU number,Unit name,SKU type,food type,price range,contains allergies,microwaved

09 September proc.csv / similar:
SKU number,efficiency category,wasted category


The possible values for each attribute can be found in attributes.txt. I may join the files using SKU numbers and Unit names if people need them.

But usage should ideally be the following: Use the SKU Master spreadsheet to look up information, since that's where the majority of the data is found. Then use other information to learn on.

If you wish to see how the sets are generated, you can check the source code in /components. To run the scripts on all the currently available data, just run main.py

Converting between the provided raw .xlsx files to python readable .csv files will require installation of xlrd for python. To install, simply run:
pip install xlrd

USAGE:

python components/main.py (flags)

flags:
h or help for instructions
c or convert for converting xlsx files to .csv
m for processing monthly csv files
w for processing weekly csv files
sku for processing the SKU Master spreadsheet


