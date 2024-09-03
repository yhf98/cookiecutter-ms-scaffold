#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/07/16 00:23
# @File           : order.py
# @IDE            : VSCode
# @desc           : pydantic 模型，用于数据库序列化操作

from pydantic import BaseModel, Field, ConfigDict
from core.data_types import DatetimeStr
from datetime import datetime
from decimal import Decimal


class Order(BaseModel):
    order_number: str = Field(..., title="订单编号")
    order_date: datetime = Field(..., title="订单日期")
    total_amount: Decimal = Field(..., title="订单总金额")
    status: int = Field(0, title="订单状态")
    user_id: int = Field(..., title="用户ID")
    create_user_id: int = Field(..., title="创建人")
    
    class Config:
        json_encoders = {
            Decimal: lambda v: str(v)
        }


class OrderSimpleOut(Order):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., title="编号")
    create_at: DatetimeStr = Field(..., title="创建时间")
    update_at: DatetimeStr = Field(..., title="更新时间")
