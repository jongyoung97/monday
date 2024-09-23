#07comprehension.py [ 연산 if/else for~~ ]

message = ['spam','ham','spam','ham','spam','spam','ham','spam']

#문제1 set보다는 리스트구현 why/ set은 순서가 없어서불편
#      for 반복 ~if
# spam출력, 갯수도출력
for k in message:
    if k=='spam':
        print(k,end=' ')


print()
#문제2 [ 맨앞 if조건 else불뒤 for~~ ]comprehension처리 
#문제2 [ 맨앞 for~~~~ if 조건만족 ] comprehension처리
temp_list= [k for k in message if k=='spam']
print(temp_list)

print()
dummy = []
#문제3 spam= 0 , ham = 1 dummy = [0,1,0,1,0,0] , ret = [ ]
#message = ['sapm','ham','spam','ham','sapm','spam']
#for ~~if ~else
for k in message:
    if k=='spam':
        dummy.append(0)
    else:
        dummy.append(1)

print('반복~제어정석 ',dummy)

mydummy=[ 0 if k == 'spam' else 1 for k in message ]
print('comprehension', mydummy)

