#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024-07-10 11:18:45
# @File           : crud.py
# @IDE            : VSCode
# @desc           :
from . import schemas, models
from sqlalchemy.ext.asyncio import AsyncSession
from core.crud import DalBase


class EnterpriseDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(EnterpriseDal, self).__init__()
        self.db = db
        self.model = models.Enterprise
        self.schema = schemas.EnterpriseSimpleOut
