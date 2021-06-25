import cx_Oracle
from learning_37_request import Gwanggaeto
import json
from datetime import datetime

class OraDB:
    dsn = cx_Oracle.makedsn("localhost", 1521, service_name="xe")
    con = cx_Oracle.connect(user="migo", password="admin1234", dsn=dsn, encoding="UTF-8")
    def __init__(self,args=None):
        if args !=None:
            self.interested_in = args[0]
            self.star_rate = args[5]
            self.address = args[2]
            self.ophours = args[4]
            self.tel = args[3]
            self.coord = args[1]
            self.coord = json.dumps(self.coord)
            self.category = "_".join(args[6])
            self.time =datetime.strftime(datetime.now() , '%Y-%m-%d %H:%M:%S')
            cur = self.con.cursor()
            outval = cur.var(int)
            cur.callproc("GETNUM", [outval])

            self.all_info=[outval,
                           self.interested_in,
                           self.category,
                           self.star_rate,
                           self.address,
                           self.ophours,
                           self.tel,
                           self.coord,
                           self.time]
            try:
                self.oraCreta()
            except:
                pass
        else:
            pass

    def oraCreta(self):
        cur = self.con.cursor()
        cur.execute("""CREATE TABLE USER1 (
                    KEY number(5), 
                    STORE_NAME varchar2(200), 
                    CATEGORY varchar2(200),
                    STAR_RATE float(7),
                    ADDRESS varchar2(200), 
                    OPERATING_HOURS varchar2(200), 
                    TEL varchar2(200),
                    COORDINATE VARCHAR2(200),
                    DOS VARCHAR2(200))
                    """ )
    def insert(self):
        cur = self.con.cursor()

        cur.execute("""INSERT INTO USER1 VALUES(:KEY, :STORE_NAME,:CATEOGRY,:STAR_RATE ,:ADDRESS, :OPERATING_HOURS,
                        :TEL, :COORDINATE, :DOS)""", self.all_info)
        self.con.commit()

    def insight(self):
        cur = self.con.cursor()
        cur.execute("""SELECT COUNT(*), category from user1 group by category order by 1 DESC""")
        for i in cur.fetchall():
            print(i)

        cur.execute("""SELECT count(*), store_name,ADDRESS from USER1 group by STORE_NAME, ADDRESS order by 1 DESC""")

        cur.execute("""SELECT COUNT(*), category from user1 group by category order by 1 DESC""")

if __name__ == '__main__':
    a = Gwanggaeto("교대 피자")
    ora = OraDB(a.final_choice) #잊지마,all_info!
    ora.insert()

   # ora = OraDB()
    #ora.insight()



