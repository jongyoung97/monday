#07testcopy.py

import math
import random
import re
import os.path
import sys
import pickle

import time
import datetime

import copy

apple = 'macos'
my = apple
print(apple)
print(my)

data = [ 11, 22, 33 ]
#양쪽적용 mydb = data
mydb = copy.deepcopy(data)

data[0] = 789
print('원본', data)
print('복사', mydb)



print()

