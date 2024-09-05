#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024-07-29 22:05:23
# @File           : crud.py
# @IDE            : VSCode
# @desc           :
from core.crud import DalBase
from apps.schemas import UserSimpleOut, UserCounterOut
from apps.models import User

from sqlalchemy.ext.asyncio import AsyncSession
class UserDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(UserDal, self).__init__()
        self.db = db
        self.model = User
        self.schema = UserSimpleOut
        
    async def get_user_count(self) -> int:
        data: UserCounterOut = await self.execute_query('users', 'getUserCount',v_schema=UserCounterOut)
        
        if data is None or data.total <= 0: return 0
        
        return data.total
