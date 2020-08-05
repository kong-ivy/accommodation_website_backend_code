# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.room import Room
from .api.room_search import RoomSearch
from .api.room_supplier import RoomSupplier
from .api.room_cancel import RoomCancel
from .api.booking import Booking
from .api.booking_user import BookingUser
from .api.booking_cancelorder import BookingCancelorder


routes = [
    dict(resource=Room, urls=['/room'], endpoint='room'),
    dict(resource=RoomSearch, urls=['/room/search'], endpoint='room_search'),
    dict(resource=RoomSupplier, urls=['/room/supplier'], endpoint='room_supplier'),
    dict(resource=RoomCancel, urls=['/room/cancel'], endpoint='room_cancel'),
    dict(resource=Booking, urls=['/booking'], endpoint='booking'),
    dict(resource=BookingUser, urls=['/booking/user'], endpoint='booking_user'),
    dict(resource=BookingCancelorder, urls=['/booking/cancelorder'], endpoint='booking_cancelorder'),
]