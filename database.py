import sqlite3 as sql3
# db = sql3.connect('user.db')
# cursor =  db.cursor()
# db.commit()
# db.close()

with sql3.connect('users.db') as connection:
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
    fulname TEXT NOT NULL,
    id  INT NOT NULL,
    salary INT DATE
    )''')

cursor.execute('''SELECT rowid,* FROM employees''')
for row in cursor.fetchall():
    print(row)

