# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import sqlite3 as sql

class UserLogout(Resource):

    def get(self):
        print(g.args)
        logout = g.args
        conn = sql.connect("./database/userdb")
        connc = conn.cursor()
        connc.execute("UPDATE user SET userStatus = 0 WHERE email = '"+logout["username"]+"'")
        connc.close()
        
        return 200
