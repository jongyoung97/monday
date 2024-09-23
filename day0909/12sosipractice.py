import os
import pandas as pd
import cx_Oracle

import oracledb
import time

config = {
    'user' : 'system',
    'password' : '1234' ,
    'dsn' : '192.168.100.58:1521/xe'
}
