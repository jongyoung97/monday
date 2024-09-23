#08testfor.py

# 문자열, 리스트출력, turply, set, dict
# 반복데이터 사용
'''
for 변수 대표 k in range(5) :
    5회처리 0~4까지 5회처리

for 변수 대표 k in range(1,5) :
    4회처리 1~4까지 4회처리

for 변수 대표 k in range(1,5,1) :
    4회처리 1~4까지 4회처리
    1씩 증가일때 3번째 1 생략

 while조건 :
     조건만족시 루프loop처리
     무한루프처리일때 if제어문으로 break반복탈출   
'''
#for,while연습할 때 사용 a, b, hap, tot

a, b=0, 0
hap, total=0, 0

#첫번째 a, hap 1~5출력 누적
'''
 1 1
 2 3
 3 6
 4 10
 5 15
 6 21
'''
a= a+1 ; hap = hap+a ; print(a,hap) 
a= a+1 ; hap = hap+a ; print(a,hap) 
a= a+1 ; hap = hap+a ; print(a,hap) 
a= a+1 ; hap = hap+a ; print(a,hap) 
a= a+1 ; hap = hap+a ; print(a,hap) 
a= a+1 ; hap = hap+a ; print(a,hap) 


print()

#for반복문, 대입연산

a, hap = 0,0 #재선언보다는 초기화

for k in range(6):
    a = a+1
    hap = hap + a
    print(a, hap)

