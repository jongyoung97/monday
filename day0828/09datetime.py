#09jumin.py

import datetime
import time

# x=datetime.now() #->에러

#x=
y=datetime.datetime.now() 
#z=

print(y)      #2024-08-28 11:18:43.344892
print(str(y)) #2024-08-28 11:18:43.344892  / 안전화
z=str(y)
print(z[0:4]) #2024
print()

dt = datetime.datetime.now()
print(dt.strftime('현재날짜 %Y년-%m월-%d일')) #현재날짜 2024년-08월-28일
print(dt.strftime('현재날짜 %H시-%M분-%S초')) #현재날짜 11시-24분-01초

mytime = time.localtime()
print(mytime) #time.struct_time(tm_year=2024, tm_mon=8, tm_mday=28, tm_hour=11, tm_min=26, tm_sec=2, tm_wday=2, tm_yday=241, tm_isdst=0)
print(mytime.tm_year,'년도') #2024 년도