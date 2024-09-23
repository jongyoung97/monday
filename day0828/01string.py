#01string.py

#str(),len()

x= 'blue'
y= 1234
print(x+str(y))  #blue1234
print(x,y) #blue 1234 / ' , ' 사용하면 문자는 문자대로 , 숫자는 숫자대로 
print(f'{x}{y}') #blue1234
print(f'{x} {y}') #blue 1234
print('='*50)

msg='sakbf676 tbnwebasd'
print('길이',len(msg))
print('갯수',msg.count('s'))  #2 s가 몇개 잇는지 카운트해줌
print()

#kb글자 단어를 추출할려고 할 때 -> [시 : 끝+1]

print(msg[2:4]) #kb
