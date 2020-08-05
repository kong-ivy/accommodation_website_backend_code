# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import sqlite3 as sql

class Booking(Resource):

    def post(self):
        print(g.json)
        info = g.json
        info["date_start"] =  info["date_start"].replace("-","")
        info["date_end"] = info["date_end"].replace("-","")
        conn = sql.connect("./database_epic2/roomdb")
        connc = conn.cursor()
        connc.execute("""SELECT start_date,end_date FROM orders WHERE rid = '"""+info["rid"]+"'")
        s = connc.fetchall()
        for item in s:
            if int(info["date_start"])>= item[0] and int(info["date_start"])<=item[1]:
                connc.close()
                conn.close()
                return "Time error",200,None
            if int(info["date_end"])>= item[0] and int(info["date_end"])<=item[1]:
                connc.close()
                conn.close()
                return "Time error",200,None
            if int(info["date_start"])<= item[0] and int(info["date_end"])>=item[1]:
                connc.close()
                conn.close()
                return "Time error",200,None
        if info["payment_statue"] == True:
            info["payment_statue"] = 1
        elif info["payment_statue"] == False:
            info["payment_statue"] = 0
        connc.execute("""INSERT INTO orders (rid,uid,first_name,last_name,email,mobile_phone,start_date,end_date,order_price,payment_statue)
                      VALUES (?,?,?,?,?,?,?,?,?,?)""",(info["rid"],info["uid"],info["first_name"],info["last_name"],info["email"],info["mobile_phone"],int(info["date_start"]),int(info["date_end"]),
                                             info["price"],info["payment_statue"]))
        conn.commit()
        connc.close()
        conn.close()
        
        return "order succeed",200,None
