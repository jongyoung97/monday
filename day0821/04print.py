#02testprint.py

# 변수 하나씩 선언, 다중선언

a,b,ret = 9, 4, 0
msg = 1234

ret = a*b


#print( '{}*{} = {}'.format(a,b,ret) )
print('{} * {} = {}'.format(a,b,ret))

print('|{}|'.format(msg))         
print('|{:0>10,}|'.format(msg))   # 여기서 '>' 는 관계연산자가 아님  |000001,234|
print('|{:*>10},|'.format(msg))   #                                |******1234|
print('|{:,}|'.format(msg))       #                                |1,234|













'''

#print(변수, '문자', ~~ )
print(a, '*', b, '=', ret)

#print( '%d 정수 , %s 문자열 ,%f 실수 ,%c 문자' )
print('%d * %d = %d' %(a,b,ret))


#print(' f{변수및값}' )
print(f'{a} * {b} = {ret}')

print()

'''

