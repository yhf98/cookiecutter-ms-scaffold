#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/07/16 00:23
# @File           : order.py
# @IDE            : VSCode
# @desc           : 订单信息

from fastapi import Depends
from core.dependencies import Paging, QueryParams


class OrderParams(QueryParams):
    def __init__(self, params: Paging = Depends()):
        super().__init__(params)
