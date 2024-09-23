score_dict = {
    "김자바": [100, 60],
    "이합격": [90, 77],
    "kang": [82, 34],
    "park": [90, 34],
}

list_kor = []
list_eng = []

# 김자바 160 80
# 이합격 167 83
# 강감찬 116 58
# 박이썬 124 62

for name, score in score_dict.items():
    score = score_dict.get(name)
    print(name, " : ", score[0] + score[1], ", ", int((score[0] + score[1]) / 2))

    list_kor.append(score[0])
    list_eng.append(score[1])

print("kor list : ", list_kor)
print("eng list : ", list_eng)

print()
print()
#
score_dict = {
    "kim" : [100,60],
    "lee" : [90, 77],
    "kang": [82,34] ,
    "park": [90,34]
}
list_kor=[]
list_eng=[]

for name,score in score_dict.items():
    score = score_dict.get(name)
    print(name, ":", score[0]+score[1],",",int((score[0]+score[1])/2))

    list_kor.append(score[0])
    list_eng.append(score[1])

print("korean score list: ",list_kor)
print("English score list: ", list_eng)    

