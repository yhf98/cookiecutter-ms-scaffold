#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/07/10 00:01
# @File           : crud.py
# @IDE            : VSCode
# @desc           : 数据访问层
from sqlalchemy.ext.asyncio import AsyncSession
from . import schemas, models
from core.crud import DalBase



class InterfaceInfoDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(InterfaceInfoDal, self).__init__()
        self.db = db
        self.model = models.InterfaceInfo
        self.schema = schemas.InterfaceInfoSimpleOut


class InterfaceUsageDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(InterfaceUsageDal, self).__init__()
        self.db = db
        self.model = models.InterfaceUsage
        self.schema = schemas.InterfaceUsageSimpleOut
