#01testlist.py

data = [#3행 * 4열
        [1,2,3,4,6,7],
        [5,6,7,8],
        [9,10,11,12,13,4]
    ] 
for k in data :
    print(k, end = ' ')
    
print()
print('리스트 길이', len(data))

#실제길이 4개 접근index [0]~[3]
#            접근index [0]~[-2][-1] 

# for j in len(range(data)) :
#     pass

#range(len())

# print('='*50)
# for a in range(0,3,1):
#     for b in range(0,4,1):
#         print(data[a][b] ,end = '\t') 
#     print()
    
print('='*50)    

for k in range(len(data)):
    for j in range(len(data[k])):
        print(data[k][j], end = '\t')
    print()   
print()
    