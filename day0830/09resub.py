#09resub.py

import re

phone = '010-1234-5678 박이썬'
re.sub( '1패턴', '2변경적용', phone)
model = re.sub( '-[0-9]{4}-','-****-' , phone)

print(phone)  # 010-1234-5678 박이썬
print(model)  # 010-****-5678 박이썬




# msg= 'my BEST %#@& 245 오렌지 is (_^!& ^.^ 수박 cheery as tea '

# result1 = re.findall('[\w]+' ,msg)
# result2 = re.findall('[\W]+' ,msg) #비권장 대문자가 없으면 안나왕
# result3 = re.findall('[a-zA-Z0-9가-힣]+',msg)
# result4 = re.findall('[^a-zA-Z0-9가-힣]+',msg)

# print(result1);print()
# print(result2);print()
# print(result3);print()
# print(result4);print()






