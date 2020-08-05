# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import sqlite3 as sql

class RoomSearch(Resource):

    def get(self):
        print(g.args)
        info = g.args
        info["check_in_date"] = info["check_in_date"].replace("-","")
        print(info["check_in_date"])
        info["check_out_date"] = info["check_out_date"].replace("-","")
        print(info["check_out_date"])
        conn = sql.connect('./database_epic2/roomdb')
        connc = conn.cursor()
        connc.execute("SELECT rid FROM room_address WHERE city = '"+info["city"]+"' AND surburb = '"+info["suburb"]+"'")
        res = connc.fetchall()
        connc.close()
        if len(res) == 0:
            return [],200,None
        list_rid = [item[0] for item in res]
        print(list_rid)
        result = []
        connc1 = conn.cursor()
        for rid in list_rid:
            connc1.execute("SELECT * FROM room WHERE rid = '"+rid+"'")
            one_re = connc1.fetchone()
            connc1.execute("SELECT * FROM room_address WHERE rid = '"+rid+"'")
            two_re = connc1.fetchone()
            dic = {"rid":one_re[0],"sid":one_re[1],"name":one_re[2],"slug":one_re[3],
                   "type":one_re[4],"price":one_re[5],"capacity":one_re[6],"pets":one_re[7],"breakfast":one_re[8],
                   "airconditioner":one_re[9],"carpark":one_re[10],"wifi":one_re[11],"gym":one_re[12],
                   "kitchen":one_re[13],"description":one_re[14],"url1":one_re[15],"url2":one_re[16],"url3":one_re[17],
                   "url4":one_re[18],"url5":one_re[19],"city":two_re[1],"suburb":two_re[2],"address":two_re[3]}
            for item in dic:
                if dic[item] == 0:
                    dic[item] = False
                elif dic[item] == 1:
                    dic[item] = True
            if dic["capacity"] == True:
                dic["capacity"] = 1
            elif dic["capacity"] == False:
                dic["capacity"] = 0
            result.append(dic)
        connc1.close()
        
        return result,200,None
