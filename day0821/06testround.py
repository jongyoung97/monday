#06testprint.py

# 변수 다중선언


a,b,ret = 9, 4, 0
mok = 34.56921
print(mok) #34.56921
print('%d' %(mok)) #34
print('%f' %(mok)) #34.569210 // %f는 자릿수 지정안하면 6자릿수까지 출력 
print('%5.2f '%(mok)) #34.57  %5.2f 는 6자리 수를 소수2번째자리까지 표현한다는 뜻
print('%.2f '%(mok)) #34.57
print(round(mok,2))  #34.57 내장함수 round(값,2)



# 내장함수 print(), int(), type(), input('안내문'),str() , sum()
# round(데이터,실수자릿수2)

# %자릿수d정수 %자릿수f실수
#print('%d정수' %(데이터))
#print('%d *%d = %d' %(a,b,ret))

# 원하는 영역 블럭선택후 ctrl + / 하면 주석처리됨
#곱하기연산처리
# ret = a*b


# #print(변수, '문자', ~~ )
# print(a, '*', b, '=', ret)

# #print( '%d 정수 , %s 문자열 ,%f 실수 ,%c 문자' )
# print('%d * %d = %d' %(a,b,ret))

# #print( '{}*{} = {}'.format(a,b,ret) )
# print('{} * {} = {}'.format(a,b,ret))

# #print(' f{변수및값}' )
# print(f'{a} * {b} = {ret}')

# print()
