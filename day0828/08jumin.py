#08jumin.py

import datetime
import time

#jumin='971230-1835064'

#문제 1 성별체크 1,3 남자 2,4여자
#문제 2 생일 12월30일 - 생일축하합니다
#문제 3 나이계산 2024-1997=???

print()
jumin=int(input("'-'없이 주민번호를 입력해주세요"))
x=str(jumin)
if x[6:7]== ('1' or '3') :
    print('남자입니다')
else :
    print('여자입니다.')    
birth=x[2:6]
print('생일이',birth[0:2],'월',birth[2:5],'일','입니다')
if birth == '1230':
    print('생일축하합니다')
else :
    print('생일이 아닙니다')
age=str(f'{19}{x[0:2]}')
y=datetime.datetime.now()
z=str(y)
x=z[0:4]
i = int(age)
j = int(x)
print('나이 :',x,'-',age,'=',j-i)

