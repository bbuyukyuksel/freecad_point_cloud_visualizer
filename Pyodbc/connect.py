import pyodbc
import time
import datetime

#tcp:
server = 'server'
database = 'database'
username = 'username'
password = 'password'
table_name = 'tablename'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

query = f'exec sp_columns [{table_name}]'
cursor.execute(query)
row = cursor.fetchall()

table_names = [i[3] for i in row]
FORMAT = '{:10} {:^20} {:^20} {:^20} {:7}|{:7}|{:7}|{:7}|{:7}|{:7} : {:12},{:12},{:12} [{}]'

header = FORMAT.format(*table_names)
print(header)
print('_'*len(header))
time.sleep(0)

now = datetime.datetime.now()
row = cursor.fetchone()

#cursor.execute("SELECT * FROM CADU  WHERE mech_name LIKE '12H00-50375-AA%'")
#cursor.execute("SELECT * FROM CADU ORDER BY id DESC")
#cursor.execute("SELECT TOP 10 * FROM CADU ORDER BY id DESC")
cursor.execute("SELECT * FROM CADU WHERE Tarih = '2019-05-24 10:37:17'")

row = cursor.fetchone()
bg = ('\033[01;47m',' ','\033[00m')

file_mech_db = open('../mech.db', 'w')

while row:
    row = tuple(map(str, row))
    row = tuple(map(str.strip, row))
    text = FORMAT.format(*row) 
    file_mech_db.write(text + '\n')
    print(*bg, text,*bg)
    print('\033[01;42m',' '*(len(text)+6),'\033[00m')
    row = cursor.fetchone()
print('Term Time:', str(datetime.datetime.now() - now))
