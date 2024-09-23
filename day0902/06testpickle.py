#06testpickle.py

# open(1파일명, 모드wb/rb,인코딩)
# dump쓰기/load읽기
# 피클로 파일처리 import

import pickle
import time

fileName= 'C:/Mtest/movie.pckl'
mybest = {'슈퍼맨superman': 9.72, '아이ironman':7.45, '손흥민': 5.3 }
file = open(fileName, 'wb')

pickle.dump(mybest, open(fileName,'wb'))
print(fileName, '피클저장 성공했습니다')
print('-'*60)
print()

time.sleep(0.7)
#피클파일 저장 dump(1,2)/load(1,'rb')
data = pickle.load(open(fileName,'rb'))
print(data)