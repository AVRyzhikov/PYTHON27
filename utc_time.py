import json
data = {'UTC+2/MSK-1': ['Caliningrad', 2,-1],
        'UTC+3/MSK': ['Moscow', 3,0],
        'UTC+4/MSK+1': ['Cazan,Astrahan', 4,1],
        'UTC+5/MSK+2': ['Salehard,Tumen', 5,2],
     	'UTC+6/MSK+3': ['Omsk', 6,3],
     	'UTC+7/MSK+4': ['Norilsk,Tomsk', 7,4]
}

# save to json
# fh = open('data.json', 'w') #, encoding='utf-8')  # open file for write
# fh.write(json.dumps(data))  #, ensure_ascii=False)) # dict to str to file

# load from json
fh=open('data.json', 'r') #encoding='utf-8')  # open file dor read
data1 = json.load(fh) # from file to dict
print data1['UTC+7/MSK+4'][2]
