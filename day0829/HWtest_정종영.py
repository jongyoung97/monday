#test.py

#day0829 폴더 오픈
#문제1 변수사용(name,age,gender),키보드입력,나이는숫자
#문제2 나이 입력범위 20~70사이
  # 조건 20미만 청소년 1~19 20~30청년 31~65중년 66이상노년
#문제3 남자/남/man입력 ->True 출력 / 여자/여/woman로 입력하면 False출력
# print(홍길동)
# print(34,'쳥년')
# print(남자)

def age():
    while True:
        age      = int(input('나이를 입력하십시오>>>: '))
        if  age<=70:
            if age<20:
                generation = '청소년'
            elif age <=30:
                generation = '청년'
            elif age <= 65:
                generation = '중년'
            else:
                generation = '노년'
            return generation        
        else:
            print('나이 입력범위는 70세까지입니다. 다시 확인해주세요.')

def gen():
    while True:
        gender = str(input('성별을 입력하십시오>>>: '))
        if gender in ['남자','남','man']:
            return '남성' , True
        elif gender in ['여자','여','woman']:
            return '여성' , False
        else:
            print(" '남자','남','man' 또는 '여자','여','woman'으로 입력해주세요." )




name     = str(input('이름을 입력하십시오>>>: '))
age_def = age()
gender_def = gen()
print('나이: ', age_def, '\n',
      '이름: ', name, '\n',
      '성별: ', gender_def
) 
print()


     
   
 



        
