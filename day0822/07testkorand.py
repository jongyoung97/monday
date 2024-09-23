# 07testkor.py


#if 제어문 논리연산추가 and or 
#점심식사 후   

#선언=declare
kor, eng , hap = 0,0,0 
avg = 0.0 
message ='안내문' 

#처리 연산,if,반복
kor = 65
eng = 50
hap = kor + eng
avg = hap//2 

#if조건 and 평균 70점부터, 각과목 60점부터 합격
#if조건 or 평균 70점부터, 각과목 60점부터 합격
'''
if  (avg >= 70 and kor >= 60 and eng >= 60) :
    message = '축합격'
else :
    message = '재시험'
'''
if  (avg >= 70 or kor >= 60 or eng >= 60) :
    message = '축합격'
else :
    message = '재시험'

#문제해결2]
#평균 100~90 A, 89~80 B, 79~70 C, 69~60 D, 59~0 F
if avg >= 90 :
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
else:
    grade = 'F'

#출력 
print('국어 ', kor)
print('영어 ', eng)
print('합계 ', hap)
print('평균 ', avg)
print('결과 ', message)





