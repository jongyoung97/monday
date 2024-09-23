#7

new_dict = {'마케팅팀': 98, '개발팀':78, '데이터분석팀': 83, '운영팀': 33}
print(new_dict)
print(new_dict['마케팅팀'])
new_dict["미화팀"]=55
print(new_dict)
new_dict['데이터분석팀']=100
print(new_dict)
new_dict['데이터분석팀'] = {'등급': 'A'}
new_dict['운영팀'] = ['A']
new_dict['개발팀'] = '재평가'
new_dict[0] = '오타'
print(new_dict)
 