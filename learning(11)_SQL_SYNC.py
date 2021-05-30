import cx_Oracle
import sys
from functools import reduce


class Table:
    current_table = []

    @staticmethod
    def connector():
        dsn = cx_Oracle.makedsn("localhost", 1521, service_name="xe")
        connection = cx_Oracle.connect(user="SCOTT",password="TIGER", dsn=dsn, encoding="UTF-8")
        cursor = connection.cursor()
        return cursor

    @staticmethod
    def query(query):
        cursor = Table.connector()
        cursor.execute(query)
        res = cursor.fetchall()

        cols = [i[0] for i in cursor.description]
        for i in cols:
            print("{:20s}".format(i) , end='')
        print()

        if res == []:
            print('no row selected')
        else:
            print('-'*20*(len(cols)-1) + '-'*len(cols[-1]))
            for i in res:  #;, / 넣으면 안됌
                for j in i:
                    if len(str(j)) > 10:
                        print("{:20s}".format(str(j)[:10]), end = '')
                    else:
                        print("{:20s}".format(str(j)), end='')
                print()
    #각자의 태스크 진짜 테이블을 출력하도록 만들어보자.

    @staticmethod
    def CRUD(query):
        cursor= Table.connector()
        #SELECT, UPDATE, DELETE, INSERT
        #CREATE, ALTER, DROP, TRUNCATE, MERGE
        try :
            cursor.execute(query)
            if "CREATE" in query.upper():
                str = ''
                for i in query[13:]:
                    if i == ' ':
                        break
                    else:
                        str += i
                Table.current_table.append(str)
        except Exception as E:
            B = sys.exc_info()[1]
            print(B)
        else:
            print("CRUD complete")


'''
def query2(query):
    cursor = connector()
    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    cursor.rowfactory = lambda *args: dict(zip(columns, args))
    data = cursor.fetchall()
    print(data[0]['DEPTNO'])
'''


print(dir(Table))


#query("SELECT * FROM EMP")
