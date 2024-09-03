#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024-07-26 15:45:18
# @File           : views.py
# @IDE            : VSCode
# @desc           :
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from apps.admin.auth.utils.validation.auth import Auth
from utils.response import SuccessResponse
from core.dependencies import IdList
from apps.admin.auth.utils.current import AllUserAuth
from core.database import db_getter
from . import models, crud, schemas, params
from fastapi import Depends, APIRouter


app = APIRouter()

###########################################################
#    产品信息
###########################################################
@app.get("/product", summary="获取产品列表")
async def get_product_list(p: params.ProductParams = Depends(), auth: Auth = Depends(AllUserAuth())):
    # datas, count = await crud.ProductDal(auth.db).get_datas(**p.dict(), v_return_count=True)
    # model = models.Product
    # options = [joinedload(model.product_type)]
    schema = schemas.ProductJoinOut
    
    datas, count = await crud.ProductDal(auth.db).get_datas(**p.dict(),v_options=[joinedload(models.Product.product_type)], v_schema=schema)
    return SuccessResponse(datas, count=count)


@app.post("/product", summary="创建产品")
async def create_product(data: schemas.Product, auth: Auth = Depends(AllUserAuth())):
    return SuccessResponse(await crud.ProductDal(auth.db).create_data(data=data))


@app.delete("/product", summary="删除产品", description="硬删除")
async def delete_product_list(ids: IdList = Depends(), auth: Auth = Depends(AllUserAuth())):
    await crud.ProductDal(auth.db).delete_datas(ids=ids.ids, v_soft=False)
    return SuccessResponse("删除成功")


@app.put("/product/{data_id}", summary="更新产品")
async def put_product(data_id: int, data: schemas.Product, auth: Auth = Depends(AllUserAuth())):
    return SuccessResponse(await crud.ProductDal(auth.db).put_data(data_id, data))


@app.get("/product/{data_id}", summary="获取产品")
async def get_product(data_id: int, db: AsyncSession = Depends(db_getter)):
    schema = schemas.ProductSimpleOut
    return SuccessResponse(await crud.ProductDal(db).get_data(data_id, v_schema=schema))




###########################################################
#    产品类型信息
###########################################################
@app.get("/product/type", summary="获取产品类型列表")
async def get_product_type_list(p: params.ProductTypeParams = Depends(), auth: Auth = Depends(AllUserAuth())):
    datas, count = await crud.ProductTypeDal(auth.db).get_datas(**p.dict(), v_return_count=True)
    
    return SuccessResponse(datas, count=count)

@app.post("/product/type", summary="创建产品类型")
async def create_product_type(data: schemas.ProductType, auth: Auth = Depends(AllUserAuth())):
    return SuccessResponse(await crud.ProductTypeDal(auth.db).create_data(data=data))


@app.delete("/product/type", summary="删除产品类型信息", description="硬删除")
async def delete_product_type_list(ids: IdList = Depends(), auth: Auth = Depends(AllUserAuth())):
    await crud.ProductTypeDal(auth.db).delete_datas(ids=ids.ids, v_soft=False)
    return SuccessResponse("删除成功")


@app.put("/product/type/{data_id}", summary="更新产品类型信息")
async def put_product_type(data_id: int, data: schemas.ProductType, auth: Auth = Depends(AllUserAuth())):
    return SuccessResponse(await crud.ProductTypeDal(auth.db).put_data(data_id, data))


@app.get("/product/type/{data_id}", summary="获取产品类型信息信息")
async def get_product_type(data_id: int, db: AsyncSession = Depends(db_getter)):
    schema = schemas.ProductTypeSimpleOut
    return SuccessResponse(await crud.ProductTypeDal(db).get_data(data_id, v_schema=schema))

