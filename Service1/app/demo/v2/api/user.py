# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import sqlite3 as sql

class User(Resource):

    def post(self):
        print(g.json)
        userinfo = g.json
        for item in userinfo:
            if len(str(userinfo[item])) == 0:
                return "Incorrect information",200,None
        email = userinfo["email"]
        if '@' not in email:
            return "Wrong email",200,None
        conn = sql.connect("./database/userdb")
        connc = conn.cursor()
        connc.execute("SELECT * FROM user WHERE email = '"+ userinfo["email"]+"'")
        res = connc.fetchall()
        
        if len(res)!=0:
            return "User has existed",200,None
        connc.execute("INSERT INTO user (uid,last_name,first_name,birthday,email,password,mobile_phone, userStatus) VALUES (?,?,?,?,?,?,?,?)"
                     ,(userinfo["email"],userinfo["last_name"],userinfo["first_name"],userinfo["birthday"],userinfo["email"],userinfo["password"],
                       userinfo["mobile_phone"],userinfo["userStatus"]))
        conn.commit()
        connc.close()
        return "Succeed",200,None
