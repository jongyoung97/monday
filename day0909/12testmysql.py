#12testmysql.py

#오라클대신 mysql데이터베이스

#import cx_Oracle    오라클임포트
import pymysql
import time
configOracle = {
    'user' : 'system',
    'password' : '1234',
    'dsn' : '127.0.0.1:1521/xe'
}

config={
    'host' : '127.0.0.1' ,
    'user' : 'root' ,
    'password' : '1234' ,
    'database' : 'naver' , 
    'port' : 3306
}




CN = pymysql.connect(**config)
cursor = CN.cursor()

msg = "select * from test"
cursor.execute(msg)
rows = cursor.fetchall()
print('cursor.fetchall()타입',type(rows))

for r in rows:
    print(r[0],r[1],r[2],r[3])



def testSelectAll() :
    msg = "select * from test"
    cursor.execute(msg)
    rows = cursor.fetchall()

    for r in rows:
        print(r[0],r[1],r[2],r[3])

def testInsert():
    dcode = int(input('코드입력 >>>'))
    message = f"select count(*) cnt from test where code = {dcode}"
    cursor.execute(message)
    cnt = cursor.fetchone()[0]
    if cnt != 0:
        print(dcode, '코드데이터는 이미 등록된 코드입니다.')
        print('정확한 code를 입력하세요')
        return
    else:
        dname = input('name 입력 >> ')
        dhit = int(input('hit 입력>> '))

        msg = f"insert into test values({dcode},'{dname}',{dhit},now())"
        cursor.execute(msg)
        CN.commit()
        print(dcode ,'저장성공')
        
testInsert()
#testSelectAll()
print()
print()


# msg = "select * from test "
# cursor.execute(msg)
# rows = cursor.fetchall()

# for r in rows:
#     print(r[0], r[1], r[2], r[3] )
# print('레코드갯수 ', len(rows))
