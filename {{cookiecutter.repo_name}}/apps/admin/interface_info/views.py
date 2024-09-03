#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/07/10 00:01
# @File           : views.py
# @IDE            : VSCode
# @desc           : 路由，视图文件
from apps.admin.interface_info.models import InterfaceInfo
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, APIRouter
from apps.admin.auth.utils.current import AllUserAuth
from utils.response import SuccessResponse, ErrorResponse
from core.database import db_getter
from utils.gateway import Gateway
from apps.admin.auth.utils.validation.auth import Auth
from core.dependencies import IdList
from . import schemas, models, crud, params
from core.exception import CustomException



app = APIRouter()

g = Gateway()


###########################################################
#    接口信息
###########################################################
@app.get("/interface/info", summary="获取接口信息列表", tags=["接口信息"])
async def get_interface_info_list(p: params.InterfaceInfoParams = Depends(), auth: Auth = Depends(AllUserAuth())):
    datas, count = await crud.InterfaceInfoDal(auth.db).get_datas(**p.dict(), v_return_count=True)
    return SuccessResponse(datas, count=count)


@app.post("/interface/info", summary="创建接口信息", tags=["接口信息"])
async def create_interface_info(data: schemas.InterfaceInfo, auth: Auth = Depends(AllUserAuth())):
    r = await crud.InterfaceInfoDal(auth.db).create_data(data=data)
    if r and g.add_service(data.name, f"{data.protocol}://{data.host}:{data.port}", data.route_path):
        return SuccessResponse(data="服务添加成功")

    # TODO: 如果服务添加失败，事务回滚
    auth.db.rollback()
    return ErrorResponse(data="服务添加失败")


@app.delete("/interface/info", summary="删除接口信息", description="硬删除", tags=["接口信息"])
async def delete_interface_info_list(ids: IdList = Depends(), auth: Auth = Depends(AllUserAuth())):
    try:
        # datas = crud.InterfaceInfoDal(auth.db).get_datas(id=("in", ids))
        # datas = crud.InterfaceInfoDal(auth.db).get_datas(limit=0, v_where=[InterfaceInfo.id.in_(ids.ids)], v_return_objs= True)
        # print(datas)
        # FIXME: 批量删除
        data = await crud.InterfaceInfoDal(auth.db).get_data(ids.ids[0], v_schema=schemas.InterfaceInfoSimpleOut)
        print("服务名称：：", data.get("name"))
        if not g.delete_service(data.get("name")):
            raise CustomException("删除失败", code=500)
        await crud.InterfaceInfoDal(auth.db).delete_datas(ids.ids, v_soft=True)
        return SuccessResponse(data="删除成功")
    except Exception as e:
        return ErrorResponse(data=str(e), code=500)


@app.put("/interface/info/{data_id}", summary="更新接口信息", tags=["接口信息"])
async def put_interface_info(data_id: int, data: schemas.InterfaceInfo, auth: Auth = Depends(AllUserAuth())):
    return SuccessResponse(await crud.InterfaceInfoDal(auth.db).put_data(data_id, data))


@app.get("/interface/info/{data_id}", summary="获取接口信息信息", tags=["接口信息"])
async def get_interface_info(data_id: int, db: AsyncSession = Depends(db_getter)):
    return SuccessResponse(await crud.InterfaceInfoDal(db).get_data(data_id, v_schema=schemas.InterfaceInfoSimpleOut))



###########################################################
#    接口用量统计
###########################################################
@app.get("/interface/usage", summary="获取接口用量统计列表", tags=["接口用量统计"])
async def get_interface_usage_list(p: params.InterfaceUsageParams = Depends(), auth: Auth = Depends(AllUserAuth())):
    datas, count = await crud.InterfaceUsageDal(auth.db).get_datas(**p.dict(), v_return_count=True)
    return SuccessResponse(datas, count=count)


@app.post("/interface/usage", summary="创建接口用量统计", tags=["接口用量统计"])
async def create_interface_usage(data: schemas.InterfaceUsage, auth: Auth = Depends(AllUserAuth())):
    return SuccessResponse(await crud.InterfaceUsageDal(auth.db).create_data(data=data))


@app.delete("/interface/usage", summary="删除接口用量统计", description="硬删除", tags=["接口用量统计"])
async def delete_interface_usage_list(ids: IdList = Depends(), auth: Auth = Depends(AllUserAuth())):
    await crud.InterfaceUsageDal(auth.db).delete_datas(ids=ids.ids, v_soft=False)
    return SuccessResponse("删除成功")


@app.put("/interface/usage/{data_id}", summary="更新接口用量统计", tags=["接口用量统计"])
async def put_interface_usage(data_id: int, data: schemas.InterfaceUsage, auth: Auth = Depends(AllUserAuth())):
    return SuccessResponse(await crud.InterfaceUsageDal(auth.db).put_data(data_id, data))


@app.get("/interface/usage/{data_id}", summary="获取接口用量统计信息", tags=["接口用量统计"])
async def get_interface_usage(data_id: int, db: AsyncSession = Depends(db_getter)):
    schema = schemas.InterfaceUsageSimpleOut
    return SuccessResponse(await crud.InterfaceUsageDal(db).get_data(data_id, v_schema=schema))

