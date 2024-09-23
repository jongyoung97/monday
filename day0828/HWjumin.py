#HWjumin.py

import datetime
import time

jumin ='971230-1835064'

mylist = list(jumin.split('-')) #['971230', '1835064'] 은행금융보험쪽에서 -분리 유용하게쓰인다.
print(mylist)
print(mylist[0]) #971230
print(mylist[1]) #1835064
gender = mylist[1][0]
print('성별표시확인', gender) #1

if (jumin.split('-')[1][0]==1) or (jumin.split('-')[1][0])== 3 :
    pass
    print('당신의 성별은 남자입니다.')
elif (jumin.split('-')[1][0]==2) or (jumin.split('-')[1][0])== 4 :
    pass
    print('당신의 성별은 여자입니다.')
else:
    print('성별표기 오류입니다\n다시 체크하세요')



print()
print('='*50)


year = jumin.split('-')[0][:2]  # == year = jumin.split('-')[0][0:2]
print('태어난 년도 ', year)