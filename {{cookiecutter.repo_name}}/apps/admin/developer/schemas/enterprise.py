#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/07/10 15:34
# @File           : enterprise.py
# @IDE            : VSCode
# @desc           : pydantic 模型，用于数据库序列化操作

from pydantic import BaseModel, Field, ConfigDict
from core.data_types import DatetimeStr


class Enterprise(BaseModel):
    enterprise_name: str = Field(..., title="企业名称")
    phone: str = Field(..., title="手机号码")
    legal_name: str = Field(..., title="法人姓名")
    legal_id_number: str = Field(..., title="法人身份证号")
    business_license: str = Field(..., title="营业执照")
    social_credit_code: str = Field(..., title="统一社会信用代码")
    status: int = Field(0, title="状态，0：正常，1：冻结")
    address: str | None = Field(None, title="地址")
    other_phone: str | None = Field(None, title="其他联系电话")
    email: str | None = Field(None, title="邮箱")
    industry: str | None = Field(None, title="行业")
    user_id: int = Field(..., title="用户ID")
    create_user_id: int = Field(..., title="创建人")


class EnterpriseSimpleOut(Enterprise):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., title="编号")
    create_at: DatetimeStr = Field(..., title="创建时间")
    update_at: DatetimeStr = Field(..., title="更新时间")
