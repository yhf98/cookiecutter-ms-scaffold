#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024-07-15 15:00:15
# @File           : views.py
# @IDE            : VSCode
# @desc           :

from core.dependencies import IdList
from fastapi import APIRouter, Depends
from utils.response import SuccessResponse
from apps.admin.auth.utils.validation.auth import Auth
from sqlalchemy.ext.asyncio import AsyncSession
from apps.platform.user import params, models, schemas, crud
from apps.admin.auth.utils.current import AllUserAuth
from core.database import db_getter
from apps.platform.user.models import User

app = APIRouter()


###########################################################
#    B端用户信息
###########################################################
@app.get("/user", summary="获取B端用户信息列表")
async def get_user_list(p: params.UserParams = Depends(), auth: Auth = Depends(AllUserAuth())):
    v_where = []
    if p.start_time:
        v_where.append(User.create_at >= p.start_time)
    if p.end_time:
        v_where.append(User.create_at <= p.end_time)
    datas, count = await crud.UserDal(auth.db).get_datas(**p.dict(), v_where = v_where, v_schema=schemas.UserWithoutPassword, v_return_count=True)
    return SuccessResponse(datas, count=count)