#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/07/17 00:16
# @File           : interface_usage.py
# @IDE            : VSCode
# @desc           : 接口用量统计

from fastapi import Depends
from core.dependencies import Paging, QueryParams


class InterfaceUsageParams(QueryParams):
    def __init__(self, params: Paging = Depends()):
        super().__init__(params)
