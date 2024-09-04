#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/07/29 16:40
# @File           : product_type.py
# @IDE            : VSCode
# @desc           : pydantic 模型，用于数据库序列化操作

from pydantic import BaseModel, Field, ConfigDict
from core.data_types import DatetimeStr
from typing import List, Optional
from apps.admin.product.models.product import Product

class ProductType(BaseModel):
    type_name: str = Field(..., title="产品类型名称")
    description: str | None = Field(None, title="产品类型描述")
    
    class Config:
        orm_mode = True

class ProductOutModel(BaseModel):
    id: int
    name: str
    description: str | None
    serve_name: str
    host: str
    protocol: str
    method: str
    port: int
    path: str | None
    route_path: str | None
    request_params: str | None
    request_header: str | None
    response_header: str | None
    status: int | None
    versions: str | None
    is_free: bool
    limit_of_seconds: int | None
    limit_of_minutes: int | None
    product_type_id: int
    create_user_id: int

    class Config:
        orm_mode = True

class ProductTypeSimpleOut(ProductType):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

    id: int = Field(..., title="编号")
    products: List[ProductOutModel]
    create_at: DatetimeStr = Field(..., title="创建时间")
    update_at: DatetimeStr = Field(..., title="更新时间")