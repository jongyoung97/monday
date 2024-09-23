#03listsearch.pt

data = [7,8,9,1,2]

find = int(input('데이터찾기>>> '))
if find in data :
    print(find, '검색 성공 !!')
    print('결과 ', find in data)  #True
else : 
    print('결과 ', find in data)  #False
    print(find, '검색 실패 !!')
#데이터있으면 성공메세지 , 데이터출력
#데이터없으면 실패메세지
#for 대표변수 in range(5):
#list에서 데이터 찾기 할 때 in 키워드 사용