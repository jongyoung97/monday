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

message = ' hello 길동!!!'
print(message)
print(message)
print(message)
print(message)
print(message)
print()


for k in range(5):
    print(k,message)
    #0부터 시작 ~ 4까지 5회처리 
    #10진수 0~9 2진수 0,1 8진수 0~7 16진수 0~9,A=(10),B,C,D,E,F
