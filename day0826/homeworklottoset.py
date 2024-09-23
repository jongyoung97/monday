#homeworklottoset.py

import random

lotto=[]
while len(lotto) !=6:
    lotto.append(random.randint(1,45))
    for k in range(len(lotto)) :
        if lotto.count(lotto[k]) >1 :
            lotto.pop()
            lotto.append(random.randint(1,45))

print(lotto)
lotto.sort()
print(lotto)

#==============SET=====================================
#로또 1~45사이 숫자
#숫자 중복체크
#리스트 대신 set사용

myset={7,29,45,3,36,12}
