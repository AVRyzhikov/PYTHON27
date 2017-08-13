#*************************
# ums_time
# ver 1.0.0
# A.Ryzhikov
#*************************
import datetime
from datetime import timedelta
import jasonRW

#****************************
def name_by_utc(xutc,xlist):
#****************************
	for i in xlist:
		if i[1]==xutc:
			return i[0]


#****************************************
#  current  name by current utc
now_time = datetime.datetime.now() 
now_time0= now_time.utcnow() 
utc0= (now_time-now_time0).seconds /3600 # current UTC
list0=jasonRW.read_from_jason('UTC.jason') # jason file data

xstr=name_by_utc(utc0,list0)

#****************************************

print 'Current time = '+ now_time.strftime("%H:%M:%S")+ ' '+xstr+' (UTC+%d)' % utc0
for i in list0:
	if i[0]<>xstr:
		hi = datetime.timedelta(hours=utc0) - datetime.timedelta(hours=i[1])
		hh=now_time-hi
		print hh.strftime("%H:%M:%S ") + i[0] + ' (UTC%+d)\(%s %+d)' % (i[1],xstr,i[1]-utc0)
					# print now_time-hi)strftime("%H:%M:%S"}
 