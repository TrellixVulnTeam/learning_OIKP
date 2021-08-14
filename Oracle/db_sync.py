import cx_Oracle

def connector():
    userpwd = "TIGER" # Obtain password string from a user prompt or environment variable
    dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XE")
    conn = cx_Oracle.connect(user="SCOTT", password=userpwd, dsn=dsn, encoding="UTF-8")
    cursor = conn.cursor()
    #def aa1
    #def aa2
    #cursor.execute("SELECT * FROM EMP")
    return cursor

def sql(query):
    cur = connector()
    cur.execute(query)
    #col_name = [col[0] for col in cur.description]
    for j in cur.description:
        print("{:15s}".format(str(j[0])),end=' ')
    print()
    for i in cur.fetchall():
        for j in i:
            if len(str(j)) > 10:
                print("{:15s}".format(str(j)[:10]) ,end= ' ')
            else:
                print("{:15s}".format(str(j)) ,end = ' ' )

        #for j,k in zip(col_name,i):
        #    print(f"{j} ".ljust(10),  f"{k}", sep=": ")
        print()
    cur.close()

def hash(query):
    cur = connector()
    cur.execute(query)
    columns = [col[0] for col in cur.description]
    print(columns)
    cur.rowfactory = lambda *args: dict(zip(columns,args))
    data = cur.fetchone()
    print(type(data),data)

sql("SELECT ENAME, SAL, DEPTNO, SUM(SAL) OVER (PARTITION BY DEPTNO ORDER BY SAL) SUMSAL FROM EMP ")
#hash("SELECT*FROM EMP")



