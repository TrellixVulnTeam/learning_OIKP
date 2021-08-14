import cx_Oracle
import pickle
import json

def connector():
    dsn = cx_Oracle.makedsn("localhost", 1521, service_name="xe")
    connection = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn=dsn, encoding="UTF-8")
    cursor = connection.cursor()
    return cursor


def write01(query):
    path = "C:/learnings/files/"
    cursor = connector()
    cursor.execute(query)
    file = open(path+'a.txt','w',encoding='utf-8')
    for i in cursor.fetchall():
        file.write("".join(str(i)) + "\n")
    file.close()

def write02(query): #pickling 형식 구현해보자.
    path = "C:/learnings/files/"
    cursor = connector()
    cursor.execute(query)
    cols = [col[0] for col in cursor.description]
    cursor.rowfactory = lambda *args : dict(zip(cols,args))
    file = open(path+'b.txt','wb')
    data = cursor.fetchone()
    data["HIREDATE"] = "/".join(map(str,[data["HIREDATE"].year,data["HIREDATE"].month ,data["HIREDATE"].day]))

    while data :
        pickle.dump(data,file)
        data = cursor.fetchone()
        if data != None:
            data["HIREDATE"] = "/".join(map(str, [data["HIREDATE"].year, data["HIREDATE"].month, data["HIREDATE"].day]))
        else :
            break

def write03(query): #json 형식 구현
    path = "C:/learnings/files/"
    cursor = connector()
    cursor.execute(query)
    cols = [col[0] for col in cursor.description]
    cursor.rowfactory = lambda *args: dict(zip(cols, args))
    file = open(path + 'b.json', 'w')
    data = cursor.fetchall()
    hash = {"result": []}
    for i in data:
        i["HIREDATE"] = "/".join(map(str, [i["HIREDATE"].year, i["HIREDATE"].month, i["HIREDATE"].day]))
        hash["result"].append(i)
    json.dump(hash,fp=file,indent=4,sort_keys=True)


def read():
    with open("C:/learnings/files/a.txt",'r',encoding='utf-8') as f:
        line = f.readline()
        while line:
            print(line,end = '\r')
            line = f.readline()

def read_pickle():
    with open("C:/learnings/files/b.txt",'rb') as f: #binarized.
        pic = pickle.load(f)
        pics =[]
        while pic:
            try:
                pics.append(pic)
                pic = pickle.load(f)
            except:
                break
        print(pics)

write03("SELECT *FROM EMP")
