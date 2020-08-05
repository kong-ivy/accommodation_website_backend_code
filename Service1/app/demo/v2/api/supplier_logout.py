# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas

import sqlite3 as sql
class SupplierLogout(Resource):

    def get(self):
        print(g.args)
        logout = g.args
        conn = sql.connect("./database/supplierdb")
        connc = conn.cursor()
        connc.execute("UPDATE supplier SET userStatus = 0 WHERE email = '"+logout["suppliername"]+"'")
        connc.close()
        
        return 200
