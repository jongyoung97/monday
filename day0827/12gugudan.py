# 12gugudan.py문서 함수

# 파이썬 함수 def  함수이름() :
# 파이썬 함수 매개인자
# 파이썬 함수 리턴값 
# 함수는 호출call 

# 내장함수
# list(), len(), tuple(), set()
# str(), int(), round(), print(), input()

# 리턴값X, 매개인자X  일반함수

import time

def gugudan(name,dan):
    for k in range(1,10,1):
        print(f'{dan} * {k} = {k*dan}')
        time.sleep(0.3)

mydata= 0
try:
    mydata = int(input('단입력>>> '))
except:
    print('정수 숫자를 입력하세요(1~9사이 숫자를 입력하세요\n)')
gugudan('jjy',mydata)
print() 

#문제 mysum함수호출












# 파이썬 함수 def  함수이름() :
# 파이썬 함수 매개인자
# 파이썬 함수 리턴값 
# 함수는 호출call 

