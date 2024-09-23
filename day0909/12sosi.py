# 12sosi.py

# 오라클 sosi테이블 + 파이썬
import os
import pandas as pd
import cx_Oracle  

# pip install oracledb 
import oracledb     
import time
       

config = {
    'user' : 'system',
    'password' : '1234',
    'dsn' : '127.0.0.1:1521/xe'
}


# conn = oracledb.connect(**config) #오류
# conn = oracledb.connect(user='system', password='1234', dsn='127.0.0.1:1521/xe') #오류
conn = cx_Oracle.connect(**config) 
cursor = conn.cursor()
#print('config매개인자타입 ', type(config))
print("database version: ", conn.version)
print("oracle connect ok success")
print()


def sosiInsert():
    print('\nsosi테이블 신규등록 처리 ')
    while True:
        dcode = int(input('코드 입력>> '))
        cursor.execute('select count(*) from sosi where code = {dcode}')
        count = cursor.fetchone()[0]

        if count > 0:
            print("이미 존재하는 코드입니다.다시입력해주세여.")
        else:
            break
    message = "select"
    dname = input('이름 입력>> ')
    dtitle = input('제목 입력>> ')
    dsal = int(input('급여 입력>> '))
    msg = f"insert into sosi values({dcode},'{dname}','{dtitle}',{dsal}, sysdate, 'D')"    
    cursor.execute(msg)
    conn.commit()
    print(dcode , ' 저장 성공했습니다')
    time.sleep(1)


def sosiSelectAll():
    msg = "select * from sosi order by code"
    cursor.execute(msg)
    rows = cursor.fetchall()
    #print('rows타입 ', type(rows))
    print()

    print('%s\t %s\t %10s\t  %4s\t %6s\t %s' %('코드','이름','제목','급여','날짜','등급') )
    for r in rows:
        # print(r[0],r[1],r[2],r[3],r[4],r[5])
        print('%4d\t %10s\t %10s\t  %4d\t %6s\t %s' %r) 
    print('전체데이터 갯수:' , len(rows))
    print('- ' * 40)
    time.sleep(1)

    #   CODE NAME  TITLE   SAL WDATE    GRADE
    #   ------ ----------- ------ ----- --------
    #  3300 three                cake                     96 24/09/06 D
    #  2200 kim                  two                      92 24/09/06 D


def sosiSelectTitle():
    pass
    print('제목데이터 like조회하세요 ')


def sosiDelete():
    codedelete = int(input('삭제할 코드 입력>>> :'))
    check = input('삭제하시겠습니까? (y/n): ')
    if check == 'y':
        cursor.execute('delete from sosi where code = :code',{'code':codedelete})
        conn.commit()
        print(codedelete,'코드가 삭제되었습니다.')
    else :
        print('취소되었습니다.')
    



sosiSelectAll()
sosiInsert()
time.sleep(0.5)
sosiSelectAll()
sosiDelete()
print()
