
import sqlite3


conn = sqlite3.connect("rajneeshG.db")
cur = conn.cursor()

sql = """
    CREATE TABLE data(
        ID INTEGER PRIMARY KEY,
        NAME TEXT,
        LEI TEXT        
    )"""
    
cur.execute(sql)
print("table has been created")

conn.commit()
conn.close()
