# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import sqlite3 as sql

class RoomSupplier(Resource):

    def get(self):
        print(g.args)
        info = g.args
        conn = sql.connect('./database_epic2/roomdb')
        result = []
        connc1 = conn.cursor()
        connc1.execute("SELECT * FROM room WHERE sid = '"+info["sid"]+"'")
        res = connc1.fetchall()
        for one_re in res:
            dic = {"rid":one_re[0],"sid":one_re[1],"name":one_re[2],"slug":one_re[3],
                   "type":one_re[4],"price":one_re[5],"capacity":one_re[6],"pets":one_re[7],"breakfast":one_re[8],
                   "airconditioner":one_re[9],"carpark":one_re[10],"wifi":one_re[11],"gym":one_re[12],
                   "kitchen":one_re[13],"description":one_re[14],"url1":one_re[15],"url2":one_re[16],"url3":one_re[17],
                   "url4":one_re[18],"url5":one_re[19]}
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
        conn.commit()
        return result,200,None
