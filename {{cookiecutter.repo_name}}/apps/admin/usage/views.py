#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024-07-30 15:46:03
# @File           : views.py
# @IDE            : VSCode
# @desc           :
from core.dependencies import IdList
from utils.response import SuccessResponse
from apps.admin.auth.utils.validation.auth import Auth
from core.database import db_getter
from apps.admin.auth.utils.current import AllUserAuth
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, params, schemas, crud

app = APIRouter()

###########################################################
#    产品用量记录
###########################################################
@app.get("/usage", summary="获取产品用量记录列表", tags=["产品用量记录"])
async def get_usage_list(p: params.UsageParams = Depends(), auth: Auth = Depends(AllUserAuth())):
    datas, count = await crud.UsageDal(auth.db).get_datas(**p.dict(["name"]), v_return_count=True)
    return SuccessResponse(datas, count=count)


@app.post("/usage", summary="创建产品用量记录", tags=["产品用量记录"])
async def create_usage(data: schemas.Usage, auth: Auth = Depends(AllUserAuth())):
    return SuccessResponse(await crud.UsageDal(auth.db).create_data(data=data))


@app.delete("/usage", summary="删除产品用量记录", description="硬删除", tags=["产品用量记录"])
async def delete_usage_list(ids: IdList = Depends(), auth: Auth = Depends(AllUserAuth())):
    await crud.UsageDal(auth.db).delete_datas(ids=ids.ids, v_soft=False)
    return SuccessResponse("删除成功")


@app.put("/usage/{data_id}", summary="更新产品用量记录", tags=["产品用量记录"])
async def put_usage(data_id: int, data: schemas.Usage, auth: Auth = Depends(AllUserAuth())):
    return SuccessResponse(await crud.UsageDal(auth.db).put_data(data_id, data))


@app.get("/usage/{data_id}", summary="获取产品用量记录信息", tags=["产品用量记录"])
async def get_usage(data_id: int, db: AsyncSession = Depends(db_getter)):
    schema = schemas.UsageSimpleOut
    return SuccessResponse(await crud.UsageDal(db).get_data(data_id, v_schema=schema))

