#07comprehension.py [ 연산 if/else for~~ ]

message = ['spam','ham','spam','ham','spam','spam','ham','spam']

#문제1 set보다는 리스트구현 why/ set은 순서가 없어서불편
#      for 반복 ~if
# spam출력, 갯수도출력
message_cnt = 0
for k in message:
    if k=='spam':
        print(k,end=' ')
        message_cnt += 1 #message_cnt= message_cnt+1

print()
print('갯수 ', message.count('spam'))        
print('갯수 ', message_cnt)


print()
#문제2 [ 맨앞 if조건 else불뒤 for~~ ]comprehension처리 
#문제2 [ 맨앞 for~~~~ if 조건만족 ] comprehension처리
temp_list= [k for k in message if 'spam' in k ]
print(temp_list)


