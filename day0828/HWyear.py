#HWyear.py

day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = int(input("year>>> "))
month = int(input("month>>> "))
#date = int(input("date>>> "))
#튜플,문자열 없이 입력데이터로 if제어문
#if 제어문 or / and 중첩 if를쓰던
'''
윤년 기준
1. 4의배수
2. 100의 배수가 아닌 4의 배수
3. 400의 배수
'''

#2024 2 입력하면 윤년입니다.
#2024년 2월 29일/2020년 2월 29일
#2021년 2022년 2023년은 2월 28일

if (year % 4 == 0 or (year % 100 !=0 and year % 4 ==0) or (year % 400 == 0)):
    year = '윤년'
    print(year,'년은 윤년입니다.')
else :
    year = '평년'
    print(year,'년은 윤년이 아닙니다. 평년입니다.')

if  year == '윤년' and month == 2:
    day = 29
    month = '29'
ellf month == (1 or 3 or 5 or 7 or 8 or 10 or 12): 
    day = 31
else:

print(year,'년',month)          