#09dictreturn2.py
def score_procedure(sd):
    kor_list=[ ]
    eng_list=[ ]

    for data in sd.values():
        kor_list.append(data[0])
        eng_list.append(data[1])

    kor_hap=sum(kor_list)
    eng_hap=sum(eng_list)
    kor_avg = kor_hap//len(kor_list)
    eng_avg = eng_hap//len(eng_list)

    return kor_hap, eng_hap, kor_avg, eng_avg


score = {
    'kim': [100,60],
    'Lee': [90,77],
    'goo': [82,34]
}

a,b,c,d = score_procedure(score)
print('국어점수합계: ',a,'\n'
      '영어점수합계: ',b,'\n'
      '국어점수평균: ',c,'\n'
      '영어점수평균: ',d)