#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/07/17 00:16
# @File           : interface_usage.py
# @IDE            : VSCode
# @desc           : pydantic 模型，用于数据库序列化操作

from pydantic import BaseModel, Field, ConfigDict
from core.data_types import DatetimeStr
from datetime import datetime


class InterfaceUsage(BaseModel):
    interface_id: int = Field(..., title="接口ID")
    interface_name: str | None = Field(None, title="接口名称")
    enterprise_id: int = Field(..., title="企业ID")
    enterprise_name: str | None = Field(None, title="企业名称")
    url: str | None = Field(None, title="接口地址")
    error_num: int | None = Field(0, title="错误次数")
    success_num: int | None = Field(0, title="成功次数")
    max_duration: float | None = Field(0.0, title="最长耗时")
    remaining_calls: int | None = Field(0, title="剩余调用量")
    partition_date: datetime | None = Field(None, title="分区时间")


class InterfaceUsageSimpleOut(InterfaceUsage):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., title="编号")
    create_at: DatetimeStr = Field(..., title="创建时间")
    update_at: DatetimeStr = Field(..., title="更新时间")
