#10recompile.py

import re



data = '''
kim 840916-1694852
lee 921207-2059327
goo 981024-1674938
'''
#\n라인개행enter기능 \t탭 \b백space
#com = re.compile('(\d{6})[-](\d{7})')
com = re.compile('-\d+')
first = com.sub('-*******',data)
print(first)

two = re.sub('[0-9]{7}','*******', data) #권장 sub(1,2,3 적용문자열)
print(two)






# compile('\d{6}-\d{7}') 적용후 sub()확인
#문자열함수 for~~if~ data[시작위치:]
# model = re.sub( '-[0-9]{4}-','-****-' , phone)
# 정규식 compile(),sub(1,2,3),다른방법
# kim 840916-*******
# lee 921207-*******
# goo 981024-*******





# 4번째 정규식 예제 re.sub(1,2,3)
# 정규 sub(1,2,3)
# phone = '010-1234-5678 박이썬'
# # re.sub( '1패턴', '2변경적용', phone)
# model = re.sub( '-[0-9]{4}-','-****-' , phone)

# print(phone)  # 010-1234-5678 박이썬
# print(model)  # 010-****-5678 박이썬




# msg= 'my BEST %#@& 245 오렌지 is (_^!& ^.^ 수박 cheery as tea '

# result1 = re.findall('[\w]+' ,msg)
# result2 = re.findall('[\W]+' ,msg) #비권장 대문자가 없으면 안나왕
# result3 = re.findall('[a-zA-Z0-9가-힣]+',msg)
# result4 = re.findall('[^a-zA-Z0-9가-힣]+',msg)

# print(result1);print()
# print(result2);print()
# print(result3);print()
# print(result4);print()






