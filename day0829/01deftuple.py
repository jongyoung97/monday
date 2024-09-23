#01deftuple.py

def data_hap(x,y,z,a,b,c,f):
    #숫자합계구해서 리턴처리
    hap = x+y+z+a+b+c+f
    return hap

def my_hap(*args):
    print('*arges타입', type(args))  #//*arges 타입 'tuple'
    hap = 0 #생략하면 에러발생
    for num in args:
        hap = hap + num
    return hap    



data = my_hap(6,11,24,7,3,21,39)
print('데이터 결과 ',data)
print('데이터 결과 ',my_hap(6,11,24,7,3,21,39))

print()    
print('='*50)
    
total = data_hap(6,11,24,7,3,21,39)
print('계산처리 합계 ', total)
print('계산처리 합계 ', data_hap(6,11,24,7,3,21,39))
# print()
'''
def data_hap(x,y,z):
    #숫자합계구해서 리턴처리
    print('x_id타입',id(x))
    print('y_id타입',id(y))
    print('z_id타입',id(z))

    print('x타입', type(x))
    print('y타입', type(y))
    print('z타입', type(z))
    
    
data_hap(6,9,21)
'''