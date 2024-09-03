#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024-07-30 15:46:03
# @File           : crud.py
# @IDE            : VSCode
# @desc           :
from core.crud import DalBase
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas


class UsageDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(UsageDal, self).__init__()
        self.db = db
        self.model = models.Usage
        self.schema = schemas.UsageSimpleOut


class UsageDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(UsageDal, self).__init__()
        self.db = db
        self.model = models.Usage
        self.schema = schemas.UsageSimpleOut
