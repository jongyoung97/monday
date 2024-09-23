#5.py
new_list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(new_list)
new_list.append(100)
print(new_list)
new_list = new_list + [101 , 102]
print(new_list)
new_list.remove(3)
print(new_list)
del new_list[3]
print(new_list)
new_list.sort()
print(new_list)
new_list.sort(reverse=True)
print(new_list)
new_list.reverse()
print(new_list)
length = len(new_list)
print(len(new_list))
print(100 in new_list)
print(100 not in new_list)