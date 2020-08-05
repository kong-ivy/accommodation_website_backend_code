import sqlite3 as sql

conn = sql.connect("roomdb")

connc = conn.cursor()

connc.execute("""SELECT * FROM orders""")
print(connc.fetchall())
connc.close()
conn.close()
