#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/07/31 14:26
# @File           : usage.py
# @IDE            : VSCode
# @desc           : pydantic 模型，用于数据库序列化操作

from pydantic import BaseModel, Field, ConfigDict
from core.data_types import DatetimeStr


class Usage(BaseModel):
    product_name: str = Field(..., title="API名称")
    response_time: float | None = Field(0.0, title="响应时间")
    status: int | None = Field(0, title="状态，0：成功，1：失败")
    request_text: str | None = Field(None, title="接口请求文本")
    response_text: str | None = Field(None, title="接口响应文本")
    apikey: str | None = Field(None, title="API KEY")
    user_id: int = Field(..., title="用户ID")
    product_id: int = Field(..., title="产品ID")


class UsageSimpleOut(Usage):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., title="编号")
    create_at: DatetimeStr = Field(..., title="创建时间")
    update_at: DatetimeStr = Field(..., title="更新时间")
