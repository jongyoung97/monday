#06testif.py


#선언=declare
kor , eng , hap =0,0,0 #변수초기화
avg= 0.0
message = '안내문' #변수초기화 / 합격여부
grade = 'F' #학점


kor = 90
eng = 96           
hap = kor + eng
avg = hap//2

if avg>=70 : 
    message = '축합격'
else : 
    message = '재시험'


if avg>=90 : 
    grade = 'A'
elif avg >=80 :
    grade = 'B' 
elif avg >=70 :
    grade = 'C'        
elif avg >=60 :
    grade = 'D' 
else: 
    grade = 'F'

#출력
print('02testif.py문서')
print('국어 ',kor)
print('영어 ',eng)
print('합계 ',hap)
print('평균 ', avg)
print('학점 ', grade)
print('결과 ', message)
print( '🍓' *30)
print()