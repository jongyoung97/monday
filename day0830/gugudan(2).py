import time

def toptitle():
    print()
    print('mygugudan 보고서')
    print('='*50)

def endtitle():
    print()
    print('='*50) 


def guguinput():
    #반드시 리턴처리
    dan = 1 #지역변수
    try:
        dan= int(input('단입력>>> '))
    except Exception as ex:
        print('에러이유', ex)
    return dan


def guguoutput(dan):
    for k in range(1,10,1):
        print(f'{dan} *{k}={dan*k}')
        time.sleep(0.5)



def main():
    toptitle()
    data = guguinput()
    guguoutput(data)
    endtitle()

main()        



