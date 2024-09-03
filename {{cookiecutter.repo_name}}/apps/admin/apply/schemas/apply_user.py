#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/07/20 17:55
# @File           : apply_user.py
# @IDE            : VSCode
# @desc           : pydantic 模型，用于数据库序列化操作

from pydantic import BaseModel, Field, ConfigDict
from core.data_types import DatetimeStr
from datetime import datetime


class ApplyUser(BaseModel):
    username: str | None = Field(None, title="用户名称")
    phone: str = Field(..., title="手机号")
    apply_date: datetime = Field(..., title="申请时间")
    intention_product: str | None = Field(None, title="意向产品")
    contact_name: str = Field(..., title="联系人姓名")
    contact_phone: str = Field(..., title="联系人电话")
    organize: str = Field(..., title="组织名称")
    status: int = Field(0, title="跟进状态：0-未跟进，1-已跟进")
    create_user_id: int = Field(..., title="创建人[跟进人]")


class ApplyUserSimpleOut(ApplyUser):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., title="编号")
    create_at: DatetimeStr = Field(..., title="创建时间")
    update_at: DatetimeStr = Field(..., title="更新时间")
