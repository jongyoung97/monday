#01 test lambda . py
#람다식은 import 기술안함 , 키워드 lambda기술

def mycal(su):
    cal = 3 * su + 8
    return cal

print('일반식', mycal(5))
print()
my1 = lambda su: 3*su+8
print('람다식', my1(5))
print('람다식', (lambda su: 3*su+8 )(21))

print()


def myAdd(x,y):
    hap = x+y
    return hap

print('일반식', myAdd(3,4))
my2 = lambda x,y: x+y
print('람다식', (lambda x,y : x+y)(3,4))
print('람다식', my2(3,5))
print()
print('='*50)
# 함수에서 계산처리후 if~else제어문 리턴값

def myCheck(su):
    msg = '안내문'
    if su % 2 == 0:
        msg = '짝수'
    else:
        msg = '홀수'
    return msg

print('일반식', myCheck(17))
print('람다식', (lambda su :  '짝수' if su % 2 == 0  else '홀수' )(18))

    