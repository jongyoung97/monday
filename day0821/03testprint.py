#02testprint.py

# 변수 하나씩 선언, 다중선언

#a=7
#b=4
#ret = 0 #결과 result축약한 변수이름


a,b,ret = 7, 4, 0

ret = a*b
print(ret) # print(' 7 * 4 = 28 ') 절대아님
#print(변수, '문자', ~~ )
print(a, '*', b, '=', ret)

#print( '%d 정수 , %s 문자열 ,%f 실수 ,%c 문자' )
print('%d * %d = %d' %(a,b,ret))

#print( '{}*{} = {}'.format(a,b,ret) )
print('{} * {} = {}'.format(a,b,ret))

#print(' f{변수및값}' )
print(f'{a} * {b} = {ret}')

print()
