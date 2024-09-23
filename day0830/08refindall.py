#08refindall.py

import re

# url = 'www.google.com'

# print(url)
# myret = url.split('.')

# ct= ' '
# print(' '.join(url))
# 첫번째 정규식 예제 
# msg = 'my best% 2400 Flu_it is blue%#357cherry'

# info1 = re.findall('[a-zA-Z]{3,7}', msg)
# info2 = re.findall('[a-zA-Z0-9]{3,7}', msg)
# print(info1)  ['best', 'Flu', 'blue', 'cherry']
# print()
# print(info2)  ['best', '2400', 'Flu', 'blue', '357cher']
# print()

# my = re.findall('[a-zA-Z]{4,10}', msg)
# if my :
#     print(my)   ['best', 'blue', 'cherry']
# else:
#     print('[a-zA-Z]{4,10} 조건에 맞는 데이터 없습니다.')

#msg변수에 새로운 내용을 재할당
msg= 'my BEST %#@& 245 오렌지 is (_^!& ^.^ 수박 cheery as tea '

result1 = re.findall('[\w]+' ,msg)
result2 = re.findall('[\W]+' ,msg) #비권장 대문자가 없으면 안나왕
result3 = re.findall('[a-zA-Z0-9가-힣]+',msg)
result4 = re.findall('[^a-zA-Z0-9가-힣]+',msg)

print(result1);print()
print(result2);print()
print(result3);print()
print(result4);print()




