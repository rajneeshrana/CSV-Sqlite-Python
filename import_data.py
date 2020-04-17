import csv
import sqlite3

connection = sqlite3.connect("rajneeshG.db")
cursor = connection.cursor()

with open('file25.csv', 'r', newline='') as f:
    csv_reader = csv.reader(f, delimiter=',')
    no_records = 0
    next(csv_reader,None)
    for row in f:
        cursor.execute("INSERT INTO data VALUES(NULL,?,?)", row.split(","))
        connection.commit()
        no_records += 1
connection.close()
print('\n{} records transferred'.format(no_records))
            