#03play.py

import time
import game #물리적인 파일이름만 명시 파일game.py를 끌고옴

print('03play.py')
time.sleep(0.5)

print(game.user_id)
print(game.user_pwd)

time.sleep(0.5)
game.terran()

time.sleep(1)
game.LG('냉장고')

time.sleep(1)
miter = game.siuuu()
print('점프높이 ',miter)
print('점프높이 ',game.siuuu(),'m')




# game.py문서
# 전역변수 user_id, user_pwd
# 함수     terran() LG(lg) LG(lg) 리턴값있음





print()