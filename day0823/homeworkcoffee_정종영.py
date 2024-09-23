#homeworkcoffee.py

money, sel = 0 , 9 

money = int(input('금액입력>>> '))
while True : 
    print('----☕----')
    print('')
    data = (input('1.커피(250) 2. 코코아(200) 3. 반환  9:종료>>> '))
    sel = int(data)
    if sel == 9:
        print('종료하였습니다.')
        break
    elif sel == 1:
        data_2 = input('몇 잔 주문하시겠습니까>>> ')
        sel_2 = int(data_2)
        if (sel_2)*(250) < money :
            print(sel_2,'잔이 주문되었습니다.')
        else :
            print('금액이 부족합니다.')    
            continue
        money = money - (250*(sel_2))
        break
    elif sel == 2:
        data_2 = input('몇 잔 주문하시겠습니까>>> ')
        sel_2 = int(data_2)
        if (sel_2)*(200) < money :
            print(sel_2,'잔이 주문되었습니다.')
        else :
            print('금액이 부족합니다.')    
            continue
        money = money - (200*(sel_2))
        break
    elif sel == 3:
        print('반환되었습니다.')
        money = money
        break
    else:
        print('주문번호를 정확히 선택하세요')



#if~elif~if 제어문으로 커피값계산    

print()
print('거스름돈은 ' , money , '입니다')

