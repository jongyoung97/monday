#1replace.py

#문자,문자열변경 replace(구(변경대상),신(변경))
#문자,문자열 공백제거

info = 'My best friend ronaldo'
myret1= info.replace('best','Goat')
print(myret1)
myret2= info.replace(' ','')
print(myret2)

print()
msg = '    It is a best Python    '
x= 'aaa'
y= 'yyy'
print(msg)     #    It is a best Python    
print(x+msg+y) #aaa    It is a best Python    yyy
print(x+msg.lstrip()+y) #lstrip 왼쪽공백제거
print(x+msg.rstrip()+y) #rstrip 오른쪾공백제거 
print(x+msg.strip()+y)  #좌우 공백제거







print()