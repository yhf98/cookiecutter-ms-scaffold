#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024-07-15 00:09:20
# @File           : views.py
# @IDE            : VSCode
# @desc           :
from apps.admin.auth.utils.current import AllUserAuth
from utils.response import SuccessResponse
from core.dependencies import IdList
from core.database import db_getter
from . import params, schemas, models, crud
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from apps.admin.auth.utils.validation.auth import Auth
from utils.tools import convert_decimal_to_float

app = APIRouter()

###########################################################
#    订单信息
###########################################################
@app.get("/order", summary="获取订单信息列表")
async def get_order_list(p: params.OrderParams = Depends(), auth: Auth = Depends(AllUserAuth())):
    datas, count = await crud.OrderDal(auth.db).get_datas(**p.dict(), v_return_count=True)
    response = {
        "data": convert_decimal_to_float(datas),
        "count": count
    }
    return SuccessResponse(data=response)


# @app.post("/order", summary="创建订单信息")
# async def create_order(data: schemas.Order, auth: Auth = Depends(AllUserAuth())):
#     return SuccessResponse(await crud.OrderDal(auth.db).create_data(data=data))



@app.post("/order", summary="创建订单信息")
async def create_order(data: schemas.Order, auth: Auth = Depends(AllUserAuth())):
    # 在这里模拟数据库操作并返回数据
    created_order = await crud.OrderDal(auth.db).create_data(data=data)
    converted_order = convert_decimal_to_float(created_order)
    return SuccessResponse(data=converted_order)


@app.delete("/order", summary="删除订单信息", description="硬删除")
async def delete_order_list(ids: IdList = Depends(), auth: Auth = Depends(AllUserAuth())):
    await crud.OrderDal(auth.db).delete_datas(ids=ids.ids, v_soft=False)
    return SuccessResponse("删除成功")


@app.put("/order/{data_id}", summary="更新订单信息")
async def put_order(data_id: int, data: schemas.Order, auth: Auth = Depends(AllUserAuth())):
    return SuccessResponse(await crud.OrderDal(auth.db).put_data(data_id, data))


@app.get("/order/{data_id}", summary="获取订单信息信息")
async def get_order(data_id: int, db: AsyncSession = Depends(db_getter)):
    schema = schemas.OrderSimpleOut
    return SuccessResponse(convert_decimal_to_float(await crud.OrderDal(db).get_data(data_id, v_schema=schema)))




###########################################################
#    订单详情
###########################################################
@app.get("/order/detail", summary="获取订单详情列表")
async def get_order_detail_list(p: params.OrderDetailParams = Depends(), auth: Auth = Depends(AllUserAuth())):
    datas, count = await crud.OrderDetailDal(auth.db).get_datas(**p.dict(), v_return_count=True)
    response = {
        "data": convert_decimal_to_float(datas),
        "count": count
    }
    return SuccessResponse(data=response)

@app.post("/order/detail", summary="创建订单详情")
async def create_order_detail(data: schemas.OrderDetail, auth: Auth = Depends(AllUserAuth())):
    return SuccessResponse(convert_decimal_to_float(await crud.OrderDetailDal(auth.db).create_data(data=data)))


@app.delete("/order/detail", summary="删除订单详情", description="硬删除")
async def delete_order_detail_list(ids: IdList = Depends(), auth: Auth = Depends(AllUserAuth())):
    await crud.OrderDetailDal(auth.db).delete_datas(ids=ids.ids, v_soft=False)
    return SuccessResponse("删除成功")


@app.put("/order/detail/{data_id}", summary="更新订单详情")
async def put_order_detail(data_id: int, data: schemas.OrderDetail, auth: Auth = Depends(AllUserAuth())):
    return SuccessResponse(await crud.OrderDetailDal(auth.db).put_data(data_id, data))


@app.get("/order/detail/{data_id}", summary="获取订单详情信息")
async def get_order_detail(data_id: int, db: AsyncSession = Depends(db_getter)):
    schema = schemas.OrderDetailSimpleOut
    return SuccessResponse(convert_decimal_to_float(await crud.OrderDetailDal(db).get_data(data_id, v_schema=schema)))

