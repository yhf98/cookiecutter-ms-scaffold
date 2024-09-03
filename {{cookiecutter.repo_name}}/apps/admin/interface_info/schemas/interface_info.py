#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/07/10 00:01
# @File           : interface_info.py
# @IDE            : VSCode
# @desc           : pydantic 模型，用于数据库序列化操作

from pydantic import BaseModel, Field, ConfigDict
from core.data_types import DatetimeStr


class InterfaceInfo(BaseModel):
    name: str = Field(..., title="接口名称")
    description: str = Field(..., title="接口描述")
    host: str = Field(..., title="接口主机、IP")
    protocol: str = Field(..., title="协议:http、https")
    port: int = Field(80, title="端口")
    method: str = Field(..., title="请求方式：GET、POST、PUT、DELETE")
    route_path: str = Field(..., title="路由地址：/tts【必须已“/”开始】")
    request_params: str = Field(..., title="请求参数")
    request_header: str = Field(..., title="请求头")
    response_header: str = Field(..., title="响应头")
    status: int = Field(0, title="状态，0：开启，1：关闭")
    create_user_id: int = Field(..., title="创建人")


class InterfaceInfoSimpleOut(InterfaceInfo):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., title="编号")
    create_at: DatetimeStr = Field(..., title="创建时间")
    update_at: DatetimeStr = Field(..., title="更新时间")
