# (1) Returns units per quantity
# (2) Categorizes based on time of day (early, mid, late)
# Author: Kevin Xu (klx@andrew.cmu.edu)

# Thresholds for timeliness
late = 19 # 7pm-onwards
mid = 13 # 1pm-7pm

# Returns Name,UID,QTY,time category
def process_line(inp):
    toks = inp.split(',')
    try:
        Name = toks[0]
        UID = toks[1] # NOT SKU!!
        QTY = toks[2]
        Date = toks[8]
        Time = Date.split(' ')[1]
        Hour = int(Time.split(':')[0])
    except:
        return False
    UID = Name + ',' + UID + ',' + QTY + ','
    if Hour >= late:
        UID += 'late'
    elif Hour >= mid:
        UID += 'mid'
    else:
        UID += 'early'
    return UID

#print process_line('Chinese Chicken Salad Wrap,238908,1,null,$5.75 ,$5.75 ,$0.00 ,Y,9/9/2015 19:42,CMU-1')
