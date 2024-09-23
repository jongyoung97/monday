# gugudan . py

# 함수 4개작성 
# 시작 진입 호출 main
# main함수 title()호출, gugudaninput(), output(), title()  호출
# 출력할 때 time.sleep(0.4)
# 입력시 input() 이용, 형변환
import time

def toptitle():
    print()
    print('mygugudan 보고서')
    print('='*50)

def endtitle():
    print()
    print('='*50)    

def gugudaninput():
    while True:    
       dan = int(input("단을 입력하세요>>>: "))
       if dan < 1 :
            print("1이상의 수를 입력해주세요.")
       else:
            break
    return dan
            

def gugudanoutput():
    for k in range(1,10,1):
        print('구구단: ',dan,'*',k,'=',(dan * k))

    
    




def main():
    toptitle()
    gugudaninput()    #리턴값필수
    gugudanoutput()   #매개인자
    endtitle()    