#04upper.py
#교재 86p~90p
msg='btskpchERry'

print(msg.upper()) #BTSKPCHERRY  대문자
print(msg.lower()) #btskpcherry  소문자
print() 
print('k=' ,msg.find('k')) #k= 3  위치
print('t=', msg.index('t')) #t= 1 위치

msg='asdjhqwqkd'
print('k=',msg.find('k')) #k= 8
print('q=',msg.index('q')) #q= 5
pos=msg.find('z')
if pos == -1:
    pass
    print('원하는 키워드가 없습니다')
else:
    pass
    #있으면 출력을 하거나 조작,연산처리
print('='*50)