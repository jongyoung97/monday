#05tuple.py
#튜플( )표식
#튜플은 리스트와 비슷, 수정불가

pos = ('홍대', 126.72345, 37.0802, '홍대', 29.345354)
print(pos)
#튜플 for반복문으로 출력
for k in range(len(pos)):
    print(pos[k],end='\t')
print()
print()
print('='* 50)
for i , v in enumerate(pos):  #enumerate는 나열의 의미
    print(i,':', v)


#튜플 append(),insert()함수 지원안됨,수정불가
print()