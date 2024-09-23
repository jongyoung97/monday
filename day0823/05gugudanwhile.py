#05gugudanfor.py

import time

data = int(input('원하는 단입력>>> '))
dan = int(data)

k=1
while True :
    print(f'{dan}*{k}={dan*k}')
    k = k+1
    if k==10:
        break
    time.sleep(0.05)
    

print()
   