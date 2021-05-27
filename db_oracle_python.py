# SCOTT/TIGER@LOCALHOST:1521/xe
# client주소

#EMP 테이블의 데이터를 파이썬 프로그램으로 읽어서 리턴을 받자.

import cx_Oracle



def myCon(): #매번 연결시키긴 귀찮으므로 함수를 만들어 저장.
    # Database Server Name - DSN
    dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XE") #오라클 주소
    connection = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn=dsn,
                               encoding="UTF-8")
    print(connection)
    return connection


def Test01(connection):
    cur = connection.cursor() #실행결과 데이터를 담을 메모리 객체
    for row in cur.execute("select * from EMP"):  #실행문을 SQL에서처럼 담는다.
        print(" | ".join(list(map(str,row))))



def Test02(connection):
    cur = connection.cursor()
    cur.execute("select * from EMP")
    while True:
        row = cur.fetchone()
        if row is None:
            break
        print(row)


def Test03():
    cur = myCon().cursor()
    cur.execute("select * from EMP")
    num_rows = 4 #4개씩 체크한다는 의미. 4개만 빼오겠다는 의미가 아님.
    while True:
        rows = cur.fetchmany(num_rows)
        if not rows:
            break
        for row in rows:
            print(row)

def Test04():
    cur = myCon().cursor()
    cur.execute("select * from EMP")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    #Test01(myCon())
    #Test02(myCon())
    Test03()
