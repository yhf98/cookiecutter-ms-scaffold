#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024-07-15 00:09:20
# @File           : crud.py
# @IDE            : VSCode
# @desc           :
from . import schemas, models
from sqlalchemy.ext.asyncio import AsyncSession
from core.crud import DalBase


class OrderDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(OrderDal, self).__init__()
        self.db = db
        self.model = models.Order
        self.schema = schemas.OrderSimpleOut


class OrderDetailDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(OrderDetailDal, self).__init__()
        self.db = db
        self.model = models.OrderDetail
        self.schema = schemas.OrderDetailSimpleOut
