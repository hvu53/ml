import sys
wordcounts = {}
for line in sys.stdin:
    toks = line.split(',')
    SKU_type = toks[2]
    if SKU_type in wordcounts:
        wordcounts[SKU_type] += 1
    else:
        wordcounts[SKU_type] = 1

print wordcounts

