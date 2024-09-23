# 2file.py

# import file~~~    (안해도됨)
#pathName = '경로/파일.txt'
# 리턴변수 = open(파일, 모드w/r/a, 인코딩)
# 리턴변수.close()
# open()대신 with open( ) as 
# ff = open(1,2,3) 대체 with open(1,2,3) as ff
import time


#파일읽기처리
pathName = 'C:/Mtest/sample.txt'
rfile = open(pathName, 'r', encoding='UTF-8')
data = rfile.read()
#data = rfile.readline()
print(data)
print('='*50)
rfile.close()
time.sleep(0.5)
print(pathName,'파일읽기성공했습니다\n')
print()


print('-' * 70)
time.sleep(1)
fileName = 'C:/Mtest/kakao.txt'
with open(fileName,'r',encoding='UTF-8') as myfile:
    my = myfile.read()
    print(my)
    

time.sleep(0.5)
print(fileName,'파일읽기성공했습니다')
print()





