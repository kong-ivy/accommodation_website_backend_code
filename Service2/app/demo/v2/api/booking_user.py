# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import sqlite3 as sql

class BookingUser(Resource):

    def get(self):
        print(g.args)
        info = g.args
        conn = sql.connect("./database_epic2/roomdb")
        connc = conn.cursor()
        connc.execute("SELECT * FROM orders WHERE uid = '"+ info["uid"]+"'")
        res = connc.fetchall()
        result = []
        for item in res:
            
            connc.execute("SELECT * FROM room WHERE rid = '"+str(item[0])+"'")
            res1 = connc.fetchone()
            connc.execute("SELECT * FROM room_address WHERE rid = '"+str(item[0])+"'")
            res2 = connc.fetchone()
            #print(res1)
            #print(res2)
            dic = {"rid":item[0],"uid":item[1],"first_name":item[2],"last_name":item[3],"email":item[4],"mobile_phone":item[5],"date_start":item[6],"date_end":item[7],
                   "price":item[8],"payment_statue":item[9],"room_name":res1[2],"room_type":res1[4],"city":res2[1],
                   "surburb":res2[2],"address":res2[3]}
            if dic["payment_statue"] == 0:
                dic["payment_statue"] = False
            elif dic["payment_statue"] == 1:
                dic["payment_statue"] = True
            result.append(dic)
        connc.close()
        conn.close()
        return result,200,None
