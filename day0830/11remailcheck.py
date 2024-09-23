#11remailcheck.py

import re


def email_check(email):
    pass
    #re.findall(' .[a-z]{2,}',)
    #re.findall(' .[a-z]{2,}',)

email_check("kim@gmail")    #.org .kr .com .net
email_check("kim_gmail.net") # @포함여부
email_check("$^kim") #첫글자특수문자포함
email_check("kim@gmail.net") #올바른이메일