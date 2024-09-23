#06comprehension.py
import time

print('='*50)
time.sleep(1)
mylist= [ a**2 for a in range(1,11,1) ] #추천
print(mylist)
print()


myset = { c**2 for c in range(1,11,1) } #단점 순서없음
print(myset)
print()

