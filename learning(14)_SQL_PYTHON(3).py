import cx_Oracle

def Create_Table():
    dsn = cx_Oracle.makedsn("localhost",1521,'xe')
    db = cx_Oracle.connect('SCOTT','TIGER',dsn)
    cur = db.cursor()

    sql_cmd = "CREATE TABLE Test_mydb(id number, name varchar2(20))"
    cur.execute(sql_cmd)
    db.close() # 디비 꺼준다.



def Select_all():
    dsn = cx_Oracle.makedsn("localhost", 1521, 'xe')
    db = cx_Oracle.connect('SCOTT', 'TIGER', dsn)
    cur = db.cursor()
    cur.execute("select * from Test_mydb")
    result = cur.fetchall()
    for row in result:
        print(str(row[0]) + "   "+ row[1])
    cur.close()
    db.close()

def Insert_m():
    dsn = cx_Oracle.makedsn("localhost", 1521, 'xe')
    db = cx_Oracle.connect('SCOTT', 'TIGER', dsn)
    cur = db.cursor()
    cur.execute("insert into test_mydb values('1','python1')")
    cur.execute("insert into test_mydb values('2','python2')")
    cur.execute("insert into test_mydb values('3','python3')")
    cur.execute("insert into test_mydb values('4','python4')")
    db.commit()
    db.close()

if __name__ == '__main__':
    #Create_Table()
    Insert_m()
    Select_all()