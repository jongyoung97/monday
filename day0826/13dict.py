#13dict.py

mysite = dict()


mysite['naver'] = 'www.naver.com'
mysite['kakao'] = 'www.kakao.net'
mysite['ibm'] = 'www.ibm.com'
mysite['google'] = 'www.google.org'

print(mysite['kakao'])
print(mysite.get('kakao'))
print()

print(mysite['kakao']) #키값을 잘못 기술했을때 ->error
print(mysite.get('kako')) #키값을 잘못 기술했을때 -> None 으로 출력
print()

mya='naver' in mysite
myb='navr' in mysite

print(mya) # ->True로 출력
print(myb) # ->False로 출력





 


      
