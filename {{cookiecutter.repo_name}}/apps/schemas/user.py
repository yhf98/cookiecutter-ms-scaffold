#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/09/04 13:57
# @File           : user.py
# @IDE            : VSCode
# @desc           : pydantic 模型，用于数据库序列化操作

from pydantic import BaseModel, Field, ConfigDict
from core.data_types import DatetimeStr


class User(BaseModel):
    username: str = Field(..., title="密码")
    age: int | None = Field(None, title="密码")


class UserSimpleOut(User):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., title="编号")
    create_at: DatetimeStr = Field(..., title="创建时间")
    update_at: DatetimeStr = Field(..., title="更新时间")
    
class UserCounterOut(BaseModel):
    total: int = Field(..., title="总数")