#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/09/04 13:57
# @File           : views.py
# @IDE            : VSCode
# @desc           : 路由，视图文件

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from . import models, schemas, crud, params
from core.dependencies import IdList
from apps.admin.auth.utils.current import AllUserAuth
from utils.response import SuccessResponse
from apps.admin.auth.utils.validation.auth import Auth
from core.database import db_getter


app = APIRouter()


###########################################################
#    用户
###########################################################
@app.get("/user", summary="获取用户列表", tags=["用户"])
async def get_user_list(p: params.UserParams = Depends(), auth: Auth = Depends(AllUserAuth())):
    datas, count = await crud.UserDal(auth.db).get_datas(**p.dict(), v_return_count=True)
    return SuccessResponse(datas, count=count)


@app.post("/user", summary="创建用户", tags=["用户"])
async def create_user(data: schemas.User, auth: Auth = Depends(AllUserAuth())):
    return SuccessResponse(await crud.UserDal(auth.db).create_data(data=data))


@app.delete("/user", summary="删除用户", description="硬删除", tags=["用户"])
async def delete_user_list(ids: IdList = Depends(), auth: Auth = Depends(AllUserAuth())):
    await crud.UserDal(auth.db).delete_datas(ids=ids.ids, v_soft=False)
    return SuccessResponse("删除成功")


@app.put("/user/{data_id}", summary="更新用户", tags=["用户"])
async def put_user(data_id: int, data: schemas.User, auth: Auth = Depends(AllUserAuth())):
    return SuccessResponse(await crud.UserDal(auth.db).put_data(data_id, data))


@app.get("/user/{data_id}", summary="获取用户信息", tags=["用户"])
async def get_user(data_id: int, db: AsyncSession = Depends(db_getter)):
    schema = schemas.UserSimpleOut
    return SuccessResponse(await crud.UserDal(db).get_data(data_id, v_schema=schema))

