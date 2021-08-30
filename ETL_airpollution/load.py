import sqlalchemy
#ORM is library that allows you to
#access data directly from python. sqlalchemy is one of them
import sqlite3
import extraction
import requests




engine = sqlalchemy.create_engine('sqlite:///db.db')
conn = sqlite3.connect("db.db")
cursor = conn.cursor()

sql_query="""
CREATE TABLE IF NOT EXISTS my_table(
    observation_location VARCHAR(200),
    time VARCHAR(200),
    pm2_5 VARCHAR(200),
    pm10 VARCHAR(200),
    ozone VARCHAR(200),
    CONSTRAINT primary_key_constraint PRIMARY KEY (time))
"""

cursor.execute(sql_query)
print("Opened database successfully")

try:
    extraction.weather_extract(1).to_sql("my_table",engine,index=False,if_exists='append')

except:
    print("Data already exists in the database")

conn.close()