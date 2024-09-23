#test.py

#day0829 폴더 오픈
#문제1 변수사용(name,age,gender),키보드입력,나이는숫자
#문제2 나이 입력범위 20~70사이
  # 조건 20미만 청소년 1~19 20~30청년 31~65중년 66이상노년
#문제3 남자/남/man입력 ->True 출력 / 여자/여/woman로 입력하면 False출력
# print(홍길동)
# print(34,'쳥년')
# print(남자)


def gen():
    if gender_2 == '남성':
        return True
    if gender_2 == '여성':
        return False




name     = str(input('이름을 입력하십시오>>>: '))

# gender   = str(input('성별을 입력하십시오>>>: '))

while True:
    age      = int(input('나이를 입력하십시오>>>: '))
    if age < 20 :
        generation = '청소년'
        break
    elif 20 <= age <=30 :
        generation = '청년'
        break
    elif 30 < age <= 65 :
        generation = '중년'
        break
    elif 70>=age >= 66 :
        generation = '노년'
        break
    else:
        print("나이 입력범위는 20~70세까지입니다. 다시 입력해주세요.")    

print('나이: ',age, generation)        

while True:
    gender   = str(input('성별을 입력하십시오>>> : '))
    if gender == '남자'or'남'or'man':
        gender_2 = '남성'
        break
    elif gender == ('여자'or'여'or'woman'):
        gender_2 = '여성'
        break
    else:
        print('남자,남,man 또는 여자,여,woman 으로 입력해주세요.')

print('성별: ',gender_2,gen())
print(name)
print([name,age,gender_2])





        
