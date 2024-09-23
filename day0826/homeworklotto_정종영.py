#homeworklotto.py

import random

#로또 1~45 사이
#로또 특성 상 정수 
#반복문 for,while,if사용해보기
#난수발생 6개 숫자 중복체크 조별...
#난수발생후 출력은 sort정렬
#set 이용x , 
lotto=[]
com = random.randint(1,45)
for k in range(6):
    while com in lotto:
        com = random.randint(1,45)
    lotto.append(com)    
    
lotto.sort()
print("lotto number : ", lotto)    



#==================================================
print('=' *50)


lotto_2=[]

while len(lotto_2) < 6: 
    k = random.randint(1,45)
    if k in lotto_2 :
        continue
    else:
        lotto_2.append(k)

lotto_2.sort()
print("lotto_2 number: ",lotto_2)         


print('='*50)
#========================================================
lotto_3=[]

while True:
    com = random.randint(1,45)
    if com in lotto_3:
        continue
    else:
        lotto_3.append(com)
        if len(lotto_3) == 6:
            break

lotto_3.sort()
print("lotto_3 number: ", lotto_3)