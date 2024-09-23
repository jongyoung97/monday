#homeworkdictex.py


score_dict = dict()
score_dict = {
    '김자바' :[100,60],
    '이합격' :[90,77],
    '강감찬' : [82,34],
    '박이썬' : [82,42]
}
list_kor = []
list_eng = []
for data in score_dict.values():
    list_kor.append(data[0])
    list_eng.append(data[1])
print(list_kor)
print(list_eng)

hap_kor =sum(list_kor)
hap_eng =sum(list_eng)
print(hap_kor,hap_kor//2)
print(hap_eng,hap_eng//2)    