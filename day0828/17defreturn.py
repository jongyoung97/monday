#17returnargument.py

'''
파이썬에서 함수 정의 시작 키워드 def함수이름():
사용자정의 함수 매개인자 
사용자정의 함수에서 처리후 외부에 값을 줄 때 return값
사용자정의 함수 매개인자+리턴값
'''

def book():       #매개인자x,리턴값0
    title = '몽블랑'  #지역변수=local variable=휘발성
    return title

def pay():        #매개인자x,리턴값0
    m = 7800   
    return m

def myCal(x,y,z): #매개인자o,리턴값o
    total = x + y + z
    avg = total//3
    #3개 데이터를 받아서 계산처리후 최종 값을 함수에 놓아줄거야
    return avg

#myCal함수호출 90 85 64
data=myCal(90,80,64)
print('myCal함수 호출 성공', data)

#myCal함수 리턴값이 있으면 변수 = 함수이름
#myCal함수 리턴값이 있으면 print(함수이름())




# def gugudan(name,dan):
#     pass
# #name출력 반복문dan출력

# def blue():       #매개인자x, 리턴값x
#     color = 'dark'
   
# def main():
#     print("main 함수")
   
# if __name__ == '__main__': #생략가능
#     main()    
    
    
    
