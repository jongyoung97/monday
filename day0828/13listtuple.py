#13listtuple.py

#리스트는 순서유지 ,중복허용
#튜플도 순서유지 , 중복허용
mylist=['kim',78,True, 3.1415, 78, 'kim' ]
mytuple = ('Lee',54,False, 3.1415 , 54,'Lee')

mylist[1]=1200 #리스트는 변경이 가능함
#mytuple[1]=1200 -> error / 튜플은 변경이 안됨
print(mylist)
print(mytuple)



print()

