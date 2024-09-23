#homeworksu.py
#list[]사용금지
#while반복문 사용해서 숫자 거꾸로 출력 ex)2495
#print(),if

su=5942           #5942-2495 = 3447  , su = 1000 * 5 + 100 * 9 + 10 * 4 + 2
a =3440
while True:
    if su % a != 2495:
        a = a+1
    else :
        break
print()
print(su % a)      

print('='*50)

while True:
    data=int(input('10000미만의수 입력>>> '))
    i = data // 1000
    j = (data-(1000*i)) // 100
    k = (data-(1000*i)-(100*j)) // 10
    l = (data-(1000*i)-(100*j)-(10*k))//1
    if data > 9999 :
        continue   
    else :
        print(l,k,j,i)
        break


    
    
        








# mylist = [ 5, 9, 4, 2]
# print(mylist)

# mylist.reverse()
# print(mylist)



