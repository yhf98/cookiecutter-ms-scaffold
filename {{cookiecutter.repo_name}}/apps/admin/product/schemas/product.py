#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/07/29 16:40
# @File           : product.py
# @IDE            : VSCode
# @desc           : pydantic 模型，用于数据库序列化操作

from pydantic import BaseModel, Field, ConfigDict
from core.data_types import DatetimeStr


class Product(BaseModel):
    name: str = Field(..., title="产品名称")
    description: str | None = Field(None, title="描述")
    serve_name: str = Field(..., title="服务名称")
    host: str = Field(..., title="接口主机、IP")
    protocol: str = Field("http", title="协议:http、https")
    method: str = Field("GET", title="请求方式：GET、POST、PUT、DELETE")
    port: int = Field(80, title="端口：1-65536")
    path: str | None = Field(None, title="服务根路径：/api/v1/ai")
    route_path: str | None = Field(None, title="网关路由地址：/tts")
    request_params: str | None = Field(None, title="请求参数")
    request_header: str | None = Field(None, title="请求头")
    response_header: str | None = Field(None, title="响应头")
    status: int | None = Field(0, title="状态，0：开启，1：关闭，2：其他")
    versions: str | None = Field(None, title="版本，接口版本号")
    is_free: bool = Field(False, title="是否是免费的接口，0：否，1：是")
    limit_of_seconds: int | None = Field(5, title="每秒可以发出的 HTTP 请求量")
    limit_of_minutes: int | None = Field(300, title="每分钟可以发出的 HTTP 请求量")
    product_type_id: int = Field(..., title="产品类型ID")
    create_user_id: int = Field(..., title="创建人")


class ProductSimpleOut(Product):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

    id: int = Field(..., title="编号")
    create_at: DatetimeStr = Field(..., title="创建时间")
    update_at: DatetimeStr = Field(..., title="更新时间")
    
class ProductTypeSimpleOut():
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., title="编号")
    type_name: str = Field(..., title="产品类型名称")
    description: str | None = Field(None, title="产品类型描述")
    create_at: DatetimeStr = Field(..., title="创建时间")
    update_at: DatetimeStr = Field(..., title="更新时间")
    
class ProductJoinOut(Product):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., title="编号")
    # product_type: ProductTypeSimpleOut
    
    create_at: DatetimeStr = Field(..., title="创建时间")
    update_at: DatetimeStr = Field(..., title="更新时间")
