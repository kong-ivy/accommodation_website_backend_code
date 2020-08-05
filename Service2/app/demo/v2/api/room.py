# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import sqlite3 as sql

class Room(Resource):

    def post(self):
        print(g.json)
        info = g.json
        conn_1 = sql.connect('./database_epic2/roomdb')
        conn1c = conn_1.cursor()
        conn1c.execute("""SELECT COUNT(*) FROM room_address""")
        res1 = conn1c.fetchone()
        rid = res1[0]
        info["rid"] = "r"+str(rid)
        conn1c.execute("""INSERT INTO room_address (rid,city,surburb,address) VALUES (?,?,?,?)""",
                       (info["rid"],info["city"],info["Suburb"],info["Address"]))
        conn1c.execute("SELECT * FROM room_address")
        conn_1.commit()
        conn1c.close()
        conn_1.close()
        for item in info:
            if info[item] == True:
                info[item] = 1
            elif info[item] == False:
                info[item] = 0
        conn_2 = sql.connect('./database_epic2/roomdb')
        conn2c = conn_2.cursor()
        conn2c.execute("""INSERT INTO room (rid,sid,name,slug,type,price,capacity,pets,breakfast,airconditioner,
              carpark,wifi,gym,kitchen,description,url1,url2,url3,url4,url5)
              VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
                       ,(info["rid"],info["sid"],info["name"],info["slug"],info["type"],info["price"],info["capacity"]
                         ,info["pets"],info["breakfast"],info["airconditioner"],info["carpark"],info["wifi"],
                         info["gym"],info["kitchen"],info["description"],info["url1"],info["url2"],info["url3"],info["url4"],
                         info["url5"]))
        conn2c.execute("SELECT * FROM room")
        print(conn2c.fetchall())
        conn_2.commit()
        conn2c.close()
        conn_2.close()
        return "Succeed",200,None
        pass
