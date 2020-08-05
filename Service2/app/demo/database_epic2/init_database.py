import sqlite3 as sql

conn = sql.connect("roomdb")

connc = conn.cursor()
connc.execute("""CREATE TABLE room_address (rid TEXT,city TEXT,surburb TEXT,address TEXT)""")
connc.execute("""CREATE TABLE room (rid TEXT,sid TEXT,name TEXT,slug TEXT,type TEXT,price INTEGER,
              capacity INTEGER,pets INTEGER,breakfast INTEGER,airconditioner INTEGER,
              carpark INTEGER,wifi INTEGER,gym INTEGER,kitchen INTEGER,description INTEGER,url1 TEXT,url2 TEXT,url3 TEXT,url4 TEXT,url5 TEXT)""")
connc.execute("CREATE TABLE orders (rid TEXT,uid TEXT,first_name TEXT,last_name TEXT,email TEXT,mobile_phone TEXT,start_date INTEGER,end_date INTEGER,order_price TEXT,payment_statue INTEGER)")
#connc.execute("""INSERT INTO room (rid,name,slug,type,price,size,capacity,pets,
#              breakfast,featured,airconditioner,carpark,wifi,gym,kitchen,description,url)
#              VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
#              ("r9","family economy","family-economy","family",300,500,3,"false",
#               "false","false","false","false","false","false","false",
#               """Street art edison bulb gluten-free, tofu try-hard lumbersexual brooklyn tattooed pickled chambray. Actually humblebrag next level, deep v art party wolf tofu direct trade readymade sustainable hell of banjo. Organic authentic subway tile cliche palo santo, street art XOXO dreamcatcher retro sriracha portland air plant kitsch stumptown. Austin small batch squid gastropub. Pabst pug tumblr gochujang offal retro cloud bread bushwick semiotics before they sold out sartorial literally mlkshk. Vaporware hashtag vice, sartorial before they sold out pok pok health goth trust fund cray.""","./images/room/16.jpg"))
#connc.execute("SELECT * FROM room")

#print(connc.fetchall())

connc.close()
conn.close()
