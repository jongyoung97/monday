# 05ospath.py

# import file~~~    (안해도됨)
#pathName = '경로/파일.txt'
# 리턴변수 = open(파일, 모드w/r/a, 인코딩)
# 리턴변수.close()
# open()대신 with open( ) as 
# ff = open(1,2,3) 대체 with open(1,2,3) as ff

#파일읽기 read(),readline(),readlines()
import sys
import os.path


save_path = os.path.abspath('C:/Mtest/my.txt')
try:
    pass
    if not os.path.exists(save_path):
        print(save_path , '대상파일이 존재하지 않습니다.') #파일저체가 없으면 경고
        #sys.exit()
    else:
        pass 
except Exception as EX:
    print('에러이유 확인',EX)

print()


