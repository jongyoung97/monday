#HWsetlotto.py

lotto = set()

#금지 lotto=list() 리스트쓰지마셈
#추천 lotto = set() #셋항목함수 lotto.add()
#난수 로또 숫자 발생, 중복체크, set추가
#출력은 오름차순적용 sort이용
#set데이터타입을 list변환
import random

def mysetlotto():
    lotto=set(random.sample(range(1,46),6))
    number = sorted(lotto)
    print("lotto number: ",number)

def mysetlotto_2():
    lotto=set()
    while True:
        number = random.randint(1,45)
        if number not in lotto:
            lotto.add(number)
            if len(lotto)==6:
                break
    number= sorted(lotto)
    print("lotto number2: ",number)            

mysetlotto()    
print()
print('='*50)
print()
mysetlotto_2()



    #while ~ while ~ if ~ else
    #while ~ for ~ if ~ else
    #while ~ if ~ else



