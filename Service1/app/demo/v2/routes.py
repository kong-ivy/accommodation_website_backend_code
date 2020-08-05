# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.user import User
from .api.user_login import UserLogin
from .api.user_logout import UserLogout
from .api.user_info import UserInfo
from .api.supplier import Supplier
from .api.supplier_login import SupplierLogin
from .api.supplier_logout import SupplierLogout
from .api.supplier_info import SupplierInfo


routes = [
    dict(resource=User, urls=['/user'], endpoint='user'),
    dict(resource=UserLogin, urls=['/user/login'], endpoint='user_login'),
    dict(resource=UserLogout, urls=['/user/logout'], endpoint='user_logout'),
    dict(resource=UserInfo, urls=['/user/info'], endpoint='user_info'),
    dict(resource=Supplier, urls=['/supplier'], endpoint='supplier'),
    dict(resource=SupplierLogin, urls=['/supplier/login'], endpoint='supplier_login'),
    dict(resource=SupplierLogout, urls=['/supplier/logout'], endpoint='supplier_logout'),
    dict(resource=SupplierInfo, urls=['/supplier/info'], endpoint='supplier_info'),
]