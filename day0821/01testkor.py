#선언부분 = 변수데이터 초기화
#변수 초기화 = 기본값 대입=할당
#변수이름명명 첫글자 소문자 시작( 첫글자 숫자 비권장, 특수문장비권장 )
#변수이름 명명 첫글자 소문자 my_kor, my_sum, my_avg, team_kor,,,
title = '데이터점수'
name = '길동'
kor = 90
eng = 85
hap = 0 #sum() 이라는 내장함수가 존재하기에 sum키워드는 금지 
avg = 0.0 

#로직 = 처리담당 연산(산술,관계,논리) , 연산결과 조건 (if), 반복문(for,while)

hap = (kor + eng) #사칙연산 + - * /몫 %나머지값
avg = hap/2    

#처리결과 출력 print( 'ㅁㅁ', data ) 
#print()내장함수는 라인개행포함 <br>역할

print('이름=',name)
print('국어=', kor)
print('영어=', eng)
print('총점=', hap)
print('평균=', avg)
print()