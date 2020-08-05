# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import sqlite3 as sql

class SupplierLogin(Resource):

    def post(self):
        print(g.json)
        log = g.json
        email = log["email"]
        if '@' not in email:
            return "Incorrect email",200,None
        conn = sql.connect("./database/supplierdb")
        connc = conn.cursor()
        connc.execute("SELECT password FROM supplier WHERE email = '"+log["email"]+"'")
        res = connc.fetchall()
        if len(res)!= 0:
            s = res[0]
            a = s[0]
            if log["password"] == a:
                connc.execute("UPDATE supplier SET userStatus = 1 where email = '"+log["email"]+"'")
                connc.close()
                return "Correct",200,None
        connc.close()
        return "Incorrect password/username",200, None
