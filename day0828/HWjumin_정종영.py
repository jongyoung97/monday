#HWjumin_정종영.py


#문제 1 성별체크 1,3 남자 2,4여자
#문제 2 생일 12월30일 - 생일축하합니다
#문제 3 나이계산 2024-1997=???
#함수 써서 해보기

import datetime
import time

def gender():
    if gen == ( 1 or 3):
        return '남성입니다.'
    else:
        return '여성입니다.'

def birth():
    if bir == 1230:
        return '생일입니다. 축하합니다'
    else:
        return '생일이 아닙니다 ㅜㅜ'
         

def age():
    now = datetime.datetime.now()
    user_age=(now.year)-(birth_year)   
    return user_age
while True:
    r_number=str(input('주민등록번호를 입력하십시오>>> :'))
    if len(r_number) == 14:
        list_r_number=r_number.split('-')
        break
    elif len(r_number) == 13:
        list_r_number=[r_number[:6],r_number[6:]]
        break
    else:
        print("잘못된 입력입니다. 다시 입력해주십시오.")    

gen = int(list_r_number[1][0])
print('성별: ', gender())

bir = int(list_r_number[0][2:6])
print('생일: ',bir,birth())

birth_year = 1900 + int(list_r_number[0][0:2])
print('나이: ',age())
             


