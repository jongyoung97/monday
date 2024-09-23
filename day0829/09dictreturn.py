#09dictreturn.py


#함수의 리턴값을 1개이상 처리하는법
#함수의 매개인자 1개이상처리 (*args)
def score_procedure(score):
    kor_list=[ ]
    eng_list=[ ]
    #각 리스트에 국어점수,영어점수추가
    for name, scores in score.items():
        kor_list.append(scores[0])
        eng_list.append(scores[1])

    kor_sum=sum(kor_list)
    eng_sum=sum(eng_list)
    kor_avg=kor_sum // len(kor_list) 
    eng_avg=eng_sum // len(eng_list)

    return [kor_sum,eng_sum,kor_avg,eng_avg]    
    
    #return 국어점수합계, 영어점수합계, 국어평균, 영어평균
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