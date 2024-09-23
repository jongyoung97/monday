#02split.py

url='www.google.com'
print(url)

myret = url.split('.')
print(myret)  #list화  ['www', 'google', 'com']
print(url.split('.'))

connect = ';'
print(connect.join(url)) #w;w;w;.;g;o;o;g;l;e;.;c;o;m
connect_2 = ' '
print(connect_2.join(url)) #w w w . g o o g l e . c o m