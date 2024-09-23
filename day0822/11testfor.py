#10testfor.py

#변수선언안하고 for대표변수 처리

#for k in range(1, 11, 1) :
#    print(k, end='\t')    #print()함수 자동 라인개행포함 엔터기능<br> 
    #5개씩 6줄 출력이니깐 if조건



for k in range(1,1001,1):
    print(k,end='\t')
    if k%5 == 0 :
        print()
    if k==40:
        break    


           
'''
문제 1 한줄에 row 5개씩 출력
for k in range(1,1001,1):
    print(k,end='\t')
    if k%5 == 0 :
        print()
문제 2 40숫자 출력 if 조건 반복탈출 break
for k in range(1,1001,1):
    print(k,end='\t')
    if k%5 == 0 :
        print()
    if k==40:
        break    

'''

        
        

 
    


    



print()       
print()
'''
1  2  3  4  5
6  7  8  9  10
11 12 13 14 15

....
'''

