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
print(my.tm_wday)

time.sleep(0.2)
print()

dt = datetime.now()
print(dt)

time.sleep(0.05)
print('aaaaaa')
time.sleep(0.03)
print('bbbbbb')