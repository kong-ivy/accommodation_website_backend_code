# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import sqlite3 as sql

class SupplierInfo(Resource):

    def get(self):
        print(g.args)
        u = g.args
        conn = sql.connect("./database/supplierdb")
        connc = conn.cursor()
        connc.execute("SELECT * FROM supplier WHERE sid = '"+u["sid"]+"'")
        res = connc.fetchall()
        connc.close()
        res = res[0]
        return {'sid':res[0],'last_name':res[1],'first_name':res[2],'birthday':res[3],'email':res[4],'mobile_phone':res[6]},200,None
        return None, 200, None
