import cx_Oracle
import csv
import random
#csv파일을 처리해서 넣어보자.

def connector():
    dsn = cx_Oracle.makedsn("localhost", 1521, service_name="xe")
    con = cx_Oracle.connect(user="MYDB", password="admin1234", dsn=dsn,  encoding="UTF-8")
    return con

def write_csv():
    con = connector()
    cursor = con.cursor()

    with open("C:\Learnings\writings\csvpr.csv",'w',newline='',encoding='utf-8') as f:
        fieldnames = ['ID','NAME']
        csv_writer = csv.DictWriter(f,fieldnames=fieldnames)
        csv_writer.writeheader()
        names = ['이원석','박민회','김형진']
        for i in range(1,101):
            name = random.choice(names)
            csv_writer.writerow({'ID':i,'NAME':name})

    with open("C:\Learnings\writings\csvpr.csv",'r',newline='',encoding='utf-8') as f:
        csv_reader = csv.DictReader(f)
        for i in csv_reader:
            cursor.execute("INSERT INTO CSV VALUES(:ID , :NAME)",i)
            con.commit()

write_csv()
