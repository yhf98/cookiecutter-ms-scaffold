#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/07/16 00:27
# @File           : order_detail.py
# @IDE            : VSCode
# @desc           : 订单详情

from fastapi import Depends
from core.dependencies import Paging, QueryParams


class OrderDetailParams(QueryParams):
    def __init__(self, params: Paging = Depends()):
        super().__init__(params)
