import cx_Oracle
import pickle

def connector():
    dsn = cx_Oracle.makedsn("localhost", 1521, service_name="xe")
    con = cx_Oracle.connect(user="MYDB", password="admin1234", dsn=dsn,  encoding="UTF-8")
    return con
def pickling(): #피클링 될 파일 적기
    with open('pickling.txt','wb') as f:
        a = [1,2,3,4,5] #for practice
        for i in range(5):
            pickle.dump(a,f)
def insert():
    con = connector()
    cur = con.cursor()
    with open('pickling.txt','rb') as f:

        try:
            for i in range(5):
                cur.execute("insert into pickling values(:id , :data)",{"id":"1","data": pickle.dumps(pickle.load(f))}) # 재이진화 시켜 저장
                con.commit()
        except Exception as E:
            print(E)

#pickling()
insert()
