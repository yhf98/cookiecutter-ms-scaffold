#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/07/16 00:27
# @File           : order_detail.py
# @IDE            : VSCode
# @desc           : pydantic 模型，用于数据库序列化操作

from pydantic import BaseModel, Field, ConfigDict
from core.data_types import DatetimeStr
from decimal import Decimal

class OrderDetail(BaseModel):
    order_id: int = Field(..., title="None")
    interface_id: int = Field(..., title="接口ID")
    interface_name: str = Field(..., title="接口名称")
    quantity: int = Field(..., title="数量")
    price: Decimal = Field(..., title="价格")
    discounted_amount: Decimal = Field(..., title="优惠价")
    discount: float = Field(..., title="折扣")


class OrderDetailSimpleOut(OrderDetail):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., title="编号")
    create_at: DatetimeStr = Field(..., title="创建时间")
    update_at: DatetimeStr = Field(..., title="更新时间")
