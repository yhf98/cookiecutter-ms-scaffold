from utils.response import ErrorResponse, SuccessResponse
from core.dependencies import IdList
from apps.admin.auth.utils.validation.auth import Auth
from sqlalchemy.ext.asyncio import AsyncSession
from apps.admin.auth.utils.current import OpenAuth, OpenAuth
from fastapi import Depends, APIRouter, UploadFile, File
from core.database import db_getter
from .... import params, schemas, models, crud
from apps.portal.home import models as page_models, schemas as page_schemas, crud as page_crud

app = APIRouter()

###########################################################
#    Test
###########################################################


@app.get("/list/{data_id}", summary="获取数据列表")
async def get_page_data(q: params.PageParams = Depends(), auth: Auth = Depends(OpenAuth())):
    """
    TODO: 获取数据列表🎎
    """
    datas, count = await page_crud.PageDal(auth.db).get_datas(**q.dict(), v_return_count=True)
    
    return SuccessResponse(data=datas, count=count)

@app.get("/page_data/{data_id}", summary="通过id获取数据-主数据库")
async def get_page_data(data_id: int, auth: Auth = Depends(OpenAuth())):
    """
    TODO: 获取数据🍦-主数据库
    """
    page = await page_crud.PageDal(auth.db).get_data_scales(data_id, v_schema=page_schemas.PageSimpleOut)
    
    return SuccessResponse(data=page)

@app.get("/page_data_secondary/{data_id}", summary="通过id获取数据-从数据库")
async def page_data_secondary(data_id: int, auth: Auth = Depends(OpenAuth())):
    """
    TODO: 获取数据🍦-主数据库
    """
    page = await page_crud.PageDal(auth.db_secondary).get_data_scales(data_id, v_schema=page_schemas.PageSimpleOut)
    
    return SuccessResponse(data=page)
