import cx_Oracle

class OraDb1:
    def __init__(self): # 연결
        self.dsn = cx_Oracle.makedsn("localhost", 1521, 'xe')
        self.db = cx_Oracle.connect('SCOTT', 'TIGER', self.dsn)
        self.cur = self.db.cursor()

    def Insert_m(self):
        self.cur.execute("insert into test_mydb values('1','python1')") #변수 찾아서 쓸것.
        self.db.commit()
        self.cur.close()
        self.db.close() #창이 닫을때까지 클로즈 안하기때문에 메소드마다 다 DB를 닫게 해준다.
    def Select_all(self):

        self.cur.execute("select * from Test_mydb")
        result = self.cur.fetchall()
        for row in result:
            print(str(row[0]) + "   " + row[1])
        self.cur.close()
        self.db.close()



    def __del__(self):  # 닫기
        pass
        #self.db.close()



if __name__ == '__main__':

    test = OraDb1()
    test.Select_all()