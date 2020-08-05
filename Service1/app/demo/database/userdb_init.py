import sqlite3 as sql

def build_dbase(dbname):
    conn = sql.connect(dbname)
    return conn.cursor()

def build_usertable(conn):
    conn.execute("CREATE TABLE user (uid TETX,last_name TEXT,first_name TEXT,birthday TEXT,email TEXT,password TEXT,mobile_phone TEXT, userStatus INTEGER)")
    #conn.execute("INSERT INTO user (uid,last_name,first_name,email,password,mobile_phone, userStatus) VALUES (?,?,?,?,?,?,?)",("U1","zx","xiao","z5202238","123456","110",1))
    return conn

def build_suppliertable(conn):
    conn.execute("CREATE TABLE supplier (sid TETX,last_name TEXT,first_name TEXT,birthday TEXT,email TEXT,password TEXT,mobile_phone TEXT, userStatus INTEGER)")
    #conn.execute("INSERT INTO supplier (sid,last_name,first_name,email,password,mobile_phone, userStatus) VALUES (?,?,?,?,?,?,?)",("s1","zx","xiao","z5202238","123456","110",1))
    return conn
def search(conn):
    conn.execute("SELECT * FROM supplier")
    res = conn.fetchall()
    conn.close()
    return res
def init_db():
    conn_user = build_dbase("userdb")
    conn_user = build_usertable(conn_user)
    print("user_db created succeed")
    conn_user.close()
    conn_supplier = build_dbase("supplierdb")
    conn_supplier = build_suppliertable(conn_supplier)
    print("supplier_db created succeed")
    conn_supplier.close()

if __name__ =='__main__':
    init_db()
    
    
