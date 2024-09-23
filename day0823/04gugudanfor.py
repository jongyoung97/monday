#gugudanfor.py

import time

dan = int(input('원하는 단입력>>> '))
#input('안내문') 문자형으로 인식함 그래서 int처리하면 수 로인식
for k in range(1,10,1):
    print(f'{dan}*{k}={dan*k}')
    time.sleep(0.05)  #초단위기술


print()
print('kakao')    
print('naver')    