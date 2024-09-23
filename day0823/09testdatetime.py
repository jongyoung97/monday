#08testdatetime.py

import time
import datetime
#from 파일명클래스 import datatime
from datetime import datetime

my = time.localtime()
print(my)
print(my.tm_year,'년') 
print(my.tm_mon,'월')
print(my.tm_mday,'일')
wday = my.tm_wday

week = [ '월요일','화요일','수요일','목요일','금요일','토요일','일요일']
print(week[wday])
#반복문대신 if제어문
#0월요일 1화요일 2수요일 3목요일 4금요일 5요일 6일요일
# if wday == 0:
#     print('월요일')
# elif wday == 1:
#     print('화요일')
# elif wday == 2:
#     print('수요일')          
# elif wday == 3:
#     print('목요일')
# elif wday == 4:
#     print('금요일')
# elif wday == 5:
#     print('토요일')
# elif wday == 6:
#     print('일요일')       
# else:
#     print('요일지정 잘못되었습니다')                        