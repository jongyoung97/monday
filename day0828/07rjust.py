#07rjust.py

for x in range(1,6,1):
    pass
    #print(f'{x} * {x} = {x*x}')
    print(x,'*',x,'=',(x*x))
print()
for x in range(1,6,1):
    #print(x,'*',x,'=',(x*x))
    print(x,'*',x,'=',str(x*x).rjust(5))
print()
for x in range(100,106,1):
    print(x,'*',x,'=',str(x*x).rjust(6)) 
print()
for x in range(1,6,1):
    print(x,'*',x,'=',str(x*x).zfill(5)) #zero(0)으로 채우는    
        










print()