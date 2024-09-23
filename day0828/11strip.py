#10replace.py

#문자,문자열변경 replace(구(변경대상),신(변경))
#문자,문자열 공백제거

msg = '    It is a best Python    '

print(msg.replace(' ',''))    #ItisabestPython
print()
for k in range(len(msg)) : 
    if msg[k] not in ' ':
        print(msg[k],end ='') #ItisabestPython
print()
mylist = msg.split() #split(x) 자동공백제거 리스트화 ['It', 'is', 'a', 'best', 'Python']
print(mylist)        


x= 'aaa '
y= 'yyy'
# print(msg)     #    It is a best Python    
# print(x+msg+y) #aaa    It is a best Python    yyy
# print(x+msg.lstrip()+y) #lstrip 왼쪽공백제거
# print(x+msg.rstrip()+y) #rstrip 오른쪾공백제거 








print()