# HWmenu.py
# 예외처리 try: ~~~ except: ~~~ 생략
import time
import sys  #프로그램종료 sys.exit()
from datetime import datetime #datetime.now()


path = 'C:/Mtest/menu.txt'  #\->/로 바꿔야함

#첫 번째 HWmenu.py문서를 class화 
#두 번째 menuInsertnew 할 때만 일반text파일저장
class EmpMenu :
    num,su,sel = 0,0,0
   
    def __init__(self) :
        self.menu = dict()
        self.flag = True
        self.path = 'C:/Mtest/menu.txt'
        self.menuFileCreate()

    def menuInsertNew(self):
        name = input('이름입력key>>>')
        price = input('가격입력value >>>')
        self.menu[name] = price
        print(name, '등록 성공했습니다')

    def menuAllprint(self):
        for k,v in self.menu.items():
            print( k ,' ', v)
        print()

    def menuEditupdate(self):
        name = input('편집대상 키값 입력>>> ')
        if self.menu.get(name) == None:
            print('편집대상 딕트가 key 없습니다')
        else:
            price = input('변경가격 재입력value >>>')
            self.menu[name] = price 
            print(name, '가격수정편집 성공했습니다')
    
    def menuDelete(self):
        name = input('삭제대상 키값 입력>>> ')
        if self.menu.get(name) == None:
            print('삭제대상 딕트가 key 없습니다')
        else:
            self.menu.pop(name)
            print(name, '데이터삭제 성공했습니다')
            time.sleep(0.3)
            for k,v in self.menu.items():
                print( k ,' ', v)

    def menuFindsearch(self):
        key = input('조회검색 key 입력>>> ')
        if self.menu.get(key) == None:
            print(key, '데이터가 없습니다')
        else:
            print(key, self.menu[key],'데이터 조회성공했습니다')

    def menuExit(self):
        print('딕트처리를 종료합니다\n')
        sys.exit

    def menuFileOpen(self):
        try:
            with open(path, 'r', encoding='UTF-8') as file:
                print(file.read())
        except FileNotFoundError:
            print('파일이 존재하지 않습니다.')
        except IOError:
            print('파일을 읽는 중 오류가 발생했습니다.')

    def menuFileCreate(self):
        with open(path,'w',encoding='UTF-8') as file:
            file.write('')
        print(f"{path} 파일이 생성되었습니다.")    



dt = datetime.now()
print('처리 날짜 ', datetime.now())
print('처리날짜 ', dt)
print()

#------------------------------------------------------------------

emp_menu = EmpMenu()

while emp_menu.flag:
    print()
    num=int(input('1등록 2출력 3수정 4삭제 5조회 6파일열기 9종료>>'))
    if   num == 9:  emp_menu.menuExit()       
    elif num == 1:  emp_menu.menuInsertNew()
    elif num == 2:  emp_menu.menuAllprint()
    elif num == 3:  emp_menu.menuEditupdate()
    elif num == 4:  emp_menu.menuDelete()
    elif num == 5:  emp_menu.menuFindsearch()
    elif num == 6:  emp_menu.menuFileOpen()
    else: print('처리번호를 잘못 입력하셨네요\n')



print()


