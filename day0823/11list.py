#11list.py

import time

lista = [ 20, 10, 40, 50, 30]
print(lista) #[20, 10, 40, 50, 30] 출력

time.sleep(0.5)
lista.insert(2,9) #3번쨰에 9 추가 [20, 10, 9, 40, 50, 30]
print(lista)

time.sleep(0.5)
lista.append(7) #append는 맨끝에 추가 [20, 10, 9, 40, 50, 30, 7]
print(lista) 

time.sleep(1)
#lista.remove(10) remove는 데이터값없으면 에러가 발생한다.
lista.pop(3)
print(lista)

time.sleep(1)
lista.reverse()
print(lista)

# lista.sort(reverse=True)
# print(lista)


print()