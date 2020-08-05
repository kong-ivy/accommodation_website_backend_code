import sqlite3 as sql

conn = sql.connect("userdb")

conn = conn.cursor()

conn.execute("SELECT * FROM user")

res = conn.fetchall()
print(res)
conn.close()
