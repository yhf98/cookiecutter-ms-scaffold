#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/07/10 15:34
# @File           : enterprise.py
# @IDE            : VSCode
# @desc           : 企业信息

from fastapi import Depends
from core.dependencies import Paging, QueryParams


class EnterpriseParams(QueryParams):
    def __init__(self, params: Paging = Depends()):
        super().__init__(params)
