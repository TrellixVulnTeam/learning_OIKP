import cx_Oracle

dsn = cx_Oracle.makedsn("localhost", 1521, service_name="xe")
connection = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn=dsn, encoding="UTF-8")
cur = connection.cursor()

#sql_cmd = "CREATE TABLE DAY30 (id number, name varchar2(20))"
#cur.execute(sql_cmd)
##place holder를 콜론을 통해 사용한다.

sql_cmd02 = "INSERT INTO DAY30 VALUES(:id,:name)" #임의변수 지정 사용 가능!
cur.execute(sql_cmd02, {"id": 1, "name": "RuRi"})
cur.execute(sql_cmd02, {"id": 2, "name": "DOMI"})
cur.execute(sql_cmd02, {"id": 3, "name": "NICOL"})
cur.execute(sql_cmd02, {"id": 4, "name": "RIO"})

sql_cmd03 = "UPDATE DAY30 SET name = :name where id = :id"
cur.execute(sql_cmd03,{"name":"RUIC", "id": 4}) # RIO -> RUIC

for row in cur.execute("SELECT * FROM day30"):
    print(row)


