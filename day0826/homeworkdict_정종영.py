#homeworkdict.py

#김자바,이합격,박패스
#aaa bbb ccc kim lee goo
score_dict = dict()
score_dict = {
    '김자바' :[100,60],
    '이합격' :[90,77],
    '강감찬' : [82,34],
    '박이썬' : [82,42]
}
list_kor = []
list_eng = []

print()
for key in score_dict:
    print(key, sum(score_dict[key]), sum(score_dict[key])//2 )

'''
      총합 평균
김자바 160 80    
이합격 167 83
강감찬 116 58
박이썬 124 62
'''
print()
print('='*50)


