# homeworkstar.py문서
# 100page while 반복문 사용 금지

#조건 / 중복for반복문 
#처리 지역 변수 , 특정 변수 필요 없음
#반복문 대표 변수 x,y i,j, a,b
# for a in range(1,11,1):
#     for b in range(1,11,1):
#         pass
'''
🐣
🐣🐣
🐣🐣🐣
🐣🐣🐣🐣
🐣🐣🐣🐣🐣
'''

k='🐣'


for a in range(6):
    print(a * k)

print('-' * 50)

for a in range(5,0,-1):
    print(a*k)    

print('-' * 50)


'''
🐣
🐣🐣
🐣🐣🐣
🐣🐣🐣🐣
🐣🐣🐣🐣🐣
--------------------------------------------------
🐣🐣🐣🐣🐣
🐣🐣🐣🐣
🐣🐣🐣
🐣🐣
🐣
--------------------------------------------------
'''
for a in range(6):
    print(a*k)
    if a==5:
        for b in range(5,1,-1):
            print((b-1)*k)

print()

'''
🐣
🐣🐣
🐣🐣🐣
🐣🐣🐣🐣
🐣🐣🐣🐣🐣
🐣🐣🐣🐣
🐣🐣🐣
🐣🐣
🐣
'''
#--------------------------------------------------------------


print('-'*50)

for a in range(1,7,1):
    for b in range(1,a,1):
        print('*',end='')
    print()    