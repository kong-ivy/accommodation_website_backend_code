# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import sqlite3 as sql

class RoomCancel(Resource):

    def post(self):
        print(g.json)
        info = g.json
        conn = sql.connect('./database_epic2/roomdb')
        connc = conn.cursor()
        connc.execute("DELETE FROM room_address WHERE rid = '"+info["rid"]+"'")
        connc.execute("DELETE FROM room WHERE rid = '"+info["rid"]+"'")
        conn.commit()
        connc.close()
        conn.close()

        
        return "Your room has been removed",200,None
