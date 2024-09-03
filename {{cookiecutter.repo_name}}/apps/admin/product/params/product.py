#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/07/29 16:40
# @File           : product.py
# @IDE            : VSCode
# @desc           : 产品信息

from fastapi import Depends
from core.dependencies import Paging, QueryParams


class ProductParams(QueryParams):
    def __init__(self, params: Paging = Depends()):
        super().__init__(params)
