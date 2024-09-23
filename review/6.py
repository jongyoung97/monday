#6

new_list = [0,1,2,3,4,5,6,7,8,9]

print("0번째 원소 :", new_list[0])
print("1번째 원소 :", new_list[1])
print("4번째 원소 :", new_list[4])
print("0~3번째 원소 :", new_list[0:3])
print("4~9번째 원소 :", new_list[4:9])
print("2~3번째 원소 :", new_list[2:3])
print("3번째 부터 모든 원소 :", new_list[3:])
print("5번째 부터 모든 원소 :", new_list[5:])
print("9번째 부터 모든 원소 :", new_list[9:])
print("1번째 이전의 모든 원소 :",new_list[:1])
print("7번째 이전의 모든 원소 :",new_list[:7])
print("9번째 이전의 모든 원소 :",new_list[:9])
print('끝에서 |-1|-1번째 이전의 모든 원소 :', new_list[:-1])
print('끝에서 |-1|-1번째 부터 모든 원소 :', new_list[-1:])
print('끝에서 |-2|-1번째 이전의 모든 원소 :', new_list[:-2])
print('끝에서 |-2|-1번째 부터 모든 원소 :', new_list[-2:])
new_list = ['텍스트', 0, 1.9, [1,2,3,4], {'서울': 1, '부산': 2, '대구': 3} ]
print(new_list)
print('Type of new_list[0] :', type(new_list[0]))
print('Type of new_list[1] :', type(new_list[1]))
print('Type of new_list[2] :', type(new_list[2]))
print('Type of new_list[3] :', type(new_list[3]))
print('Type of new_list[4] :', type(new_list[4]))
new_list = [[0,1,2],[2,3,7],[9,6,8],[4,5,1]]
print('new_list :', new_list)
print('new_list[0] :', new_list[0])
print('new_list[1] :', new_list[1])
print('new_list[2] :', new_list[2])
print('new_list[3] :', new_list[3])
new_list.sort()
print(new_list)

new_list.sort(key=lambda elem: elem[2])
print('new_list ;', new_list)