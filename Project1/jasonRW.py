import json
import os

#*****************************
# read_from_jason
# ver. 1.0.0
# A. Ryzhikov
#*****************************
def read_from_jason(xname):
#******************************************************************
# par xname   strung, name of jason-file  for example 'UTC.jason' 
# value     list [[a1,b1]...[ai,bi]]? where ai -zone name, bi - UTC
#******************************************************************

# open/save to json
	if os.path.exists(xname)==False:    
		
		data = [['Caliningrad', 2],
		        ['Moscow', 3],
        		['Cazan,Astrahan', 4],
        		['Salehard,Tumen', 5],
     			['Omsk', 6],
     			['Norilsk,Tomsk', 7],
     			['Bratsk,Irkutsk', 8],
     			['Yakutsk,Chita', 9],
     			['Verhoyansk,Vladivostok', 10],
     			['Magadan,Sahalin', 11],
     			['Anadyr,Kamchatka', 12]
			]

		
		fh = open(xname, 'w')  # open file for write
		fh.write(json.dumps(data))  #, ensure_ascii=False)) # dict to str to file
        
		
	# load from json
	fh=open(xname, 'r')  # open file for read
	a=json.load(fh)
	return a  # from file to list
    
