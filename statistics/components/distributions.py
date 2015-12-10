# Processes each attribute individually and gives the
# distribution of each value within the attribute

survey_data = '../../preprocess/output/survey/ML for Lunch Survey.csv'
attr_count = 15
name = ['food_type', 'allergies', 'breakfast_freq', 'lunch_freq',
        'dinner_freq', 'variety_happiness', 'quantity_happiness',
        'pay_price', 'buy_if_added_options', 'sandwich_freq',
        'salad_freq', 'soup_freq', 'rice_freq', 'noodle_freq',
        'pasta_freq', 'desert_freq']
def distribution(fname):
    with open(fname) as survey:
        entries = survey.readlines()
    print ""
    print "____________________________________________"
    for feature in xrange(attr_count):
        d = {}
        total = 0.0
        for entry in entries:
            feat = entry.strip().split(',')[feature]
            if feat == "":
                continue
            if name[feature] != 'food_type':
                if feat in d:
                    d[feat] += 1
                else:
                    d[feat] = 1
                total += 1
            else:
                feats = feat.split('+')
                for f in feats:
                    if f in d:
                        d[f] += 1
                    else:
                        d[f] = 1
                    total += 1

        print "Feature " + name[feature] + " (" + str(feature) + ") distributions:"
        for k in d:
            print k + ": " + str(d[k]) + ' | ' + str(d[k] * 100 / total)[:5] + '%'
        if name[feature] == 'pay_price':
            count = 0
            total = 0.0
            mode_c = -1
            mode = 0
            for k in d:
                count += d[k]
                total += int(k) * d[k]
                if d[k] > mode_c:
                    mode = k
                    mode_c = d[k]
            print ""
            print "Additional stats for pay_price: "
            print "Total entries : " + str(count)
            print "Mean : " + str(total/count)
            print "Mode : " + mode
        print "____________________________________________"



distribution(survey_data)
