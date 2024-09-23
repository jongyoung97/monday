#02deftuple.py



def my_hap(*args):
    print('*arges타입', type(args))  
    hap = 0 
    for num in args:
        hap = hap + num
    return hap    



# data = my_hap(6,11,24,7,3,21,39,45)
# print('데이터 결과 ',data)
# print('데이터 결과 ',my_hap(6,11,24,7,3,21,39,45))
print()    
print('='*50)
    
mylist = [6,11,24,7 ]     #list는 수정가능, 쉽게 데이터를 추가 할 수 있다.
mytuple = (5,10,23,6 )    #tuple은 수정x , 쉽게 데이터를 추가 할 수 없다.
mylist[1] = 54
print(mylist) #[6, 54, 24, 7]

mytuple[1] = 94 #에러발생 -> 수정이 안돼~
print(mytuple)