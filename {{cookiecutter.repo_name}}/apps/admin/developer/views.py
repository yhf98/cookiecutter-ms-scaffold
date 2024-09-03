#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024-07-10 11:18:45
# @File           : views.py
# @IDE            : VSCode
# @desc           :
from . import schemas, crud, params, models
from core.dependencies import IdList
from apps.admin.auth.utils.current import AllUserAuth
from apps.admin.auth.utils.validation.auth import Auth
from fastapi import APIRouter, Depends,Form, File, UploadFile
from core.database import db_getter
from utils.response import SuccessResponse
from sqlalchemy.ext.asyncio import AsyncSession
from utils.file.aliyun_oss import AliyunOSS, BucketConf
from application.settings import ALIYUN_OSS

from typing import Optional


app = APIRouter()

###########################################################
#    企业信息
###########################################################
@app.get("/enterprise", summary="获取企业信息列表", tags=["企业信息"])
async def get_enterprise_list(p: params.EnterpriseParams = Depends(), auth: Auth = Depends(AllUserAuth())):
    datas, count = await crud.EnterpriseDal(auth.db).get_datas(**p.dict(), v_return_count=True)
    return SuccessResponse(datas, count=count)


# @app.post("/enterprise", summary="创建企业信息", tags=["企业信息"])
# async def create_enterprise(data: schemas.Enterprise, auth: Auth = Depends(AllUserAuth())):
#     return SuccessResponse(await crud.EnterpriseDal(auth.db).create_data(data=data))
@app.post("/enterprise", summary="创建企业信息", tags=["企业信息"])
async def create_enterprise(
    enterprise_name: str = Form(...),
    phone: str = Form(...),
    legal_name: str = Form(...),
    legal_id_number: str = Form(...),
    social_credit_code: str = Form(...),
    status: int = Form(0),
    address: Optional[str] = Form(None),
    other_phone: Optional[str] = Form(None),
    email: Optional[str] = Form(None),
    industry: Optional[str] = Form(None),
    user_id: int = Form(...),
    create_user_id: int = Form(...),
    business_license: UploadFile = File(...),
    auth: Auth = Depends(AllUserAuth())
):
    filepath = f"/resource/business_license/"
    result = await AliyunOSS(BucketConf(**ALIYUN_OSS)).upload_image(filepath, business_license)
    print("文件上传成功：", result)
    data = schemas.Enterprise(
        enterprise_name=enterprise_name,
        phone=phone,
        legal_name=legal_name,
        legal_id_number=legal_id_number,
        social_credit_code=social_credit_code,
        status=status,
        address=address,
        other_phone=other_phone,
        email=email,
        industry=industry,
        user_id=user_id,
        create_user_id=create_user_id,
        business_license = result
    )
    return SuccessResponse(await crud.EnterpriseDal(auth.db).create_data(data=data))

@app.delete("/enterprise", summary="删除企业信息", description="硬删除", tags=["企业信息"])
async def delete_enterprise_list(ids: IdList = Depends(), auth: Auth = Depends(AllUserAuth())):
    await crud.EnterpriseDal(auth.db).delete_datas(ids=ids.ids, v_soft=False)
    return SuccessResponse("删除成功")


@app.put("/enterprise/{data_id}", summary="更新企业信息", tags=["企业信息"])
async def put_enterprise(data_id: int, data: schemas.Enterprise, auth: Auth = Depends(AllUserAuth())):
    return SuccessResponse(await crud.EnterpriseDal(auth.db).put_data(data_id, data))


@app.get("/enterprise/{data_id}", summary="获取企业信息信息", tags=["企业信息"])
async def get_enterprise(data_id: int, db: AsyncSession = Depends(db_getter)):
    schema = schemas.EnterpriseSimpleOut
    return SuccessResponse(await crud.EnterpriseDal(db).get_data(data_id, v_schema=schema))

