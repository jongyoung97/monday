#10testlambda.py


#람다 는 익명의 함수 -> 함수이름이 없어유
#람다식은 import 없다
#람다식은 lambda 키워드기술
def mysu(num):
    value = 3*num+5
    return value


data = int(input('숫자입력>>> '))    
print('일반식', mysu(data))
print('람다식',(lambda number:3*number+5 )(data))
print()
