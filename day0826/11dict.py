#11dict.py

mysite = dict()


mysite['naver'] = 'www.naver.com'
mysite['kakao'] = 'www.kakao.net'
mysite['ibm'] = 'www.ibm.com'

#for반복문
for key in mysite:
    print(key, ':', mysite[key])


print()
print()

for i,k in enumerate(mysite) :
    print(i,':',mysite[k])

print()
print()

for k,v in mysite.items():
    print(k, ':', v)





# dict = 딕트 k:v    


      
