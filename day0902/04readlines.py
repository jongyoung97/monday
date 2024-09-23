# 04readlines.py

# import file~~~    (안해도됨)
#pathName = '경로/파일.txt'
# 리턴변수 = open(파일, 모드w/r/a, 인코딩)
# 리턴변수.close()
# open()대신 with open( ) as 
# ff = open(1,2,3) 대체 with open(1,2,3) as ff

#파일읽기 read(),readline(),readlines()

file = 'C:/Mtest/kakao.txt'
with open(file,'r',encoding='UTF-8') as myfile:
    for data in  myfile.readlines():
        print(data, end='')
        
        
      
    


print(file,'파일읽기성공했습니다')
print()





