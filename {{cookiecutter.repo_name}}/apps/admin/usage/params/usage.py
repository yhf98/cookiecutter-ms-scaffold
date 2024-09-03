#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/07/31 14:26
# @File           : usage.py
# @IDE            : VSCode
# @desc           : 产品用量记录

from fastapi import Depends
from core.dependencies import Paging, QueryParams


class UsageParams(QueryParams):
    def __init__(self, name: str = None,  params: Paging = Depends()):
        super().__init__(params)
        self.name = name