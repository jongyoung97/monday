#16sortselect.py

print()

a=[4,7,5,1,2]
for i in range (4) :
    for j in range(i,5):
        if a[i]>a[j]:
            temp = a[i]
            a[i]= a[j]
            a[j]=temp
    print(a)

# [1, 7, 5, 4, 2]
# [1, 2, 7, 5, 4]
# [1, 2, 4, 7, 5]
# [1, 2, 4, 5, 7]