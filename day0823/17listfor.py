#17listfor.py

mylist = ['kim', 7]
print(mylist)

mylist.append('민재')
print(mylist)

mylist.append(13)
print(mylist)

mylist.insert(1,'blue')
print(mylist)
print('='*50)
# 최종출력 ['kim', 'blue', 7, '민재', 13]
mylist[0]='SON' # 첫번째 데이터를 Kim->SON으로 변경
mylist[1]='토트넘'
print(mylist)
#['SON', '토트넘', 7, '민재', 13]



print()



#삭제 '민재' / del mylsit[1], remove , pop()
print(mylist)
mylist.pop(3)
print(mylist)

del mylist[3]
print(mylist)
mylist.sort()

#주의사항 sort()적용은 같은타입만 가능하다
