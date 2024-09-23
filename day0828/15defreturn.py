#15defreturn.py

'''
파이썬에서 함수 정의 시작 키워드 def함수이름():
사용자정의 함수 매개인자 
사용자정의 함수에서 처리후 외부에 값을 줄 때 return값
사용자정의 함수 매개인자+리턴값
'''

def book():
    title = '몽블랑'  #지역변수=local variable=휘발성
    return title

def pay():
    m = 7800
    return m

def blue():
    color = 'dark'
    #리턴값이 없이 출력하면 None이라고 에러뜸
    return color

def main():
    print("main 함수")
    data = book()
    value = pay()
    print("책 제목 ", data)   #책 제목  몽블랑
    print("책 가격 ", value)  #책 가격  7800
    print("책 제목 ", book()) #책 제목  몽블랑
    print("책 가격 ", pay())  #책 가격  7800
    print("블 루",    blue())

if __name__ == '__main__': #생략가능
    main()    
    
    
    
