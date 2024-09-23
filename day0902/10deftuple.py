#10deftuple.py

def my_hap(*args):
    print('*args타입', type(args))
    hap = 0 
    for num in args:
        hap  = hap + num
    return hap

def my_hap2(args):
    return hap

def mycal():
    pass


a,b,c,d,e = 1, 2, 3, 4, 5
ret = mycal(a,b,c,d,e)


mylist= [1,2,3,4]
msg = my_hap(mylist)
print ('리스트합계 :',msg)