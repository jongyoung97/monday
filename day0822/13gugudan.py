# 13gugudan.py

dan = 7
for k in range(1,10,1):
    pass    

print()
print('구구단연습')
'''
파이썬 화면모니터 출력 print( '안내문', 값)
파이썬 키보드자판 입력 input('안내문')
파이썬 키보드입력 데이터는 문자로 인식
int("78") 숫자 78
'''
# a='12300'
# b='87'
# print(a+b) #1230087

# c = int(a) + int(b) #int정수 = integer
# print(int(a)+int(b)) #12387
# print(c)             #12387

#파이썬 내장함수
#print(), int(), round(),input(),str(),sum()

data = input('구구단입력>>> ')
dan = int(data)
for k in range(1,10,1):
    print(dan, '*', k, '=', (dan*k))

print()
          
